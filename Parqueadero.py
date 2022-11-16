from abc import ABC, abstractmethod

''' Clase abstracta'''
class Parqueadero(ABC):
    @abstractmethod
    def __init__(self, plazaC:int, plazaSUV:int, plazaVan:int, tipoCars:str):
        self.plazaC = plazaC
        self.plazaSUV = plazaSUV
        self.plazaVan = plazaVan
        self.tipoCars = tipoCars
        
    '''Metodos sin funcionalidad'''
    
    @abstractmethod
    def horario(self):
        pass
    @abstractmethod
    def plazas(self):
        pass
    @abstractmethod
    def cobrohoras(self):
        pass
    

    
    
   


   

        
    
        
        
         