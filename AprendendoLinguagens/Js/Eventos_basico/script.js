var table = document.querySelector('table');
table.addEventListener('click', function(evento) {
  document.getElementById('para').value=evento.target.innerText;
})
var avatar=document.getElementById('avatar');
avatar.addEventListener('click',function(evento){
  document.getElementById('imagem').src=prompt("URL");
})
var botao=document.getElementById('save');
botao.addEventListener('click', function(evento) {
  var div=document.getElementById('h');
  var par=document.createElement('p');
  par.innerHTML="Para: " + document.getElementById('para').value + "   Assunto: " + document.getElementById('assunto').value;
  div.appendChild(par);
  document.getElementById('para').value="Para";
  document.getElementById('assunto').value="Assunto";
  document.getElementById('text').value="";
})
