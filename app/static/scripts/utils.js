const Utils = (() => {
    const progressBar = document.getElementById('progress-bar');
    const remainingCount = document.getElementById('remaining-count');

    function updateProgressBar(totalUseCases, completedUseCases) {
        const progressPercentage = (completedUseCases / totalUseCases) * 100;
        progressBar.style.width = `${progressPercentage}%`;
        progressBar.textContent = `${progressPercentage.toFixed(0)}%`;
    }

    function updateRemainingUseCases(totalUseCases, completedUseCases) {
        remainingCount.textContent = totalUseCases - completedUseCases;
    }

    function playSound(file) {
        const audio = new Audio(`/static/${file}`);
        audio.play();
    }

    return {
        updateProgressBar,
        updateRemainingUseCases,
        playSound
    };
})();