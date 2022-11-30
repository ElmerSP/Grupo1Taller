class Agenda:
    def __init__(self,idReunion,temaReunion,lugar,fecha,hora):
        self._idReunion=idReunion
        self._temaReunion=temaReunion
        self._lugar=lugar
        self._fecha=fecha
        self._hora=hora
        
    def get_idReunion(self):
        return self._idReunion
    def get_temaReunion(self):
        return self._temaReunion
    def get_lugar(self):
        return self._lugar
    def get_fecha(self):
        return self._fecha
    def get_hora(self):
        return self._hora
    
    def set_idReunion(self,idAgenda):
        self._idAgenda=idAgenda
    def set_idPersona(self,idPersona):
        self._idPersona=idPersona
    def set_temaReunion(self,temaReunion):
        self._temaReunion=temaReunion
    def set_lugar(self,lugar):
        self._lugar=lugar
    def set_fecha(self,fecha):
        self._fecha=fecha
    def set_hora(self,hora):
        self._hora=hora