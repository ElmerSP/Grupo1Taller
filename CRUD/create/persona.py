class Persona:
    def __init__(self,idPersona,nombre,apellido,ci):
        self._idPersona=idPersona
        self._nombre=nombre
        self._apellido=apellido
        self._ci=ci
        
    def get_idPersona(self):
        return self._idPersona
    def get_nombre(self):
        return self._nombre
    def get_apellido(self):
        return self._apellido
    def get_ci(self):
        return self._ci
    
    def set_idPersona(self,idPersona):
        self._idPersona=idPersona
    def set_nombre(self,nombre):
        self._nombre=nombre
    def set_apellido(self,apellido):
        self._apellido=apellido
    def set_ci(self,ci):
        self._ci=ci