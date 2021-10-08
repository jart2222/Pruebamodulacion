class Vehiculos():

	def __init__(self, marca, modelo): 
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena =False
	def arrancar(self):
		self.enmarcha=True
	def acelera(self):
		self.acelera=True 
	def frenar(self):
		self.frena=True
	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "la Furgoneta esta cargada"
		else:
			return "la Furgoneta no esta cargada"

class VEelectricos(Vehiculos):
	def __init__(self, marca_bici, modelo_bici):
		super().__init__(marca_bici, modelo_bici)
		self.autonomia=100

	def cargarenergia(self):
		self.cargado=True 

	def estado(self):
		super().estado()
		print("Autonomia de la bateria: ", self.autonomia)



class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="\nvoy haciendo el caballito"
	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ",self.modelo, "\nEn Marcha: ",self.enmarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, self.hcaballito)

class Bicicletaelectrica(VEelectricos):
	pass



#mimoto=Moto("Honda", "CBR")
#mimoto.caballito()
#mimoto.estado()
#print("----------------------------------")
#mifurgoneta=Furgoneta("Renault", "Kangoo")
#mifurgoneta.arrancar()
#mifurgoneta.estado()
#print(mifurgoneta.carga(True))
#print("----------------------------------")
#mibici=Bicicletaelectrica("Orbea", "HC1030")
#mibici.estado()