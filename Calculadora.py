import tkinter as tk


def calcular_imc():
    try:
        # Obter valores do peso e altura
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        # Calcular o IMC
        imc = peso / (altura ** 2)

        # Exibir o resultado
        label_resultado.config(text=f"IMC: {imc:.2f}")
    except ValueError:
        label_resultado.config(text="Por favor, insira valores válidos!")


# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x200")

# Rótulo de Peso
label_peso = tk.Label(janela, text="Peso (kg):")
label_peso.pack()

# Campo de entrada de peso
entry_peso = tk.Entry(janela)
entry_peso.pack()

# Rótulo de Altura
label_altura = tk.Label(janela, text="Altura (m):")
label_altura.pack()

# Campo de entrada de altura
entry_altura = tk.Entry(janela)
entry_altura.pack()

# Botão para calcular o IMC
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
botao_calcular.pack()

# Rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="IMC: ")
label_resultado.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
