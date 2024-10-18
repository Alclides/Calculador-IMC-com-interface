import tkinter as tk
from tkinter import messagebox

#calculadora de imc em python

def calc_imc():
    try:
        #pedindo irformacões ao úsuario
        peso = float(entry_peso.get())
        alt = float(entry_altura.get())

        #calculando dados obtidos
        imc = peso / (alt ** 2)

        #razão matemática, dados retidos de https://www.tuasaude.com/calculadora/imc/
        if imc <= 18.9:
            messagebox.showinfo("Resultado", f"IMC {imc:.2f}, Magreza")
        elif imc <= 24.9:
            messagebox.showinfo("Resultado", f"IMC: {imc:.2f}, Normal")
        elif imc <= 29.9:
            messagebox.showinfo("Resultado" ,f"IMC: {imc:.2f}, Sobrepeso")
        elif imc <= 34.9:
            messagebox.showinfo("Resultado" ,f"IMC: {imc:.2f}, Obesidade de grau 1")
        elif imc <= 40:
            messagebox.showinfo("Resultado", f"IMC: {imc:.2f}, Obsidade de grau 2(Severa)")
        else:
            messagebox.showinfo("Resultado", f"IMC: {imc:.2f}, Obesidade de grau 3(Mórbida)")
    except ValueError:
        messagebox.showerror("Inválido")
#criando janela
janela = tk.Tk()
janela.title("Calculador de IMC")
janela.geometry("300x200")

#criando coletores de informações
label_peso = tk.Label(janela, text="Peso (KG): ")
label_peso.pack()

entry_peso = tk.Entry(janela)
entry_peso.pack()

label_altura = tk.Label(janela, text="Altura (M): ")
label_altura.pack()

entry_altura = tk.Entry(janela)
entry_altura.pack()

#botão de calculo com função def
botao_calc = tk.Button(janela, text="Calcular IMC", command=calc_imc)
botao_calc.pack()

#mantendo janela aberta até que o usúario feche a aba
janela.mainloop()