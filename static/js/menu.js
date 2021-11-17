function showmenu() {
    const icon = document.getElementById('navbar')
    const menu = document.getElementById('menu')
    const navl = document.getElementsByClassName('nav-links')
    const bd = document.getElementsByTagName('body')[0]


    if (icon.textContent.trim() === "dehaze") {
        openmenu(icon, menu, navl[0])
        bd.style.overflow = 'hidden'

    } else {
        closemenu(icon, menu, navl[0])
        bd.style.overflow = 'auto'
    }
}

function openmenu(icon, menu, nav) {
    icon.innerHTML = `<i class="material-icons nav-icon">clear</i>`;
    delayit(icon, 0.3)
    icon.style.transform = 'rotate(90deg)';
    menuHW(menu, "600vh")
    fadeIn(nav)
}


function closemenu(icon, menu, nav,bd) {
    delayit(icon, 0.3)
    icon.style.transform = 'rotate(180deg)';
    menuHW(menu, "40px")
    icon.innerHTML = `<i class="material-icons nav-icon">dehaze</i>`;
    fadeOut(nav)
}

function menuHW(menu, size) {
    menu.style.height = size
    menu.style.width = size
}



function delayit(element, delay) {
    element.style.WebkitTransitionDuration = `${delay}s`
}



// ** FADE OUT FUNCTION **
function fadeOut(el) {
    el.style.opacity = 1;
    (function fade() {
        if ((el.style.opacity -= .1) < 0) {
            el.style.display = "none";
        } else {
            requestAnimationFrame(fade);
        }
    })();
};

// ** FADE IN FUNCTION **
function fadeIn(el, display) {
    el.style.opacity = 0;
    el.style.display = display || "block";
    (function fade() {
        var val = parseFloat(el.style.opacity);
        if (!((val += .1) > 1)) {
            el.style.opacity = val;
            requestAnimationFrame(fade);
        }
    })();
};