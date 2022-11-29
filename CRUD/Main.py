from Menu import Menu

class Main:
    def __init__(self):
        self.menu = Menu()
        
    def Inicio(self):
        opcion =-1
        while opcion!=0:
            self.menu.menuPrincipal()
            try:              
                opcion=int(input(">> "))
            except:
                self.menu.Valor()
                input('ingrese un numero')
            if opcion == 1:
                pass
            if opcion == 2:
                pass
            if opcion == 3:
                pass
            if opcion == 4:
                pass
            elif opcion == 0:
                print('gracias...')