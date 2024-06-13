import random
import tkinter as tk
import math 
from tabulate import tabulate
from tkinter import ttk
import copy

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
    
    self.entry_L.insert(10, "10")

    #Ingreso Datos futbol
    
    self.label_F = ttk.Label(self.tab1, text="Futbol")
    self.label_F.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    
    self.label_FL = ttk.Label(self.tab1, text="\t Ingrese media de llegada con dist. Exp negativa")
    self.label_FL.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FL = ttk.Entry(self.tab1)
    self.entry_FL.grid(row=4, column=1, padx=10, pady=5)
    self.entry_FL.insert(10,"10")
    
    
    self.label_FOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_FOI.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FOI = ttk.Entry(self.tab1)
    self.entry_FOI.grid(row=5, column=1, padx=10, pady=5)
    self.entry_FOI.insert(80, "80")
    
    self.label_FOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_FOS.grid(row=6, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_FOS = ttk.Entry(self.tab1)
    self.entry_FOS.grid(row=6, column=1, padx=10, pady=5)
    self.entry_FOS.insert(100, "100")

    #Ingreso Datos Handball
    
    self.label_H = ttk.Label(self.tab1, text="Handball")
    self.label_H.grid(row=7, column=0, padx=10, pady=5, sticky="w")
    
    self.label_HLI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de la llegada a la cancha con Dist. uniforme")
    self.label_HLI.grid(row=8, column=0, padx=10, pady=5, sticky="w")
    
    
    self.entry_HLI = ttk.Entry(self.tab1)
    self.entry_HLI.grid(row=8, column=1, padx=10, pady=5)
    self.entry_HLI.insert(10,"10")
    
    self.label_HLS = ttk.Label(self.tab1, text="\t Ingrese limite superior de la llegada a la cancha con Dist. uniforme")
    self.label_HLS.grid(row=9, column=0, padx=10, pady=5, sticky="w")

    self.entry_HLS = ttk.Entry(self.tab1)
    self.entry_HLS.grid(row=9, column=1, padx=10, pady=5)
    self.entry_HLS.insert(14,"14")

    self.label_HOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_HOI.grid(row=10, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_HOI = ttk.Entry(self.tab1)
    self.entry_HOI.grid(row=10, column=1, padx=10, pady=5)
    self.entry_HOI.insert(60,"60")
    
    self.label_HOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_HOS.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        
    self.entry_HOS = ttk.Entry(self.tab1)
    self.entry_HOS.grid(row=11, column=1, padx=10, pady=5)
    self.entry_HOS.insert(100, "100")
    
    #Ingreso Datos Basketball
    
    self.label_B = ttk.Label(self.tab1, text="Basketball")
    self.label_B.grid(row=12, column=0, padx=10, pady=5, sticky="w")
    
    self.label_BLI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de la llegada a la cancha con Dist. uniforme")
    self.label_BLI.grid(row=13, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_BLI = ttk.Entry(self.tab1)
    self.entry_BLI.grid(row=13, column=1, padx=10, pady=5)
    self.entry_BLI.insert(6, "6")
    
    self.label_BLS = ttk.Label(self.tab1, text="\t Ingrese limite superior de la llegada a la cancha con Dist. uniforme")
    self.label_BLS.grid(row=14, column=0, padx=10, pady=5, sticky="w")

    self.entry_BLS = ttk.Entry(self.tab1)
    self.entry_BLS.grid(row=14, column=1, padx=10, pady=5)
    self.entry_BLS.insert(10, "10")


    self.label_BOI = ttk.Label(self.tab1, text="\t Ingrese limite inferior de ocupacion cancha con Dist. uniforme")
    self.label_BOI.grid(row=15, column=0, padx=10, pady=5, sticky="w")
    
    self.entry_BOI = ttk.Entry(self.tab1)
    self.entry_BOI.grid(row=15, column=1, padx=10, pady=5)
    self.entry_BOI.insert(70,"70")
    
    self.label_BOS = ttk.Label(self.tab1, text="\t Ingrese limite superior de ocupacion cancha con Dist. uniforme")
    self.label_BOS.grid(row=16, column=0, padx=10, pady=5, sticky="w")
        
    self.entry_BOS = ttk.Entry(self.tab1)
    self.entry_BOS.grid(row=16, column=1, padx=10, pady=5)
    self.entry_BOS.insert(130, "130")

    self.button_generate = ttk.Button(
        self.tab1, text="Generar", command=self.llamar)
    self.button_generate.grid(
        row=17, column=0, columnspan=2, padx=10, pady=10)

    self.canvas = tk.Canvas(self.tab1, width=400, height=600)
    self.canvas.grid(row=18, column=0, columnspan=2, padx=10, pady=10)
    
def exp_negativa(RND, media):
    return (-media * math.log(1 - RND))

def uniforme(inf, sup, RND):
    return (inf + RND*(sup-inf)) 

def inicializar_vector(med_lleg_futbol, inf_lleg_hand, sup_lleg_hand, inf_lleg_bas, sup_lleg_bas):
    vector_estado = ["Inicializacion", 0, 0, 0, 0, 0, 0, 0, 'Libre', '-', 0, 0, 0, '-', 0, 0, 0, 0,[]]
    vector_estado[2] = round(random.random(),4)
    vector_estado[3] = round(exp_negativa(vector_estado[2], med_lleg_futbol) * 60,4)

    vector_estado[4] = round(random.random(),4)
    vector_estado[5] = round(uniforme(inf_lleg_hand, sup_lleg_hand, vector_estado[4]) * 60,4)

    vector_estado[6] = round(random.random(),4)
    vector_estado[7] = round(uniforme(inf_lleg_bas,sup_lleg_bas , vector_estado[6]) * 60,4)

    return vector_estado

def generacion_linea(vector_anterior, t_limpieza, med_lleg_futbol, inf_oc_fut, sup_oc_fut, inf_lleg_hand, sup_lleg_hand, inf_oc_hand, sup_oc_hand, inf_lleg_bas, sup_lleg_bas, inf_oc_bas, sup_oc_bas):
    vector_posterior = vector_anterior
    if vector_posterior[1] == 0 or vector_posterior[13] in ['-', 0]:
        valores = [vector_anterior[3], vector_anterior[5], vector_anterior[7]]
    else:
        valores = [vector_anterior[3], vector_anterior[5], vector_anterior[7], vector_anterior[13]]


    minimo_valor = min(valores)
    indice_minimo = valores.index(minimo_valor)
    
    if indice_minimo in [0,1,2] and 'llegada' in vector_anterior[0].lower():
        if indice_minimo == 0:
            vector_posterior[0] = 'Llegada futbol'
            vector_posterior[1] = vector_anterior[3] 
            vector_posterior[2] = random.random()
            vector_posterior[3] = exp_negativa(vector_posterior[2], med_lleg_futbol) * 60 + vector_anterior[3] 
            vector_posterior[4] = 0
            vector_posterior[6] = 0
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = vector_anterior[9]
            vector_posterior[10] += 1
            vector_posterior[18].append('futbol')
            
        elif indice_minimo == 1:
            vector_posterior[0] = 'Llegada handball'
            vector_posterior[1] = vector_anterior[5] 
            vector_posterior[4] = random.random()
            vector_posterior[5] = uniforme(inf_lleg_hand, sup_lleg_hand, vector_posterior[4]) * 60 + vector_anterior[3] 
            vector_posterior[2] = 0
            vector_posterior[6] = 0
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = vector_anterior[9]
            vector_posterior[10] += 1
            vector_posterior[18].append('handball')

        elif indice_minimo == 2:
            vector_posterior[0] = 'Llegada basket'
            vector_posterior[1] = vector_anterior[7] 
            vector_posterior[6] = random.random()
            vector_posterior[7] = uniforme(inf_lleg_bas, sup_lleg_bas, vector_posterior[6]) * 60 + vector_anterior[3] 
            vector_posterior[2] = 0
            vector_posterior[4] = 0
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = vector_anterior[9]
            vector_posterior[10] += 1
            vector_posterior[18].append('basket')
            
    elif indice_minimo == 0:
        vector_posterior[0] = 'Llegada futbol'
        vector_posterior[1] = vector_anterior[3] 
        vector_posterior[2] = random.random()
        vector_posterior[3] = (exp_negativa(vector_posterior[2], med_lleg_futbol) * 60) + vector_posterior[1]  # cambiar el 10 por lo que ingrese
        vector_posterior[4] = 0
        vector_posterior[6] = 0
        
        if vector_anterior[8] == 'Ocupado' or vector_anterior[8] == 'En limpieza':
            vector_posterior[10] += 1
            vector_posterior[18].append('Futbol')
        else:
            vector_posterior[17] = vector_anterior[17] + (vector_posterior[1] - vector_anterior[1])
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = 'Futbol'
            vector_posterior[11] = random.random()
            vector_posterior[12] = uniforme(inf_oc_fut, sup_oc_fut,vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            if vector_anterior[10] > 0:
                vector_posterior[10] = vector_anterior[10] - 1
                vector_posterior[14] = vector_anterior[14] + (vector_posterior[1] - vector_anterior[1])

    elif indice_minimo == 1:
        vector_posterior[0] = 'Llegada handball'
        vector_posterior[1] = vector_anterior[5] 
        vector_posterior[4] = random.random()
        vector_posterior[5] = (uniforme(inf_lleg_hand, sup_lleg_hand, vector_posterior[4]) * 60) + vector_posterior[1]
        vector_posterior[2] = 0
        vector_posterior[6] = 0
        
        if vector_anterior[8] == 'Ocupado' or vector_anterior[8] == 'En limpieza':
            vector_posterior[10] += 1
            vector_posterior[18].append('Handball')
        else:
            vector_posterior[17] = vector_anterior[17] + (vector_posterior[1] - vector_anterior[1])
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = 'Handball'
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(inf_oc_hand, sup_oc_hand, vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            if vector_anterior[10] > 0:
                vector_posterior[10] = vector_anterior[10] - 1
                vector_posterior[16] = vector_anterior[16] + (vector_posterior[1] - vector_anterior[1])

    elif indice_minimo == 2:
        vector_posterior[0] = 'Llegada basket'
        vector_posterior[1] = vector_anterior[7] 
        vector_posterior[6] = random.random()
        vector_posterior[7] = (uniforme(inf_lleg_bas, sup_lleg_bas, vector_posterior[6]) * 60)+ vector_posterior[1]
        vector_posterior[2] = 0
        vector_posterior[4] = 0
        
        if vector_anterior[8] == 'Ocupado' or vector_anterior[8] == 'En limpieza':
            vector_posterior[10] += 1
            vector_posterior[18].append('Basket')
        else:
            vector_posterior[17] = vector_anterior[17] + (vector_posterior[1] - vector_anterior[1])
            vector_posterior[8] = 'Ocupado'
            vector_posterior[9] = 'Basket'
            vector_posterior[11] = random.random()
            vector_posterior[12] = uniforme(inf_oc_bas, sup_oc_bas, vector_posterior[11])
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            if vector_anterior[10] > 0:
                vector_posterior[10] = vector_anterior[10] - 1
                vector_posterior[15] = vector_anterior[15] + (vector_posterior[1] - vector_anterior[1])
    elif indice_minimo == 3 and  'Fin de limpieza' in vector_anterior[0] and 'Ocupado' in vector_anterior[8] and vector_posterior[10] == 0:
        vector_posterior[11] = 0
        vector_posterior[0] = 'Inicio de limpieza'
        vector_posterior[2] = 0
        vector_posterior[4] = 0
        vector_posterior[6] = 0
        
        vector_posterior[1] = vector_anterior[13]       
        vector_posterior[8] = 'En limpieza'
        vector_posterior[9] = '-'
        vector_posterior[12] = t_limpieza 
        vector_posterior[13] = vector_posterior[1] + vector_posterior[12]
    elif indice_minimo == 3 and  'Fin de limpieza' in vector_anterior[0] and 'Ocupado' in vector_anterior[8] and vector_posterior[10] > 0:
        
        vector_posterior[0] = 'Entrada' + vector_posterior[18][0]
        vector_posterior[1] = vector_posterior[13]
        vector_posterior[4] = 0
        vector_posterior[4] = 0
        vector_posterior[6] = 0
        vector_posterior[8] = 'Ocupado'
        vector_posterior[9] =  vector_posterior[18][0]
        vector_posterior[10] -= 1
        if 'futbol' in vector_posterior[18][0].lower():
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(inf_oc_fut, sup_oc_fut,vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            
        elif 'handball' in vector_posterior[18][0].lower():
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(inf_oc_hand, sup_oc_hand, vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            
        elif 'basket' in vector_posterior[18][0].lower():  
            vector_posterior[11] = random.random()
            vector_posterior[12] = uniforme(inf_oc_bas, sup_oc_bas, vector_posterior[11])
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1] 
        vector_posterior[18].pop(0)
       
   
        
    elif indice_minimo == 3 and 'Llegada' in vector_anterior[0] and  vector_posterior[10] > 0 and vector_posterior[8] == 'En limpieza':
        vector_posterior[10] -= 1
        vector_posterior[0] = 'Fin de limpieza'
        vector_posterior[8] = 'Ocupado' 
        vector_posterior[9] = vector_posterior[18][0]
        vector_posterior[1] = vector_posterior[13]
        vector_posterior[12] = 0
        vector_posterior[13] = 0 
         
        if 'futbol' in vector_posterior[18][0].lower():
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(inf_oc_fut, sup_oc_fut,vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            
        elif 'handball' in vector_posterior[18][0].lower():
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(inf_oc_hand, sup_oc_hand, vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            
        elif 'basket' in vector_posterior[18][0].lower():  
            vector_posterior[11] = random.random()
            vector_posterior[12] = uniforme(inf_oc_bas, sup_oc_bas, vector_posterior[11])
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1] 
        vector_posterior[18].pop(0)
         
    elif indice_minimo == 3 and ( 'entrada' in vector_anterior[0].lower() or 'llegada' in vector_anterior[0].lower()):
        vector_posterior[11] = 0
        vector_posterior[0] = 'Inicio de limpieza'
        vector_posterior[2] = 0
        vector_posterior[4] = 0
        vector_posterior[6] = 0
        
        vector_posterior[1] = vector_anterior[13]       
        vector_posterior[8] = 'En limpieza'
        vector_posterior[9] = '-'
        vector_posterior[12] = t_limpieza 
        vector_posterior[13] = vector_posterior[1] + vector_posterior[12]
 
    elif indice_minimo == 3 and vector_anterior[0] == "Inicio de limpieza" and  vector_posterior[10] > 0:
        vector_posterior[10] -= 1
        vector_posterior[0] = 'Entrada ' + vector_posterior[18][0]
        vector_posterior[9] = vector_posterior[18][0]
        vector_posterior[18].pop(0)
        vector_posterior[1] = vector_anterior[13]
        vector_posterior[8] = 'Ocupado'
        
        
        if 'futbol' in vector_posterior[0].lower():
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(inf_oc_fut, sup_oc_fut,vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            
        elif 'handball' in vector_posterior[0].lower():
            vector_posterior[11] = random.random()
            vector_posterior[12] =  uniforme(inf_oc_hand, sup_oc_hand, vector_posterior[11]) 
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
            
        elif 'basket' in vector_posterior[0].lower():  
            vector_posterior[11] = random.random()
            vector_posterior[12] = uniforme(inf_oc_bas, sup_oc_bas, vector_posterior[11])
            vector_posterior[13] = vector_posterior[12] + vector_posterior[1]
        
    elif indice_minimo == 3 and vector_anterior[0] == "Inicio de limpieza":
        vector_posterior[11] = 0 
        vector_posterior [0] = 'Fin de limpieza'
        vector_posterior [1]  = vector_anterior[13] 
        vector_posterior[8] = 'Libre'
        vector_posterior[12] = 0
        vector_posterior[13] = 0
    vector_posterior[1] = round(vector_posterior[1],4)
    vector_posterior[2] = round(vector_posterior[2],4)
    vector_posterior[3] = round(vector_posterior[3],4)
    vector_posterior[4] = round(vector_posterior[4],4)
    vector_posterior[5] = round(vector_posterior[5],4)
    vector_posterior[6] = round(vector_posterior[6],4)
    vector_posterior[7] = round(vector_posterior[7],4)
    vector_posterior[11] = round(vector_posterior[11],4)
    vector_posterior[12] = round(vector_posterior[12],4)
    vector_posterior[13] = round(vector_posterior[13],4)
    vector_posterior[14] = round(vector_posterior[14],4)
    vector_posterior[15] = round(vector_posterior[15],4)
    vector_posterior[16] = round(vector_posterior[16],4)
    vector_posterior[17] = round(vector_posterior[17],4)
    
    return vector_posterior


# cambiar las funciones unifrme y exponencial y sacrle el *60, ya que en algunas se usan pero ya estan puestas en minutos,, agregar el * 60 en las lineas que se calculen en horas nomas.
#cmabiar los numeros por la entradas. 

class GestionFila:
    def __init__(self, root):
        # PESTAÑA 1
        pestaña(self, root)
    def llamar(self):
        tiempo_final = float(self.entry_TS.get())
        t_limpieza = float(self.entry_L.get())
        
        med_lleg_futbol = float(self.entry_FL.get())
        inf_oc_fut= float(self.entry_FOI.get())
        sup_oc_fut= float(self.entry_FOS.get())
        
        inf_lleg_hand= float(self.entry_HLI.get())
        sup_lleg_hand = float(self.entry_HLS.get())
        inf_oc_hand = float(self.entry_HOI.get())
        sup_oc_hand = float(self.entry_HOS.get())
        
        inf_lleg_bas = float(self.entry_BLI.get())
        sup_lleg_bas = float(self.entry_BLS.get())
        inf_oc_bas = float(self.entry_BOI.get())
        sup_oc_bas = float(self.entry_BOS.get())
        
        vector_anterior = inicializar_vector(med_lleg_futbol, inf_lleg_hand, sup_lleg_hand, inf_lleg_bas, sup_lleg_bas)
        data = []
        data.append(copy.deepcopy(vector_anterior))

        while vector_anterior[1] <= tiempo_final:
            vector_anterior = generacion_linea(vector_anterior, t_limpieza, med_lleg_futbol, inf_oc_fut, sup_oc_fut, inf_lleg_hand, sup_lleg_hand, inf_oc_hand, sup_oc_hand, inf_lleg_bas, sup_lleg_bas, inf_oc_bas, sup_oc_bas)
            data.append(copy.deepcopy(vector_anterior))
        table_text = tabulate(data, headers=['Evento', 'Reloj', '?',
                                            'Tpo llegada', '?', 'Tpo llegada', '?',
                                            'Tpo llegada', 'Estado','Quien', 'Cola', '?', 'TPO', 
                                            'Tpo des', 'F', 'B', 'HB', 'ACUTLC', 'cola'])

        root = tk.Tk()
        root.title("Tabla de visitas")
        
        text_area = tk.Text(root, height=40, width=170)
        text_area.insert(tk.END, table_text)
        text_area.pack(expand=True, fill=tk.BOTH)
        
        root.mainloop()
    
# Ejemplo de uso
root = tk.Tk()
app = GestionFila(root)
root.mainloop()