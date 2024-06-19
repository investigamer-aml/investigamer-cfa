export function updateProgressBar(totalUseCases, completedUseCases) {
    const progressBar = document.getElementById('progress-bar');
    const progressPercentage = (completedUseCases / totalUseCases) * 100;
    progressBar.style.width = `${progressPercentage}%`;
    progressBar.textContent = `${progressPercentage.toFixed(0)}%`;
}

export function updateRemainingUseCases(totalUseCases, completedUseCases) {
    const remainingCount = document.getElementById('remaining-count');
    remainingCount.textContent = totalUseCases - completedUseCases;
}

export function toggleSidebarStyle(open) {
    const sidebar = document.getElementById('mySidebar');
    const mainContent = document.getElementById('main');
    const width = open ? '250px' : '0';
    sidebar.style.width = width;
    mainContent.style.marginRight = width;
}

export function playSound(file) {
    const audio = new Audio(`/static/${file}`);
    audio.play();
}