class Carro:
   def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano 

   def exibir(self):  
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        print(f"ano: {self.ano}")
        print("-" * 80)
        
car1 = Carro("Honda", "Civic", 2022)
car2 = Carro("Toyota", "corolla", 2023)

car1.exibir()
car2.exibir()