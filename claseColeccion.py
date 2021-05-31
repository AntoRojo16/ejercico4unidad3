from claseEmpleado import Empleado
from ClasePlanta import Planta
from ClaseContratados import Contratados
from ClaseExternos import Externos

from datetime import date
import numpy as np
import csv
import os
import time

class Coleccion:
    __colec=None
    __cantidad=0

    def __init__(self, tam):
        self.__colec=np.empty(tam,dtype=Empleado)
        self.__cantidad=0
    def CargarEmpleados(self):
        try:
            archi=open('Planta.csv')
            reader = csv.reader(archi,delimiter=';')

            for fila in reader:
                if(fila[0]!="DNI"):
                    EPlanta=Planta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
                    self.__colec[self.__cantidad]=EPlanta
                    self.__cantidad+=1
            archi.close()
            
            archi=open('Contratados.csv')
            reader = csv.reader(archi,delimiter=';')

            for fila in reader:
                if(fila[0]!="DNI"):
                    EContrat=Contratados(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                    self.__colec[self.__cantidad]=EContrat
                    self.__cantidad+=1
            archi.close()
            
            archi=open('Externos.csv')
            reader = csv.reader(archi,delimiter=';')

            for fila in reader:
                if(fila[0]!="DNI"):
                    EExternos=Externos(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
                    self.__colec[self.__cantidad]=EExternos
                    self.__cantidad+=1
            archi.close()
        except IndexError:
            print("***1q ERROR ***.\n El numero ingresado debe ser igual o mayor al numero de empleados")
            time.sleep(1.8)
            return -1

    def BuscarDNI(self,dni):
        i=0
        ban=False    
        while((ban==False) and (i<len(self.__colec))):
            if((self.__colec[i]!=None) and (self.__colec[i].getDNI()==dni)):
                if(isinstance(self.__colec[i],Contratados)==True):
                    ban=True
                else:
                    i+=1
            else:
                    i+=1
        if(ban==True):
            return self.__colec[i]
        elif(ban==False):
            return -1
        else:
            return 0
    
    def BuscarTarea(self,tarea):
        hoy=date.today()
        i=0
        ban=False
        while((ban==False) and (i<len(self.__colec))):
            if(isinstance(self.__colec[i],Externos)==True):
                if(self.__colec[i].getTarea().lower() == tarea):
                    ban=True
                else:
                    i+=1
            else:
                i+=1
        if(ban==True):
            fin = self.__colec[i].getFinTarea()
            fin=fin.split("/",3)
            if(int(fin[0]) >= int(hoy.year)):
                if(int(fin[1]) >= int(hoy.month)):
                    if(int(fin[2]) >= int(hoy.day)):
                        ban=True
                        os.system('cls')
                        print("Tarea: {}" .format(tarea))
                        print("Empleado: {}".format(self.__colec[i].getNom()))
                        print("--- MONTO TOTAL DE LA TAREA: ${} ---".format(self.__colec[i].getMonto()))
                        input("")
                    else:
                        print("El lapso de realizacion ya finalizó")
                        input("")
                else:
                    print("El lapso de realizacion ya finalizó")
                    input("")
            else:
                print("El lapso de realizacion ya finalizó")
                input("")
        else:
            print("Tarea no encontrada.")
            input("")


    def AyudaSolid(self):
        os.system('cls')
        i=0
        cont=0
        print("***** LISTADO DE EMPLEADOS QUE NECECITAN AYUDA *****")
        for i in range(len(self.__colec)):
            if(self.__colec[i].Sueldo() < 25000):
                print("Empleado {}" .format(i+1))
                self.__colec[i].MuestraDatos()
                print('\n')
                cont+=1

        input("PRESIONE ENTER PARA CONTINUAR")
        if(cont==0):
            print("No hay empleados que nececiten de ayuda")
            #input("**** Presione ENTER para continuar ****")

    def MuestraSueldos(self):
        i=0
        print(" LISTADO DE SUELDOS ")
        for i in range(len(self.__colec)):
            if(self.__colec[i]!=None):
                print("\n")
                print("Empleado N° {}" .format(i+1))
                nom=self.__colec[i].getNom()
                tel=self.__colec[i].getTel()
                sueldo=self.__colec[i].Sueldo()
                print("Nombre: {}" .format(nom))
                print("Telefono: {}" .format(tel))
                print("Sueldo: {}" .format(sueldo))
        input()
    