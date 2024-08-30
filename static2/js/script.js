// Bismillah
// Scroll to the top visibility
const backToTop = document.querySelector(".back-top")

window.addEventListener("scroll", ()=>{
    const header = document.querySelector('header')
    const links = document.querySelector('nav ul li a')

    backToTop.style.display =  window.scrollY > 150 ?'block': 'none'

    if (window.scrollY > 0){
        header.classList.add("scroll-down")
        links.classList.add("nav-down")
    }
    else{
        header.classList.remove('scroll-down')
        links.classList.remove('nav-down')
    }
})


let box = document.querySelectorAll('.choose-us-item')
let boxi = document.querySelectorAll('.choose-us-item i')



