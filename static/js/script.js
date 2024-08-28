// Bismillah
// Scroll to the top visibility
const backToTop = document.querySelector(".back-top")

window.addEventListener("scroll", ()=>{
    backToTop.style.display =  window.scrollY > 150 ?'block': 'none'
})


let box = document.querySelectorAll('.choose-us-item')
let boxi = document.querySelectorAll('.choose-us-item i')



