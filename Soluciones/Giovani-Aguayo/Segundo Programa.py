
def numerosEnteros(parametroUno, parametroDos):

	p1=0
	p2=0
	for i in range(100):
		if i%3==0:
			if i%5==0:
				p1+=1
				p2+=1
				print(parametroDos, "Y", parametroUno)
			else:
				p1+=1
				print (parametroUno)
		else: 
			p2+=1
			print(parametroDos)
	return p1,p2

p1, p2= numerosEnteros("Multiplo de 3", "Multiplo de 5") 

print("Numeros multiplos de cinco =", p2)
print("Numeros multiplos de tres =", p1)