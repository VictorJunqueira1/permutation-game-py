import tkinter as tk
from tkinter import messagebox
import random
import itertools

def gerar_permutacoes(lista):
    return [''.join(map(str, perm)) for perm in itertools.permutations(lista)]

class PermutacaoJogo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo Adivinhe a Permutação")
        self.geometry("600x850")
        self.configure(bg="#f0f8ff")

        self.permutacao_correta = None
        self.permutacoes = None
        self.chances = 5
        self.criar_widgets()

    def criar_widgets(self):
        # Cabeçalho
        self.header_frame = tk.Frame(self, bg="#4682b4", pady=10)
        self.header_frame.pack(fill=tk.X)

        self.titulo_label = tk.Label(self.header_frame, text="Adivinhe a Permutação", font=("Arial", 20, "bold"), bg="#4682b4", fg="white")
        self.titulo_label.pack(pady=5)

        # Seleção de nível de dificuldade
        self.nivel_frame = tk.Frame(self, bg="#f0f8ff", pady=20)
        self.nivel_frame.pack(pady=10)

        self.nivel_label = tk.Label(self.nivel_frame, text="Escolha o nível de dificuldade:", bg="#f0f8ff", font=("Arial", 14))
        self.nivel_label.pack(pady=5)

        # Botões de dificuldade organizados em duas colunas
        self.dificuldade_frame = tk.Frame(self.nivel_frame, bg="#f0f8ff")
        self.dificuldade_frame.pack(pady=10)

        self.coluna_esquerda = tk.Frame(self.dificuldade_frame, bg="#f0f8ff")
        self.coluna_esquerda.grid(row=0, column=0, padx=40)

        self.coluna_direita = tk.Frame(self.dificuldade_frame, bg="#f0f8ff")
        self.coluna_direita.grid(row=0, column=1, padx=40)

        self.nivel_var = tk.StringVar(value="Fácil")  # Define o nível padrão

        # Coluna Esquerda
        self.facil_radio = tk.Radiobutton(self.coluna_esquerda, text="Fácil (2 dígitos)", variable=self.nivel_var, value="Fácil", bg="#f0f8ff", font=("Arial", 12))
        self.facil_radio.pack(pady=5)

        self.dificil_radio = tk.Radiobutton(self.coluna_esquerda, text="Difícil (4 dígitos)", variable=self.nivel_var, value="Difícil", bg="#f0f8ff", font=("Arial", 12))
        self.dificil_radio.pack(pady=5)

        # Coluna Direita
        self.medio_radio = tk.Radiobutton(self.coluna_direita, text="Médio (3 dígitos)", variable=self.nivel_var, value="Médio", bg="#f0f8ff", font=("Arial", 12))
        self.medio_radio.pack(pady=5)

        self.impossivel_radio = tk.Radiobutton(self.coluna_direita, text="Impossível (5 dígitos)", variable=self.nivel_var, value="Impossível", bg="#f0f8ff", font=("Arial", 12))
        self.impossivel_radio.pack(pady=5)

        # Botão para gerar permutação
        self.gerar_button = tk.Button(self.nivel_frame, text="Gerar Permutação", command=self.gerar_permutacao, font=("Arial", 14), bg="#4682b4", fg="white", width=20)
        self.gerar_button.pack(pady=15)

        # Adivinhação
        self.adivinhacao_frame = tk.Frame(self, bg="#f0f8ff", pady=20)
        self.adivinhacao_frame.pack(pady=10)

        self.adivinhacao_label = tk.Label(self.adivinhacao_frame, text="Digite sua adivinhação (sequência de números):", bg="#f0f8ff", font=("Arial", 14))
        self.adivinhacao_label.pack(pady=5)

        self.adivinhacao_entry = tk.Entry(self.adivinhacao_frame, font=("Arial", 14), justify='center')
        self.adivinhacao_entry.pack(pady=5, ipadx=5, ipady=5)

        self.tentar_button = tk.Button(self.adivinhacao_frame, text="Tentar", command=self.tentar_adivinhar, font=("Arial", 14), bg="#ffa07a", fg="white", width=20)
        self.tentar_button.pack(pady=10)

        self.encerrar_button = tk.Button(self.adivinhacao_frame, text="Encerrar Jogo", command=self.encerrar_jogo, font=("Arial", 14), bg="#dc143c", fg="white", width=20)
        self.encerrar_button.pack(pady=10)

        # Resultado
        self.resultado_frame = tk.Frame(self, bg="#f0f8ff", pady=20)
        self.resultado_frame.pack(pady=10)

        self.resultado_label = tk.Label(self.resultado_frame, text="", bg="#f0f8ff", font=("Arial", 14))
        self.resultado_label.pack(pady=10)

        self.chances_label = tk.Label(self.resultado_frame, text=f"Chances restantes: {self.chances}", bg="#f0f8ff", font=("Arial", 14))
        self.chances_label.pack(pady=10)

        # Botão de reiniciar quiz
        self.reiniciar_button = tk.Button(self.resultado_frame, text="Reiniciar Quiz", command=self.reiniciar_jogo, font=("Arial", 14), bg="#4682b4", fg="white", width=20)
        self.reiniciar_button.pack(pady=10)
        self.reiniciar_button.pack_forget()

    def gerar_permutacao(self):
        nivel = self.nivel_var.get()
        tamanho = {"Fácil": 2, "Médio": 3, "Difícil": 4, "Impossível": 5}[nivel]
        
        numeros = list(range(1, tamanho + 1))
        self.permutacoes = gerar_permutacoes(numeros)
        self.permutacao_correta = random.choice(self.permutacoes)
        self.resultado_label.config(text="Permutação gerada. Faça sua adivinhação.")
        self.chances = 5
        self.chances_label.config(text=f"Chances restantes: {self.chances}")
        self.tentar_button.config(state=tk.NORMAL) 
        self.reiniciar_button.pack_forget()

    def tentar_adivinhar(self):
        if self.permutacao_correta is None:
            messagebox.showwarning("Aviso", "Por favor, gere uma permutação primeiro.")
            return

        adivinhacao = self.adivinhacao_entry.get().strip()
        if len(adivinhacao) != len(self.permutacao_correta):
            messagebox.showerror("Erro", f"Por favor, insira uma adivinhação com {len(self.permutacao_correta)} dígitos.")
            return

        if adivinhacao == self.permutacao_correta:
            self.resultado_label.config(text="Parabéns! Você adivinhou corretamente.")
            self.chances = 0
            self.destaque_permutacao()
            self.tentar_button.config(state=tk.DISABLED)
            self.reiniciar_button.pack(pady=10)
        else:
            self.chances -= 1
            dica = "Mais alto!" if adivinhacao < self.permutacao_correta else "Mais baixo!"
            if self.chances > 0:
                self.resultado_label.config(text=f"Adivinhação incorreta. {dica}")
            else:
                self.resultado_label.config(text=f"Você perdeu! A permutação correta era: {self.permutacao_correta}")
                self.tentar_button.config(state=tk.DISABLED)
                self.reiniciar_button.pack(pady=10)

        self.chances_label.config(text=f"Chances restantes: {self.chances}")

    def destaque_permutacao(self):
        for _ in range(3):
            self.resultado_label.config(text=f"A permutação correta era: {self.permutacao_correta}", fg="#ff0000")
            self.after(500, lambda: self.resultado_label.config(text=f"A permutação correta era: {self.permutacao_correta}", fg="#000000"))
            self.after(1000, lambda: self.resultado_label.config(text=f"A permutacao correta era: {self.permutacao_correta}", fg="#ff0000"))

    def encerrar_jogo(self):
        self.destroy()

    def reiniciar_jogo(self):
        self.permutacao_correta = None
        self.permutacoes = None
        self.chances = 5
        self.resultado_label.config(text="")
        self.chances_label.config(text=f"Chances restantes: {self.chances}")
        self.adivinhacao_entry.delete(0, tk.END)
        self.tentar_button.config(state=tk.NORMAL)
        self.reiniciar_button.pack_forget()

if __name__ == "__main__":
    app = PermutacaoJogo()
    app.mainloop()