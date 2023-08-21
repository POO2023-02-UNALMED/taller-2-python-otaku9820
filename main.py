class Asiento:
    def __init__(self, color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
        
    def cambiarColor(self,color):
        if color== "rojo"or color=='verde'or color=='amarillo' or color=='blanco'or color=='negro':
            self.color=color
        
        
class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantidadCreados=cantidadCreados
        

    def cantidadAsientos(self):
        asientos1=len(self.asientos)
        return asientos1 
    
    
    def verificarIntegridad(self):
        if self.registro==self.motor.registro and self.registro==cantidadAsientos():
            return "Auto original"
        else:
            return 'las piezas no son originales'
    
    
    
class Motor :
    def __init__(self, numeroCilindros, tipo, registro ):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
            
    def cambiarRegistro(self, numRegistro):
        self.registro = numRegistro
            
    def asignarTipo(self, tipo):
        if tipo=='gasolina'or tipo=='electrico':
            self.tipo=tipo