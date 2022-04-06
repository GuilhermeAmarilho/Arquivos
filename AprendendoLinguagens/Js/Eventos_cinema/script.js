var body=document.querySelector('body');
body.children[5].value=0;
var classe=[document.getElementsByClassName('inteira'),document.getElementsByClassName('meia')];
body.setAttribute('align','center');
body.children[0].setAttribute('style','color: blue;font: bold 30px Arial');body.children[0].setAttribute('disabled','');
var table=document.querySelector('table');
table.setAttribute('align','center');
var valorentrada=document.body.children[5];
var output=[document.querySelectorAll('output')[0],document.querySelectorAll('output')[1],document.querySelectorAll('output')[2],document.querySelectorAll('output')[3]];
var tr=document.querySelectorAll('tr');
for (b=0;b<tr.length;b++){
  for (a=0;a<16;a++){
    td=document.createElement('td');
    tr[b].appendChild(td);
  }
}
for(a=0, b=[0, 1, 2, 3, 4, 5, 12, 13, 14, 15, 16, 17, 20, 21, 28, 29, 36, 37, 44, 45, 52, 53, 60, 61];a<b.length;a++){
  c=document.querySelectorAll('td');
  c[b[a]].setAttribute('class','fuga');
}
function mudanca(){
  output[3].textContent=(classe[0].length*valorentrada.value)+(classe[1].length*(valorentrada.value/2));
  output[0].textContent=parseFloat(valorentrada.value)/2;
  if (classe[0].length==1) {output[1].textContent="1 Entrada Inteira     R$: "+valorentrada.value}
  if (classe[0].length!=1) {output[1].textContent=classe[0].length+" Entradas Inteiras    R$: "+classe[0].length*valorentrada.value}
  if (classe[0].length==0) {output[1].textContent="Nenhuma Entrada Inteira       R$ 00.00"}
  if (classe[1].length==1) {output[2].textContent="1 Meia-Entrada     R$: "+(valorentrada.value/2);}if (classe[1].length!=1) {output[2].textContent=classe[1].length+" Meias-Entradas     R$: "+classe[1].length*(valorentrada.value/2)}
  if (classe[1].length<1) {output[2].textContent="Nenhuma Meia-Entrada     R$: "+(valorentrada.value/2);}if (classe[1].length!=1) {output[2].textContent=classe[1].length+" Meias-Entradas     R$: "+classe[1].length*(valorentrada.value/2)}
  if (classe[1].length>1) {output[2].textContent=classe[1].length+" Meia-Entrada     R$: "+(valorentrada.value/2);}if (classe[1].length!=1) {output[2].textContent=classe[1].length+" Meias-Entradas     R$: "+classe[1].length*(valorentrada.value/2)}
}
table.addEventListener('click', function(evento) {
  var celula = evento.target;
  if ((celula.className!="fuga")&&(celula!=table)&&(celula!=tr[0])&&(celula!=tr[1])&&(celula!=tr[2])&&(celula!=tr[3])&&(celula!=tr[4])&&(celula!=table.children[0])) {
    switch (celula.className) {
      case "":celula.className='inteira';break;
      case "inteira":celula.className='meia';break;
      case "meia":celula.className='';break;
    }
    mudanca();
  }
});
onkeyup=function () {
  mudanca();
}
