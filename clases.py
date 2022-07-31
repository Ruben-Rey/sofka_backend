class Nave():

    def __init__(self, nom, sit, lan, pes, emp, comb, obj, pai):
        self.nombre = nom
        self.situacion = sit
        self.lanzamiento = lan
        self.peso = pes
        self.empuje = emp
        self.combustible = comb
        self.objetivo = obj
        self.pais = pai

    def __str__(self):
        return f'''Nombre : {self.nombre},
            Situacion : {self.situacion},
            Lanzamiento : {self.lanzamiento} Km/h,
            Peso :{self.peso},
            empuje :{self.empuje},
            empuje :{self.combustible}
            '''
    def encender(self):
        pass

    def apagar(self):
        pass


class Lanzadera(Nave):

    def __init__(self, nom, sit, lan, pes, emp, comb, fase, reu):
        super().__init__(nom, sit, lan, pes, emp, comb)
        self.fase = fase
        self.reutilizable = reu

    def desaclopar_motor(self):
        pass


class Tripulada(Nave):

    def __init__(self, nom, sit, lan, pes, emp, comb, cap):
        super().__init__(nom, sit, lan, pes, emp, comb)
        self.capacidad = cap


class NoTripulada(Nave):

    def __init__(self, nom, sit, lan, pes, emp, comb, reu, obj, pai):
        super().__init__(nom, sit, lan, pes, emp, comb, obj, pai)
        self.reutilizable = reu
    
    def __str__(self):
        return f'''Nombre :{self.nombre},
            Situacion :{self.situacion},
            Lanzamiento :{self.lanzamiento} Km/h,
            Peso :{self.peso},
            Empuje :{self.empuje},
            Combustible :{self.combustible},
            Reutilizable :{self.reutilizable},
            Objetivo :{self.objetivo},
            Pais :{self.pais}
            '''
 # Reutilizable :{self.reu},
            # Objetivo :{self.objetivo},
            # Pais :{self.pais}


# x = Nave("Lucas","retirado",111,222,22,"helio")
# print(x)

soyus = NoTripulada("Soyus","activo",111,222,22,"helio",True,"Exploracion","Peru")
print(soyus)



