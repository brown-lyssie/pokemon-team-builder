import tkinter as tk
import tkinter.ttk as ttk
from pokemon import Pokemon as Pokemon
from Widgets import MainWindow as MainWindow


def main():
    print("Hello world")
    #tk._test() 
    window = tk.Tk()
    window.title("Pokemon Team Builder by Lyssie Brown")
    #window.geometry("750x500")
    pikachu = Pokemon()
    print(pikachu)
    print(set(ttk.Button().configure().keys()))
    main_window = MainWindow(window)

    window.mainloop()

if __name__ == "__main__":
    main()