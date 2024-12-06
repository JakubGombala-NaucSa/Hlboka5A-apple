import tkinter as tk

root = tk.Tk()
root.title("Preteky lopticiek")

platno = tk.Canvas(width=400, height=600, bg="lightblue")
platno.pack()

lopticky = []

def vytvor_lopticky():
    for i in range(10):
        
