import random
import time
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

class Visualizador:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista Aleatoria")

        self.array = []
        self.algorithm = tk.StringVar(value="Bubble Sort")


        controls_frame = ttk.Frame(self.root, padding=10) # Para ver que tan retirado estara la barra de inicio
        controls_frame.pack(fill=tk.X)

        ttk.Label(controls_frame, text="Algoritmo:").pack(side=tk.LEFT, padx=5)
        algo_menu = ttk.Combobox(
            controls_frame,
            textvariable=self.algorithm,
            values=["Bubble Sort", "Selection Sort"],
            state="Lectura",
        )
        algo_menu.pack(side=tk.LEFT, padx=5)

        ttk.Button(controls_frame, text="Generar", command=self.generate_array).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="Iniciar", command=self.start_sorting).pack(side=tk.LEFT, padx=5)
        ttk.Button(controls_frame, text="Reiniciar", command=self.reset).pack(side=tk.LEFT, padx=5)

        self.canvas = tk.Canvas(self.root, height=400, bg= "white") # Altura y color del cuadro
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def generate_array(self):
        self.array = [random.randint(10, 100) for _ in range(20)] # GENERA NUMEROS ALEATORIOS ENTRE 1O Y 100 Y CREA UNA LISTA CON 20 NUMEROS
        self.draw_array() # LLAMA LA FUNCION PARA DIBUJAR LA LISTA GENERADA

    def draw_array(self, highlight_indices=None):
        self.canvas.delete("all") # BORRA TODO
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        bar_width = canvas_width / len(self.array) # ANCHO DE CADA BARRA
        max_height = max(self.array)

        highlight_indices = highlight_indices or []

        for i, value in enumerate(self.array):
            x0 = i * bar_width
            y0 = canvas_height - (value / max_height) * canvas_height
            x1 = (i + 1) * bar_width
            y1 = canvas_height
            color = "red" if i in highlight_indices else "blue" # ES LO QUE HACE QUE LA BARRA SE PONGA ROJA
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
        self.root.update_idletasks() # ACTUALIZA LA GRAFICA

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    swapped = True
                    self.draw_array([j, j + 1])
                    time.sleep(0.1)
            if not swapped:
                break

    def Eleccion(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw_array([i, min_idx])
            time.sleep(0.1)

    def start_sorting(self):
        algorithm = self.algorithm.get()
        if algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Selection Sort":
            self.Eleccion()

    def reset(self):
        self.array = []
        self.canvas.delete("all")

if __name__ == "__main__":
    root = ttk.Window(themename="flatly") #flatly
    app = Visualizador(root)
    root.mainloop()
