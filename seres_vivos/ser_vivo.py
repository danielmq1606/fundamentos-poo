class SerVivo:
    def __init__(self, name, specie,age,habitat):
        self.name = name
        self.specie = specie
        self.age = age
        self.habitat = habitat 
        self.alive = True

    def eat(self,food):
        if self.alive:
            return f"{self.name} está comiendo {food}."
        else:
            return f"{self.name} No puede comer porque no está vivo."
        
    def sleep(self, hours):
        if self.alive:
            return f"{self.name} está durmiendo por {hours} horas."
        else:
            return f"{self.name} No puede dormir porque no está vivo."
        
    # Mostrar informacion del ser vivo
    def show_info(self):
        return f"Nombre: {self.name}\nEspecie: {self.specie}\nEdad: {self.age} años\nHábitat: {self.habitat}\nEstado: {'Vivo' if self.alive else 'Muerto'}"