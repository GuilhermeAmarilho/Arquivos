var h1=document.querySelector('h1');
function pegar(){navigator.geolocation.getCurrentPosition(local)}
function local(posicao){
    var c={};
    c.lat=posicao.coords.latitude;
    c.long=posicao.coords.longitude;
    h1.innerHTML+="<br><br>Latitude: "+c.lat+"<br>Longitude: "+c.long;
  }
  pegar ();
