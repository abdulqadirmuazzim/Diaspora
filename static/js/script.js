// Bismillah
// Scroll to the top visibility
const backToTop = document.querySelector(".back-top")

window.addEventListener("scroll", ()=>{
    backToTop.style.display =  window.scrollY > 150 ?'block': 'none'
})

// Nav scrolling effect
let lastScrollTop = 0;
const header = document.querySelector(".navigation-bar");

window.addEventListener("scroll", function () {
    let scrollTop = window.scrollY;
    console.log(scrollTop)
    if (scrollTop > lastScrollTop) {
        // Scrolling down
        header.classList.add("scroll-up")
        header.classList.add("shadow")
    } else {
        // Scrolling up
        header.classList.remove("scroll-up");
    }
    if (scrollTop == 0){
        header.classList.remove("shadow");
    }
    lastScrollTop = scrollTop;
});

let box = document.querySelectorAll('.choose-us-item')
let boxi = document.querySelectorAll('.choose-us-item i')



