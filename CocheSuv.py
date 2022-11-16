from Parqueadero import Parqueadero
'''Esta subclase es utilizada unicamente para autos vann'''
class CocheSuv (Parqueadero):
    
    def __init__(self, plazaC: int, plazaSUV: int, plazaVan: int, tipoCars: str, cochesSuv:int, cobroSuv:int):
        super().__init__(plazaC, plazaSUV, plazaVan, tipoCars)
        
        self.cochesSuv = cochesSuv
        self.cobroSuv = cobroSuv
        
        
    '''Este metodo indica el horario habil del parqueadero'''
  
    def horario(self):
        "El parqueadero no tiene hora de cierre"
        print("Se aceptan coches durante 24 horas")
    
       
        
    '''Este metodo indica las plazas disponibles'''

    def plazas(self):
        "Suponiendo que los usuarios estan registrados"
        C = "suv"

        if self.tipoCars == C:
            self.plazaSUV = self.plazaSUV - self.cochesSuv
            print("PLAZAS DISPONIBLES AUTOS SUV")
            print(self.plazaSUV)
        else:
            print("Tipo de carro incorrecto")
                
    '''Este metodo le indica al usuario cuanto debe pagar'''
 
    def cobrohoras(self):
    
        horas= int(input("¿Cuantas horas duro su auto parqueado?\t"))
        print("3000 por hora para coches compactos")
        self.cobroSuv  = self.cobroSuv  * horas
        print("Tiene que pagar")
        print(self.cobroSuv)
        
