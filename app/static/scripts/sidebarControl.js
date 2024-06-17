import { toggleSidebarStyle } from './utils.js';

document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.querySelector('.sidebar-btn');
    const sidebar = document.querySelector('.sidebar');

    console.log(sidebar)

    toggleBtn.onclick = function() {
        const isOpen = sidebar.style.width === '250px';
        toggleSidebarStyle(!isOpen);
    };

    window.toggleSidebar = function() {
        toggleSidebarStyle(sidebar.style.width === '0');
    };
});