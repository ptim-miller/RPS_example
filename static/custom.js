document.addEventListener('readystatechange', event => {
    if (event.target.readyState === "complete") {
        document.getElementById("page_audio").play();
    }
});

document.addEventListener('keydown', function(event){
    if(event.keyCode == 49)
      document.getElementById('Rock').click();
    if(event.keyCode == 50)
      document.getElementById('Paper').click();
    if(event.keyCode == 51)
      document.getElementById('Scissors').click();
});