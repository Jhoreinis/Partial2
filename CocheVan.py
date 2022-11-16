from Parqueadero import Parqueadero


'''Esta subclase es utilizada unicamente para autos vann'''

class CocheVan (Parqueadero):
    def __init__(self, plazaC: int, plazaSUV: int, plazaVan: int, tipoCars: str, cochesVan: int, cobroVan: int):
        super().__init__(plazaC, plazaSUV, plazaVan, tipoCars)
        
        self.cochesVan = cochesVan
        self.cobroVan = cobroVan
      
    
    '''Este metodo indica el horario habil del parqueadero'''
     
    def horario(self):
        "El parqueadero no tiene hora de cierre"
        print("Se aceptan coches durante 24 horas")
     
        
    '''Este metodo indica las plazas disponibles'''

    def plazas(self):
        "Suponiendo que los usuarios estan registrados"
        C = "van"
        if self.tipoCars == C:
            self.plazaVan = self.plazaVan - self.cochesVan
            print("PLAZAS DISPONIBLES AUTOS VAN")
            print(self.plazaVan)
        else:
            print("Tipo de carro incorrecto")
 
 
    '''Este metodo le indica al usuario cuanto debe pagar'''

        
    def cobrohoras(self):
      
        horas= int(input("¿Cuantas horas duro su auto parqueado?\t"))
        print("2000 por hora para coches compactos")
        self.cobroVan  = self.cobroVan  * horas
        print("Tiene que pagar")
        print(self.cobroVan)
    