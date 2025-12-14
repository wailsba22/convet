"""
Quran Video Generator - Web Version
Flask-based web app for generating Quran videos
"""
from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
import json
import threading
import uuid
from quran_video_generator import QuranVideoGenerator
import os

app = Flask(__name__)
app.secret_key = 'quran_video_generator_secret_key_2025'

# Store active generation tasks
active_tasks = {}

# Ensure output directories exist
OUTPUT_DIR = Path("web_output")
OUTPUT_DIR.mkdir(exist_ok=True)

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/generate/random', methods=['POST'])
def generate_random():
    """Generate random video(s)"""
    data = request.json
    count = data.get('count', 1)
    second_language = data.get('second_language', 'en')
    reciter = data.get('reciter', 'ar.alafasy')
    
    # Create task ID
    task_id = str(uuid.uuid4())
    
    # Create generator
    generator = QuranVideoGenerator(
        output_dir=str(OUTPUT_DIR),
        background_videos_dir="backgrounds"
    )
    generator.subtitle_languages = ["ar", second_language]
    generator.default_reciter = reciter
    
    # Store task
    active_tasks[task_id] = {
        'status': 'starting',
        'progress': 0,
        'current': 0,
        'total': count,
        'videos': []
    }
    
    # Start generation in background thread
    thread = threading.Thread(
        target=generate_random_worker,
        args=(task_id, generator, count)
    )
    thread.daemon = True
    thread.start()
    
    return jsonify({'task_id': task_id})

def generate_random_worker(task_id, generator, count):
    """Background worker for random generation"""
    try:
        for i in range(count):
            active_tasks[task_id]['status'] = f'Generating video {i+1} of {count}...'
            active_tasks[task_id]['current'] = i
            
            # Progress callback
            def progress_callback(progress, msg=""):
                active_tasks[task_id]['progress'] = int(((i + progress/100) / count) * 100)
                if msg:
                    active_tasks[task_id]['status'] = msg
                return True  # Always return True to continue processing
            
            video_path = generator.generate_random_video(
                progress_callback=progress_callback
            )
            
            if video_path:
                video_name = Path(video_path).name
                active_tasks[task_id]['videos'].append({
                    'name': video_name,
                    'path': str(video_path)
                })
            
            active_tasks[task_id]['current'] = i + 1
        
        active_tasks[task_id]['status'] = 'completed'
        active_tasks[task_id]['progress'] = 100
        
    except Exception as e:
        active_tasks[task_id]['status'] = 'failed'
        active_tasks[task_id]['error'] = str(e)

@app.route('/api/generate/range', methods=['POST'])
def generate_range():
    """Generate range of verses from a single surah"""
    data = request.json
    surah = data.get('surah')
    start_verse = data.get('start_verse')
    end_verse = data.get('end_verse')
    second_language = data.get('second_language', 'en')
    reciter = data.get('reciter', 'ar.alafasy')
    
    # Create task ID
    task_id = str(uuid.uuid4())
    
    # Create generator
    generator = QuranVideoGenerator(
        output_dir=str(OUTPUT_DIR),
        background_videos_dir="backgrounds"
    )
    generator.subtitle_languages = ["ar", second_language]
    generator.default_reciter = reciter
    
    # Store task
    active_tasks[task_id] = {
        'status': 'starting',
        'progress': 0,
        'current': 0,
        'total': 1,
        'videos': []
    }
    
    # Start generation in background thread
    thread = threading.Thread(
        target=generate_range_worker,
        args=(task_id, generator, surah, start_verse, end_verse)
    )
    thread.daemon = True
    thread.start()
    
    return jsonify({'task_id': task_id})



def generate_range_worker(task_id, generator, surah, start_verse, end_verse):
    """Background worker for range generation"""
    try:
        active_tasks[task_id]['status'] = 'Generating video range...'
        
        def progress_callback(progress, msg=""):
            active_tasks[task_id]['progress'] = progress
            if msg:
                active_tasks[task_id]['status'] = msg
            return True  # Always return True to continue processing
        
        video_path = generator.generate_video(
            surah=surah,
            ayah_start=start_verse,
            ayah_end=end_verse,
            progress_callback=progress_callback
        )
        
        if video_path:
            video_name = Path(video_path).name
            active_tasks[task_id]['videos'].append({
                'name': video_name,
                'path': str(video_path)
            })
        
        active_tasks[task_id]['status'] = 'completed'
        active_tasks[task_id]['progress'] = 100
        active_tasks[task_id]['current'] = 1
        
    except Exception as e:
        active_tasks[task_id]['status'] = 'failed'
        active_tasks[task_id]['error'] = str(e)

@app.route('/api/progress/<task_id>')
def get_progress(task_id):
    """Get generation progress"""
    if task_id in active_tasks:
        return jsonify(active_tasks[task_id])
    return jsonify({'status': 'not_found'}), 404

@app.route('/api/download/<path:filename>')
def download_video(filename):
    """Download generated video"""
    file_path = OUTPUT_DIR / filename
    if file_path.exists():
        return send_file(str(file_path), as_attachment=True)
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    # Use environment port if available (for deployment)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
