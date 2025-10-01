class Coche:
    def init (self,m):
        self.marca = m
        self.color = 'sin definir'
        self.rendimiento = 0.0
        self.gasolina = 0.0
        self.articulos = []
    def Guarda(self,t):
        self.articulos.append(t)
        print('Se guardo el articulo', t, 'en el', self.marca)
    def MuestraArticulos(self):
        if len(self.articulos)==0:
            print('no hay ningun articulo aun.')
        else:
            print('En la cajuela del', self.marca, 'hay:')
            for k in self.articulos:
                print(' - ', k)
    def Distancia(self):
        d = self.gasolina * self.rendimiento
        return d
