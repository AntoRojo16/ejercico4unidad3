class Empleado:
    __dni=0
    __nombre=""
    __direccion=""
    __telefono=""
    
    
    def __init__ (self,dni,nombre,direccion,telefono):
        self.__dni=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        
        
    def getDni (self):
        return self._dni
    
    def getNonbre (self):
        return self.__nombre
    
    
    def getDireccion (self):
        return self.__direccion
    
    def MuestraDatos(self):
        print("Nombre: {}".format(self.__nombre))
        print("DNI: {}".format(self.__dni))
        print("Dirección: {}".format(self.__direccion))
    
    
    def getTelefono (self):
        return self.__telefono
    
    
    
    
    
    
    
    

    

