// Tab switching functionality
const tabs = document.querySelectorAll('.tab');
const tabContents = document.querySelectorAll('.tab-content');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const tabName = tab.getAttribute('data-tab');
        
        // Remove active class from all tabs and contents
        tabs.forEach(t => t.classList.remove('active'));
        tabContents.forEach(content => content.classList.remove('active'));
        
        // Add active class to clicked tab and corresponding content
        tab.classList.add('active');
        document.getElementById(tabName).classList.add('active');
    });
});

// Form submission handlers
document.getElementById('randomForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {
        count: parseInt(formData.get('count')),
        second_language: formData.get('second_language'),
        reciter: formData.get('reciter')
    };
    await generateVideos('/api/generate/random', data);
});

document.getElementById('rangeForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {
        surah: parseInt(formData.get('surah')),
        start_verse: parseInt(formData.get('start_verse')),
        end_verse: parseInt(formData.get('end_verse')),
        second_language: formData.get('second_language'),
        reciter: formData.get('reciter')
    };
    await generateVideos('/api/generate/range', data);
});

// Video generation function
async function generateVideos(endpoint, data) {
    // Show progress section
    document.getElementById('progressSection').style.display = 'block';
    document.getElementById('resultsSection').style.display = 'none';
    
    // Disable all forms
    document.querySelectorAll('form').forEach(form => {
        form.querySelectorAll('button').forEach(btn => btn.disabled = true);
    });

    try {
        // Start generation
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        if (result.task_id) {
            // Poll for progress
            pollProgress(result.task_id);
        } else {
            throw new Error(result.error || 'Failed to start generation');
        }
    } catch (error) {
        alert('Error: ' + error.message);
        resetGenerator();
    }
}

// Poll progress function
function pollProgress(taskId) {
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');
    const progressDetails = document.getElementById('progressDetails');
    
    const interval = setInterval(async () => {
        try {
            const response = await fetch(`/api/progress/${taskId}`);
            const progress = await response.json();
            
            // Update progress
            const percentage = progress.total > 0 
                ? Math.round((progress.current / progress.total) * 100)
                : 0;
            
            progressBar.style.width = percentage + '%';
            progressText.textContent = progress.status;
            progressDetails.textContent = `${progress.current} of ${progress.total} videos`;
            
            // Check if complete
            if (progress.status === 'completed') {
                clearInterval(interval);
                showResults(progress.videos);
            } else if (progress.status === 'failed') {
                clearInterval(interval);
                alert('Video generation failed: ' + (progress.error || 'Unknown error'));
                resetGenerator();
            }
        } catch (error) {
            clearInterval(interval);
            alert('Error checking progress: ' + error.message);
            resetGenerator();
        }
    }, 1000); // Poll every second
}

// Show results function
function showResults(videos) {
    document.getElementById('progressSection').style.display = 'none';
    document.getElementById('resultsSection').style.display = 'block';
    
    const videoList = document.getElementById('videoList');
    videoList.innerHTML = '';
    
    if (videos && videos.length > 0) {
        videos.forEach(video => {
            const videoItem = document.createElement('div');
            videoItem.className = 'video-item';
            videoItem.innerHTML = `
                <h4>${video.name}</h4>
                <a href="/api/download/${encodeURIComponent(video.name)}" download>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                        <polyline points="7 10 12 15 17 10"></polyline>
                        <line x1="12" y1="15" x2="12" y2="3"></line>
                    </svg>
                    Download Video
                </a>
            `;
            videoList.appendChild(videoItem);
        });
    } else {
        videoList.innerHTML = '<p style="text-align: center; color: var(--text-secondary);">No videos generated</p>';
    }
}

// Reset function
function resetGenerator() {
    document.getElementById('progressSection').style.display = 'none';
    document.getElementById('resultsSection').style.display = 'none';
    
    // Re-enable all forms
    document.querySelectorAll('form').forEach(form => {
        form.querySelectorAll('button').forEach(btn => btn.disabled = false);
        form.reset();
    });
    
    // Reset progress
    document.getElementById('progressBar').style.width = '0%';
}

// Smooth scroll animation for page load
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    }, 100);
});
