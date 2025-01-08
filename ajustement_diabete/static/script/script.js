let downArc = document.getElementById("down-arc");
let sousMenu = document.querySelector(".sous-menu");
let menuHamburger = document.getElementById("menu-hamburger");
let menu = document.querySelector(".menu-hamburger");
let exitMenu = document.querySelector(".exit-menu");
let languePrincipale = document.querySelector(".langue-principale");
let body = document.body;
downArc.addEventListener("click" , ()=> {
    sousMenu.classList.toggle("sous-menu-active");
});
document.addEventListener("click" , ()=> {
    if(!downArc.contains(event.target)) {
        sousMenu.classList.remove("sous-menu-active");
    }
});
menuHamburger.addEventListener("click" , ()=> {
    menu.classList.add("menu-hamburger-active");
    exitMenu.classList.add("exit-menu-active");
    languePrincipale.classList.add("langue-principale-active");
    body.classList.add("no-scroll");
})
exitMenu.addEventListener("click" ,()=> {
    exitMenu.classList.remove("exit-menu-active");
    menu.classList.remove("menu-hamburger-active");
    languePrincipale.classList.remove("langue-principale-active");
    body.classList.add("no-scroll");
})