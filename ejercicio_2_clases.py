from mailbox import NoSuchMailboxError


class Alumno:
    
    def inicializar(self, nombre, nota) -> None:
        self.nombre = nombre 
        self.nota = nota 

    def imprimir (self):
        print("El nombre del alumno es ", self.nombre)
        print("la nota del alumno es ", self.nota)
    
    def resultado (self):
        if self.nota < 60:
            print("usted perdio por obtener una nota de ", self.nota)
        else:
            print("usted gano por obtener una nota mayor a 60 siendo de ", self.nota)

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("pedro", 80)
alumno2.inicializar("Samuelito", 55)

alumno1.imprimir()
alumno1.resultado()