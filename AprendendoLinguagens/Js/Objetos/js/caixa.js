function roda(valor){
  cedulas=[5,10,20,50,100];
  posicao=-1;
  for	(i=0;i<5;i++){
    if(valor==cedulas[i]){
      posicao=i;
    }
  }
  return posicao;
}

function ATM(){
  this.cedulas=[[5,0],[10,0],[20,0],[50,0],[100,0]];
  this.abastecer=function(quantidade,valor){
    if ((valor==5)||(valor==10)||(valor==20)||(valor==50)||(valor==100)){
      if ((valor<=1000)) {
        i=roda(valor);
        this.cedulas[i][1]=quantidade;
      }
      else{
        return "limite maximo de sedulas exedido";
      }
    }
  }
  this.consultarQuantidade=function(valor){
    i=roda(valor);
    if(i!=-1){
      return this.cedulas[i][1];
    }
    else{
      return 0;
    }
  }
  this.consultarValor=function(){
    for (var i=0, posicao=0; i < 5; i++) {
      posicao+=this.cedulas[i][0]*this.cedulas[i][1];
    }
    return posicao;
  }
  this.retirar=function(valor){
    a=this.cedulas;
    x=[a[0][1],a[1][1],a[2][1],a[3][1],a[4][1]];
    for (var i = 4; i >=0; i--) {
      for (var b=a[i];((b[1]>0)&&(valor/b[0]>=1));) {
        b[1]-=1
        valor-=b[0]
      }
    }
    if (valor>0) {
      for (var i = 0; i < 5; i++) {
        this.cedulas[i][1]=x[i];
      }
    }
    else {
      this.cedulas=a;
    }
  }
}
const atm = new ATM();
atm.abastecer(33, 100);
console.log(atm.consultarQuantidade(100));
console.log(atm.consultarQuantidade(100) === 33);
console.log(atm.consultarQuantidade(5));
console.log(atm.consultarQuantidade(5) === 0);
console.log(atm.consultarQuantidade(50));
console.log(atm.consultarQuantidade(50) === 0);
console.log(atm.consultarQuantidade(3));
console.log(atm.consultarQuantidade(3) === 0);
atm.abastecer(8, 3);
console.log(atm.consultarQuantidade(3) === 0);
console.log(atm.consultarValor());
console.log(atm.consultarValor() === 3300);
atm.retirar(350);
console.log(atm.consultarQuantidade(100) === 33);
console.log(atm.consultarValor() === 3300);
atm.retirar(300);
console.log(atm.consultarQuantidade(100) === 30);
console.log(atm.consultarValor() === 3000);
atm.retirar(3100);
console.log(atm.consultarQuantidade(100) === 30);
console.log(atm.consultarValor() === 3000);
atm.retirar(3000);
console.log(atm.consultarQuantidade(100) === 0);
console.log(atm.consultarValor() === 0);
atm.abastecer(10, 10);
atm.abastecer(10, 50);
console.log(atm.consultarQuantidade(10) === 10);
console.log(atm.consultarQuantidade(50) === 10);
console.log(atm.consultarValor() === 600);
atm.retirar(100);
console.log(atm.consultarQuantidade(10) === 10);
console.log(atm.consultarQuantidade(50) === 8);
console.log(atm.consultarValor() === 500);
atm.retirar(90);
console.log(atm.consultarQuantidade(10) === 6);
console.log(atm.consultarQuantidade(50) === 7);
console.log(atm.consultarValor() === 410);
//minha parte
atm2=new ATM()
atm2.abastecer(20, 100);
atm2.abastecer(20, 20);
atm2.abastecer(20, 50);
atm2.abastecer(20, 10);
atm2.abastecer(20, 5);

console.log(atm2.consultarValor());
atm2.retirar(645);
console.log(atm2.consultarValor());

atm2.retirar(85);
console.log(atm2.consultarValor());

atm2.retirar(375);
console.log(atm2.consultarValor());

atm2.retirar(1500);
console.log(atm2.consultarValor());

atm2.retirar(495);
console.log(atm2.consultarValor());

atm2.retirar(235);
console.log(atm2.consultarValor());
//aqui acabou as notas de 100 e de 50
atm2.retirar(365);
console.log(atm2.consultarValor());
//zerou
atm2.abastecer(8, 100);
atm2.abastecer(1, 50);
atm2.abastecer(12, 5);
atm2.abastecer(1, 20);
console.log(atm2.consultarValor());
atm2.retirar(920);
console.log(atm2.consultarValor());
atm2.abastecer(4, 100);
atm2.abastecer(7, 20);
console.log(atm2.consultarValor());
atm2.retirar(545);
console.log(atm2.consultarValor());
atm2.abastecer(99, 50);
atm2.abastecer(3, 10);
atm2.abastecer(2, 20);
console.log(atm2.consultarValor());
atm2.retirar(5025);
console.log(atm2.consultarValor());
