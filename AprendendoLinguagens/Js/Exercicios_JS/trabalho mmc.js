	//calcular o mmc de dois numeros

	n1=parseInt(prompt("Informe o 1º valor: ")); 
	n2=parseInt(prompt("Informe o 2º valor: "));
	a=2;
	b=2;
	a1=1;
	b1=1;
	v=2;
	x=0;
	c=1;
	n11=n1;
	n22=n2;
	if	((n1%n2==0)||(n2%n1==0)){
		if	(n1>n2){
			alert("O mmc de "+n1+" e "+n2+" é: "+n1);
			x++;
		}	
		if	(n1<n2){
			alert("O mmc de "+n1+" e "+n2+" é: "+n2);
			x++;
		}
		if	(n1==n2){
			alert("O mmc de "+n1+" e "+n2+" é: "+n1);
			x++;
		}
	}
	if	(x==0) {
		if	(n1!=n2) {
			while (n1%a!=0) {
					a++;
			}
			while (n2%b!=0) {
					b++;
			}
			if	(a!=b) {
				alert("O mmc de "+n1+" e "+n2+" é: "+(n1*n2));
				x++;
			}
		}
	}
	if	(x==0) {
		if	(n1!=n2) {
			while (n1%a!=0) {
					a++;
			}
			while (n2%b!=0) {
					b++;
			}
			if	(a==b) {
				n1=n1/a;
				n2=n2/a;
				c=a;
				while ((n1>1)&&(n2>1)){
					while (n1%a!=0) {
							a++;
					}
					while (n2%b!=0) {
							b++;
					}
					if(a==b){
						c*=a;
					}
					if(a!=b){
						c=c*a*b;
					}
					n1/=a;
					n2/=b;
				}
				alert("O mmc de "+n11+" e "+n22+" é: "+c);
			}
		}
	}
	
	