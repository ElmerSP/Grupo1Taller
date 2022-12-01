from Colores import Colores

class Menu:
  def __init__(self):
    self.colores=Colores()
  def menuPrincipal(self):
    print(self.colores.celeste,'''
    ================================
       ---->>>> MENU <<<<----
     [1] Insertar  [3] Actualizar
     [2] Ver       [4] Eliminar
            [0] salir
    ================================
    ''',self.colores.RESET)
    
  def menuCrear(self):
    print(self.colores.verde,'''
    ================================
      ---->>>> REGISTRAR <<<<----
      [1] Persona  [3] Grupo
      [2] Reunion  [0] Atras
    ================================
    ''',self.colores.RESET)
        
  def menuRead(self):
    print(self.colores.azul,'''
    ================================
        ---->>>> BUSCAR <<<<----
      [1] Por Fecha     
      [2] Por Asistente 
      [3] Por Tema
      [4] Listar Personas
      [5] Listar Agenda
      [0] Atras
    ================================
    ''',self.colores.RESET)
      
  def menuUpdate(self):
    print(self.colores.amarillo,'''
    ================================
        ---->>>> EDITAR <<<<----
      [1] Nombre de Persona 
      [2] CI de Persona
      [3] Tema de reunion
      [4] Lugar de ruinion
      [5] Fecha de reunion
      [6] Hora de reunion
      [0] Atras
    ================================
    ''',self.colores.RESET)
    
  def menuDelete(self):
    print(self.colores.rojo,'''
    ================================
       ---->>>> ELIMINAR <<<<----
      [1] Grupo    [3] Reunion   
      [2] Persona  [0] Atras
    ================================
    ''',self.colores.RESET)