from tkinter import Tk, Text, Button, END, re

'''
Tk inicializa la libreria tkinter
Text habilita el uso de textos, recuadros, etc.
Button habilita los botones

END permite acceder al final del 'Text'
re expresion regular para la busqueda de patrones
'''

class Interfaz:
    def __init__(self, ventana) -> None:
        self.ventana = ventana

        # TITULO DE LA VENTANA
        self.ventana.title("Calculadora")


        # AGREGAR UNA CAJA DE TEXTO  | CONTENIDO DE LAS OPERACIONES
        self.pantalla = Text(ventana, state='disabled', width=40, height=3, background='royal blue',
                                foreground='white', font=('Helvetica', 15))

        ''' 
        ¬ El estado es 'disabled' para que el usuario no pueda ingresar datos con el teclado
        ¬ width y height otorga tamaño
        ¬ BG fondo, FG color a la letra
        '''

        # UBICAR PANTALLA EN LA VENTANA CON GRID QUE ES UN GESTOR DE GEOMETRIA
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        '''
        ¬ grid permite ubicar elementor con la libreria tkinter
        ¬ row - fila, column - columna (ambas en la posicion 0)
        ¬ columnspan indica las columnas que va abarcar, ya que r y c valen 0, ira de 0 <= 4

        ¬ pad genera espacio del recuadro
        '''

        # OPERACIONES
        self.operacion = ""

        # BOTONES
        boton1, boton2, boton3  = self.CrearBoton(7), self.CrearBoton(8), self.CrearBoton(9)

        boton4 = self.CrearBoton(u"\u232B", escribir=False) # FECLA DE BORRADO

        boton5, boton6, boton7 = self.CrearBoton(4), self.CrearBoton(5), self.CrearBoton(6)
     
        boton8 = self.CrearBoton(u"\u00F7") # DIVISION

        boton9, boton10, boton11  = self.CrearBoton(1), self.CrearBoton(2), self.CrearBoton(3)

        boton12, boton13 = self.CrearBoton("*"), self.CrearBoton(".")
    
        boton14, boton15, boton16 = self.CrearBoton(0), self.CrearBoton("+"), self.CrearBoton("-")
        
        boton17 = self.CrearBoton("=", escribir=False, ancho=20, alto=2)

        # UBICAR BOTONES
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10,
                    boton11, boton12, boton13, boton14, boton15, boton16, boton17]

        contador = 0

        '''
        se crea una lista para almacenar todos los botones que se van a imprimir, y posteriormente
        se establece un contador el cual buscara en la posicion de la lista a cada elemento dentro de
        ella.

        posteriormente se crea un for para incrementar y ordenar los botones
        '''
        for fila in range(1, 5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1
        # UBICAR EL ULTIMO BOTON AL FINAL
        botones[16].grid(row=5, column=0, columnspan=4)

        return

    def CrearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 15), 
                        command=lambda: self.click(valor, escribir))

    # CONTROLAR EVENTO DE LOS BOTONES
    def click(self, texto, escribir):

        '''
        Si el parametro 'escribir' es True, se mostrara en pantalla
        '''
        if not escribir:
            '''
            solo evaluar si el usuario a dado '='
            '''
            if texto == "=" and self.operacion != "":
                self.operacion = re.sub(u"\u00F7", "/", self.operacion)
                resultado = str(eval(self.operacion))
                self.operacion = ""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            
            #si se presiono el boton de borrado borrar la pantalla
            elif texto == u"\u232B":
                self.operacion = ""
                self.limpiarPantalla()

        # MOSTRAR TEXTO
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(texto)
        return

    # BORRAR EL CONTENIDO DE LA PANTALLA
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", END)
        self.pantalla.configure(state="disabled")

        return

    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END, valor)
        self.pantalla.configure(state="disabled")


Ventana_Principal = Tk()

calculadora = Interfaz(Ventana_Principal)

Ventana_Principal.mainloop()