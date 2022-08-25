class persona:
	# Constructor
	def __init__(self, nombre, apellido, correo):
		# Instance attributes
		self.nombre = nombre
		self.apellido = apellido
		self.correo = correo

	# el objeto esta pasandose a si mismo como un parametro
	def hablar(self):
		print(f'hola! mi nombre es {self.nombre}, y mi apellido es {self.apellido} aqui dejo mi correp: {self.correo}')

nueva_persona = persona('pablo', 'pimentel', 'tatu_pm')
nueva_persona.hablar()




    