class Organizador:
    def __init__(self, plan, config):
        self.cursada = Cursada(self.cargarPlan(plan), self.cargarConfig(config))

    def cargarPlan(self, plan):
        #TODO

    def cargarConfig(self, config):
        #TODO

    def aprobarMateria(self, codigo, nota):
        #TODO

    def aplazarMateria(self, codigo):
        #TODO

    def consultarCursables(self):
        return self.cursada.consultarCursables()

    def consultarPromedio(self):
        return self.cursada.consultarPromedio()

    def consultarCreditos(self):
        return self.cursada.consultarCreditos()

    def consultarEstadoCarrera(self):
        #TODO