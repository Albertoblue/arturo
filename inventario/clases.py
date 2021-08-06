frutas=["Sandia","Melón","Manzana"] #listas
frutas={} #objetos

for fruta in frutas:
    print(fruta)

class Alumno:
    def __init__(self,matricula,promedio,edad,nombre):
        self.matricula=matricula
        self.promedio=promedio
        self.edad=edad
        self.nombre=nombre

    def estudiar(self):
        return "El alumno esta estudiando"

    def __str__(self):
        return "Soy %s tengo promedio %.2f y mi matricula es: %i"%(self.nombre,self.promedio,self.edad)

alumnos=[]



alumnos.append(Alumno(253126,9.0,25,"Oscar"))
alumnos.append(Alumno(122354,8.5,18,"Lau"))


for alumno in alumnos:
    print(alumno)