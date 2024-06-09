import random
import tkinter as tk
import math 

from tkinter import ttk
        

def pestaña(self, root):
    self.root = root
    self.root.title("Sistema de gestion de filas")
    self.notebook = ttk.Notebook(root)
    self.notebook.pack(fill=tk.BOTH, expand=True)

    self.tab1 = ttk.Frame(self.notebook)
    self.notebook.add(self.tab1, text="Polideportivo Colón")
    
    self.label_TS = ttk.Label(self.tab1, text="Ingrese tiempo de simulacion")
    self.label_TS.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_TS = ttk.Entry(self.tab1)
    self.entry_TS.grid(row=1, column=1, padx=10, pady=5)


    self.label_L = ttk.Label(self.tab1, text="Ingrese tiempo de limpieza")
    self.label_L.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_L = ttk.Entry(self.tab1)
    self.entry_L.grid(row=2, column=1, padx=10, pady=5)

    #Ingreso Datos futbol
    
    self.label_F = ttk.Label(self.tab1, text="Futbol")
    self.label_F.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    self.label_FL = ttk.Label(self.tab1, text="\t Ingrese media de llegada con dist. Exp negativa")
    self.label_FL.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FL = ttk.Entry(self.tab1)
    self.entry_FL.grid(row=4, column=1, padx=10, pady=5)
    
    self.label_FOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_FOI.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FOI = ttk.Entry(self.tab1)
    self.entry_FOI.grid(row=5, column=1, padx=10, pady=5)
    
    self.label_FOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_FOS.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FOS = ttk.Entry(self.tab1)
    self.entry_FOS.grid(row=6, column=1, padx=10, pady=5)

    #Ingreso Datos Handball
    
    self.label_H = ttk.Label(self.tab1, text="Handball")
    self.label_H.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    
    self.label_HLI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de la llegada a la cancha con Dist. uniforme")
    self.label_HLI.grid(row=8, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_HLI = ttk.Entry(self.tab1)
    self.entry_HLI.grid(row=8, column=1, padx=10, pady=5)
    
    self.label_HLS = ttk.Label(self.tab1, text="\t Ingrese limite superior de la llegada a la cancha con Dist. uniforme")
    self.label_HLS.grid(row=9, column=0, padx=10, pady=5, sticky="w")

    self.entry_HLS = ttk.Entry(self.tab1)
    self.entry_HLS.grid(row=9, column=1, padx=10, pady=5)

    self.label_HOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_HOI.grid(row=10, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_HOI = ttk.Entry(self.tab1)
    self.entry_HOI.grid(row=10, column=1, padx=10, pady=5)
    
    self.label_HOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_HOS.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        
    self.entry_HOS = ttk.Entry(self.tab1)
    self.entry_HOS.grid(row=11, column=1, padx=10, pady=5)
    
    #Ingreso Datos Basketball
    
    self.label_B = ttk.Label(self.tab1, text="Basketball")
    self.label_B.grid(row=12, column=0, padx=10, pady=5, sticky="w")
    
    self.label_BLI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de la llegada a la cancha con Dist. uniforme")
    self.label_BLI.grid(row=13, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_BLI = ttk.Entry(self.tab1)
    self.entry_BLI.grid(row=13, column=1, padx=10, pady=5)
    
    self.label_BLS = ttk.Label(self.tab1, text="\t Ingrese limite superior de la llegada a la cancha con Dist. uniforme")
    self.label_BLS.grid(row=14, column=0, padx=10, pady=5, sticky="w")

    self.entry_BLS = ttk.Entry(self.tab1)
    self.entry_BLS.grid(row=14, column=1, padx=10, pady=5)


    self.label_BOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_BOI.grid(row=15, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_BOI = ttk.Entry(self.tab1)
    self.entry_BOI.grid(row=15, column=1, padx=10, pady=5)
    
    self.label_BOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_BOS.grid(row=16, column=0, padx=10, pady=5, sticky="w")
        
    self.entry_BOS = ttk.Entry(self.tab1)
    self.entry_BOS.grid(row=16, column=1, padx=10, pady=5)
    

    self.button_generate = ttk.Button(
        self.tab1, text="Generar", command=self.generador)
    self.button_generate.grid(
        row=17, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab1, width=400, height=600)
    self.canvas.grid(row=18, column=0, columnspan=2, padx=10, pady=10)
    
def exp_negativa(RND, media):
    return (-media * math.log(1 - RND))*60

def uniforme(inf, sup, RND):
    amp = sup - inf
    return (inf + (amp * RND)) *60

def inicializar_vector(tiempo_simulacion):
    vector_estado = ["Inicializacion", tiempo_simulacion, 0, 0, 0, 0, 0, 0, 'Libre', '-', 0, '-', '-', '-', '-', '-', '-']
    vector_estado[2] = random.random()
    vector_estado[3] = exp_negativa(vector_estado[3], 10) 

    vector_estado[4] = random.random()
    vector_estado[5] = uniforme(10, 14, vector_estado[5]) 

    vector_estado[6] = random.random()
    vector_estado[7] = uniforme(6, 10, vector_estado[7]) 

    return vector_estado

def generacion_linea(vector_anterior):
    vector_posterior = vector_anterior
    if vector_anterior[1] == 0:
        valores = [vector_anterior[3], vector_anterior[5], vector_anterior[7]]
    else:
        valores = [vector_anterior[3], vector_anterior[5], vector_anterior[7], vector_anterior[14]]


    minimo_valor = min(valores)
    indice_minimo = valores.index(minimo_valor)
    
    
    if indice_minimo == 0:
        vector_posterior[0] = 'Llegada futbol'
        vector_posterior[1] = vector_anterior[7]
        vector_posterior[2] = random.random()
        vector_posterior[3] = exp_negativa(vector_anterior[3], 10) 
        
        if vector_anterior[8] == 'Ocupado' or vector_anterior[8] == 'En limpieza':
            vector_posterior[10] += 1
        else:
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = 'Futbol'
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(70, 130, vector_posterior[11])
            if vector_anterior[10] > 0:
                vector_posterior[10] = vector_anterior[10] - 1

    elif indice_minimo == 1:
        vector_posterior[0] = 'Llegada handball'
        vector_posterior[1] = vector_anterior[7]
        vector_posterior[4] = random.random()
        vector_posterior[5] = uniforme(10, 14, vector_posterior[6])
        
        if vector_anterior[8] == 'Ocupado' or vector_anterior[8] == 'En limpieza':
            vector_posterior[10] += 1
        else:
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = 'Handball'
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(70, 130, vector_posterior[11])
            if vector_anterior[10] > 0:
                vector_posterior[10] = vector_anterior[10] - 1

    elif indice_minimo == 2:
        vector_posterior[0] = 'Llegada basket'
        vector_posterior[1] = vector_anterior[7]
        vector_posterior[6] = random.random()
        vector_posterior[7] = uniforme(6, 10, vector_posterior[6])
        
        if vector_anterior[8] == 'Ocupado' or vector_anterior[8] == 'En limpieza':
            vector_posterior[10] += 1
        else:
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = 'Basket'
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(60, 100, vector_posterior[11])
            if vector_anterior[10] > 0:
                vector_posterior[10] = vector_anterior[10] - 1
    elif indice_minimo == 3 and vector_anterior[0] == 'Llegada basket' or vector_anterior[0] == 'Llegada futbol' or vector_anterior[0] == 'Llegada handball':
        vector_posterior[0] = 'Inicio de limpieza'
        vector_posterior[1] = vector_anterior[14]
        vector_posterior[8] = 'En limpieza'
        vector_posterior[12] = 10
        vector_posterior[13] = vector_posterior[1] + vector_posterior[12]
    elif indice_minimo == 3 and vector_anterior[0] == "Inicio de limpieza":
        vector_posterior [0] = 'Fin de limpieza'
        vector_posterior [1]  = vector_anterior[14]
        vector_posterior[8] = 'Libre'

    return vector_posterior




class GestionFila:
    def __init__(self, root):
        # PESTAÑA 1
        pestaña(self, root)
    def llamar(self):
        tiempo_final = float(self.entry_TS.get())
        vector_anterior = inicializar_vector(0)

        while vector_anterior[1] <= tiempo_final:
            vector_anterior = generacion_linea(vector_anterior)

    
# Ejemplo de uso
root = tk.Tk()
app = GestionFila(root)
root.mainloop()