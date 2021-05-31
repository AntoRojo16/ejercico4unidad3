from ClaseEmpleados import Empleados

class Plata(Empleado):
    __sueldoB=0
    __antiguedad=0
    
    
    def __init__ (self,dni,nombre,direccion,telefono,sueldo,ant):
        self.__sueldoB=sueldo
        self.__antiguedad=ant
        super.__init__(self,dni,nombre,direccion,telefono)
        
        
    def  getNom ( self ):
         return  super (). getNom ()
    
    def  getTel ( self ):
        return  super (). getTel ()

    def  Sueldo ( self ):
        total = float (self.__SueldoB ) *  int (self.__antiguedad )
        return  total
    
    def  MuestraDatos ( self , ban = False ):
        print ( "EMPLEADO DE PLANTA" )
        super (). MuestraDatos () 
        
    
    
