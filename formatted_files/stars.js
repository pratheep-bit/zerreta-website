document.addEventListener('DOMContentLoaded', function() {
    // Create the stars container if it doesn't exist
    let container = document.getElementById('starsContainer');
    if (!container) {
        container = document.createElement('div');
        container.id = 'starsContainer';
        container.className = 'stars-container';
        document.body.insertBefore(container, document.body.firstChild);
    }
    
    const numStars = 150;
    
    for (let i = 0; i < numStars; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        
        // Random size
        const size = Math.random() * 2.5 + 0.5;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        
        // Random position
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        
        // Random movement direction
        const angle = Math.random() * Math.PI * 2;
        const distance = Math.random() * 300 + 100;
        const xDistance = Math.cos(angle) * distance;
        const yDistance = Math.sin(angle) * distance;
        star.style.setProperty('--x-distance', `${xDistance}px`);
        star.style.setProperty('--y-distance', `${yDistance}px`);
        
        // Random animation duration
        const duration = Math.random() * 25 + 15;
        star.style.setProperty('--duration', `${duration}s`);
        
        // Random animation delay
        star.style.animationDelay = `${Math.random() * 25}s`;
        
        container.appendChild(star);
    }
}); 