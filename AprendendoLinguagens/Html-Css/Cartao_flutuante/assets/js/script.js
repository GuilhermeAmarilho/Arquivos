var img = document.getElementById("img");
var $JQuery2 = jQuery.noConflict()
$JQuery2(function() {
   $JQuery2(".card").hover(
      function(){
         img.src = img.src.replace("img1","img2");
      },
      function(){
        img.src = img.src.replace("img2","img1");
      });
});