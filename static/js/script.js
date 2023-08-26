const navProfileIcon = document.querySelector('#navProfileIcon');
const navProfileIconMenu = document.getElementById('navProfileIconMenu')
const sidebarBtn = document.getElementById('sidebarBtn')
const sidebar = document.getElementById('sidebar')

navProfileIcon.addEventListener('click',()=>{
    navProfileIconMenu.classList.toggle('hidden')
});

sidebarBtn.addEventListener('click',()=>{
    sidebar.classList.toggle('hidden')      
});

