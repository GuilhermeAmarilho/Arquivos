let center = document.querySelector('div.center');
let body = document.body;
let display = document.querySelector('div.display');
let color = document.querySelector('div.color');
let x = document.querySelector('button.x');
body.addEventListener('click',function(e){
    if(e.target.classList[0]=='cor'){
        display.style.background=e.target.classList[1];
    }
    if(e.target.classList[0]=='definir'){
        center.style.background = display.style.background;
    }
})
x.addEventListener('click',function(e){
    color.style.marginLeft='-600px'
})