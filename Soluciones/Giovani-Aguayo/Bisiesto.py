from datetime import datetime, timedelta
def numeroEntero():
	numero=int(input("Introduce el numero "))
	fechaBase=datetime(1,1,1)

	fechaResultado = fechaBase+timedelta(days=numero)

	print(fechaResultado.strftime("%d/%m/%Y"))

##return fecha

numeroEntero()