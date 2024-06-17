document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('mySidebar');
    const mainContent = document.getElementById('main');
    const toggleBtn = document.querySelector('.sidebar-btn');

    function toggleSidebarStyle(open) {
        const width = open ? '250px' : '0';
        sidebar.style.width = width;
        mainContent.style.marginRight = width;
    }

    toggleBtn.onclick = function() {
        const isOpen = sidebar.style.width === '250px';
        toggleSidebarStyle(!isOpen);
    };

    window.toggleSidebar = function() {
        toggleSidebarStyle(sidebar.style.width === '0');
    };
});