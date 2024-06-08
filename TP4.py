import random
import tkinter as tk

from tkinter import ttk
from tabulate import tabulate



class GestionFila:
    def __init__(self, root):
        # PESTAÑA 1
        pestaña(self, root)
    def generador(self):
        pass
        

def pestaña(self, root):
    self.root = root
    self.root.title("Sistema de gestion de filas")
    self.notebook = ttk.Notebook(root)
    self.notebook.pack(fill=tk.BOTH, expand=True)

    self.tab1 = ttk.Frame(self.notebook)
    self.notebook.add(self.tab1, text="Polideportivo Colón")
    
    self.label_L = ttk.Label(self.tab1, text="Ingrese tiempo de limpieza")
    self.label_L.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_L = ttk.Entry(self.tab1)
    self.entry_L.grid(row=1, column=1, padx=10, pady=5)
    
    self.label_F = ttk.Label(self.tab1, text="Futbol")
    self.label_F.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    
    self.label_FL = ttk.Label(self.tab1, text="\t Ingrese media de llegada con dist. Exp negativa")
    self.label_FL.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FL = ttk.Entry(self.tab1)
    self.entry_FL.grid(row=3, column=1, padx=10, pady=5)
    
    self.label_FOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_FOI.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FOI = ttk.Entry(self.tab1)
    self.entry_FOI.grid(row=4, column=1, padx=10, pady=5)
    
    self.label_FOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_FOS.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FOS = ttk.Entry(self.tab1)
    self.entry_FOS.grid(row=5, column=1, padx=10, pady=5)
    
    self.label_H = ttk.Label(self.tab1, text="Handball")
    self.label_H.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    
    self.label_HLI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de la llegada a la cancha con Dist. uniforme")
    self.label_HLI.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_HLI = ttk.Entry(self.tab1)
    self.entry_HLI.grid(row=7, column=1, padx=10, pady=5)
    
    self.label_HLS = ttk.Label(self.tab1, text="\t Ingrese limite superior de la llegada a la cancha con Dist. uniforme")
    self.label_HLS.grid(row=8, column=0, padx=10, pady=5, sticky="w")

    self.entry_HLS = ttk.Entry(self.tab1)
    self.entry_HLS.grid(row=8, column=1, padx=10, pady=5)


    self.label_HOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_HOI.grid(row=9, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_HOI = ttk.Entry(self.tab1)
    self.entry_HOI.grid(row=9, column=1, padx=10, pady=5)
    
    self.label_HOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_HOS.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        
    self.entry_HOS = ttk.Entry(self.tab1)
    self.entry_HOS.grid(row=10, column=1, padx=10, pady=5)
    
    
    self.label_B = ttk.Label(self.tab1, text="Handball")
    self.label_B.grid(row=11, column=0, padx=10, pady=5, sticky="w")
    
    self.label_BLI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de la llegada a la cancha con Dist. uniforme")
    self.label_BLI.grid(row=12, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_BLI = ttk.Entry(self.tab1)
    self.entry_BLI.grid(row=12, column=1, padx=10, pady=5)
    
    self.label_BLS = ttk.Label(self.tab1, text="\t Ingrese limite superior de la llegada a la cancha con Dist. uniforme")
    self.label_BLS.grid(row=13, column=0, padx=10, pady=5, sticky="w")

    self.entry_BLS = ttk.Entry(self.tab1)
    self.entry_BLS.grid(row=13, column=1, padx=10, pady=5)


    self.label_BOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_BOI.grid(row=14, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_BOI = ttk.Entry(self.tab1)
    self.entry_BOI.grid(row=14, column=1, padx=10, pady=5)
    
    self.label_BOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_BOS.grid(row=15, column=0, padx=10, pady=5, sticky="w")
        
    self.entry_BOS = ttk.Entry(self.tab1)
    self.entry_BOS.grid(row=15, column=1, padx=10, pady=5)
    

    self.button_generate = ttk.Button(
        self.tab1, text="Generar", command=self.generador)
    self.button_generate.grid(
        row=16, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab1, width=400, height=600)
    self.canvas.grid(row=18, column=0, columnspan=2, padx=10, pady=10)
    

def generacion_vector(param):
    primer_vector = [0] * 11
    acu = 0
    acu_precio = 0
 
  
    for i in range(param):
        primer_vector[3] = 0
        primer_vector[4] = 0
        primer_vector[5] = 0
        primer_vector[6] = 0
        primer_vector[7] = 0
        primer_vector[8] = 0
        primer_vector[0] = i + 1
        primer_vector[1] = random.random()
        if primer_vector[1] > 0.29:
            primer_vector[2] = "Sí abrio"
            primer_vector[3] = random.random()
            if primer_vector[3] < 0.20:
                # abre señor
                primer_vector[4] = "Señor"
                primer_vector[5] = random.random()
                if primer_vector[5] < 0.25:
                    primer_vector[6] = "Si vende"
                    primer_vector[7] = random.random()
                    if primer_vector[7] < 0.10:
                        # vende 1 
                        primer_vector[8] = 1
                
                        
                    elif primer_vector[7] < 0.50:
                        # vende 2 
                        primer_vector[8] = 2
                  
                    elif primer_vector[7] < 0.80:
                        # vende 3 
                        primer_vector[8] = 3
                   
                    else:
                        # vende 4
                        primer_vector[8] = 4
                  
                        
                else:
                    # no vende
                    primer_vector[6] = "No vende"
                   
                    
            else:
                primer_vector[4] = "Señora"
                primer_vector[5] = random.random()
                if primer_vector[5] < 0.15:
                    primer_vector[6] = "Si vende"
                    primer_vector[7] = random.random()
                    if primer_vector[7] < 0.60:
                        # vende 1 
                        primer_vector[8] = 1
                     
                    elif primer_vector[7] < 0.90:
                        # vende 2 
                        primer_vector[8] = 2
    
                    else:
                        # vende 3 
                        primer_vector[8] = 3
                        
                
                else:
                    # no vende
                     # no vende
                    primer_vector[6] = "No vende"
                    
                    
        else:
             primer_vector[2] = "No abrio"
         
        acu += primer_vector[8]
        acu_precio = acu * 200     
        primer_vector[9] += acu
        primer_vector[10]+= acu_precio
    return primer_vector   
    

root = tk.Tk()
app = GestionFila(root)
root.mainloop()
