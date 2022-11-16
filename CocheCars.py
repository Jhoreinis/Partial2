from Parqueadero import Parqueadero

'''Esta subclase es utilizada unicamente para autos compuestos'''

class CocheCars (Parqueadero):
    
    def __init__(self, plazaC: int, plazaSUV: int, plazaVan: int, tipoCars: str,cochescompactos: int, cobrocompactos: int):
        super().__init__(plazaC, plazaSUV, plazaVan, tipoCars)
        
        self.cochescompactos = cochescompactos
        self.cobrocompactos = cobrocompactos
        
        
    '''Este metodo indica el horario habil del parqueadero'''
   
    def horario(self):
        
        "El parqueadero no tiene hora de cierre"
        print("Se aceptan coches durante 24 horas")
        
  
    '''Este metodo indica las plazas disponibles'''
    
    def plazas(self):
        "Suponiendo que los usuarios estan registrados"
        C = "compacto"
        if self.tipoCars == C:
            self.plazaC = self.plazaC - self.cochescompactos
            print("PLAZAS DISPONIBLES AUTOS COMPUESTOS")
            print(self.plazaC)
        else:
            print("Tipo de carro incorrecto")
          
    '''Este metodo le indica al usuario cuanto debe pagar'''

    
  
    def cobrohoras(self):
        horas= int(input("¿Cuantas horas duro su auto parqueado?\t"))
        print("1000 por hora para coches compactos")
        print("Tiene que pagar")
        self.cobrocompactos = self.cobrocompactos * horas
        print(self.cobrocompactos)
       