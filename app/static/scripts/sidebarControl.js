import { toggleSidebarStyle } from './utils.js';

document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.querySelector('.sidebar-btn');

    toggleBtn.onclick = function() {
        const isOpen = sidebar.style.width === '250px';
        toggleSidebarStyle(!isOpen);
    };

    window.toggleSidebar = function() {
        toggleSidebarStyle(sidebar.style.width === '0');
    };
});