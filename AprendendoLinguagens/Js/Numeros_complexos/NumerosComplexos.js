var aux=[,];
var num={};
function Complex (val,img){
	val+=""; //para garantir que ele será uma string
	var num={};
	if(img==aux[3]){//se for dado na forma de string, a img ficara undefined.
		for(;val.indexOf(" ")!=-1;){val=val.replace(" ","")}
		if(val.indexOf("i")!=-1){
			if((val.indexOf("+")!=-1)||(val.indexOf("+")!=-1)){
				num.real=parseFloat(val);
				if(val.indexOf("+")!=-1){num.imaginary=parseFloat(val.substr(val.indexOf("+")))}
				if(val.indexOf("-")!=-1){num.imaginary=parseFloat(val.substr(val.indexOf("-")))}
			}
			else{num.real=0;num.imaginary=parseFloat(val)}
		}
		else{num.real=parseFloat(val);num.imaginary=0}
	}
	else{num.real=parseFloat(val);num.imaginary=img}
	return num;
}
function add(val1,val2){
	var num={};
	num.real=val1.real+val2.real;
	num.imaginary=val1.imaginary+val2.imaginary;
	return num;
}
function subtract(val1,val2){
	var num={};
	num.real=val1.real-val2.real;
	num.imaginary=val1.imaginary-val2.imaginary;
	return num;
}
function multiply(val1,val2){
	var num={};
	num.real=val1.real*val2.real+val1.imaginary*val2.imaginary*-1
	num.imaginary=val1.real*val2.imaginary+val2.real*val1.imaginary;
	return num;
}
function conjugate(val){
	val.imaginary*=-1;
	return val;
}
function complexToString(val){
	num=""+val.real;
	if	(val.imaginary>0){
		num+="+"+val.imaginary+"i";
	}
	else{if	(val.imaginary!=0){num+=val.imaginary+"i"}}
	return num;
}
var c1 = {real: 2, imaginary: 3};
console.log(c1.real === 2);
console.log(c1.imaginary === 3);

var c2 = Complex('2+3i');
console.log(c2.real === 2);
console.log(c2.imaginary === 3);

var c3 = Complex('5');
console.log(c3.real === 5);
console.log(c3.imaginary === 0);

var c4 = Complex('4i');
console.log(c4.real === 0);
console.log(c4.imaginary === 4);

var c5 = Complex('5 + 4i');
console.log(c5.real === 5);
console.log(c5.imaginary === 4);

var c6 = Complex('5.5 + 4.3i');
console.log(c6.real === 5.5);
console.log(c6.imaginary === 4.3);

var c7 = Complex(2, 3);
console.log(c7.real === 2);
console.log(c7.imaginary === 3);

var c8 = Complex(2);
console.log(c8.real === 2);
console.log(c8.imaginary === 0);

var c9 = add(c1, c5); // 2+3i + 5+4i = 7+7i
console.log(c9.real === 7);
console.log(c9.imaginary === 7);
   var c10 = subtract(c5, c1); // 5+4i - 2+3i = 3+1i    console.log(c10.real === 3);    console.log(c10.imaginary === 1);

var c11 = multiply(c1, c9); // 2+3i * 7+7i = 2*7 - 3*7
console.log(c11.real === -7);
console.log(c11.imaginary === 35);
   var c12 = subtract(c1, c10); // 2+3i - 3+1i = -1+2i    console.log(c12.real === -1);    console.log(c12.imaginary === 2);

var c13 = conjugate(c9); // conjugate(7+7i) = 7-7i
console.log(c13.real === 7);
console.log(c13.imaginary === -7);

console.log(add(Complex("4+7i"), Complex("5+9i")).real === 9);
console.log(add(Complex("4+7i"), Complex("5+9i")).imaginary === 16);

// adicione mais 2 casos de teste para add, multiply, subtract e conjugate

var s1 = complexToString(c11);
console.log(s1 === "-7+35i");
console.log(complexToString(c12) === "-1+2i");
console.log(complexToString(c13) === "7-7i");
console.log(complexToString(Complex(8)) === "8");
console.log(complexToString(Complex(8, 2)) === "8+2i");
console.log(complexToString(Complex("8 + 2i")) === "8+2i");
