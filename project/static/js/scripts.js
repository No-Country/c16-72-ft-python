let btn_back = document.querySelector(".return");

btn_back.addEventListener('click', function(e){
    e.preventDefault();
    window.history.back();
});