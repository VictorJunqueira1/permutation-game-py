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
        self.geometry("800x600")
        self.configure(bg="#f0f8ff")  # Cor de fundo mais clara

        self.permutacao_correta = None
        self.permutacoes = None
        self.chances = 5
        self.criar_widgets()

    def criar_widgets(self):
        # Cabeçalho
        self.header_frame = tk.Frame(self, bg="#4682b4", pady=10)
        self.header_frame.pack(fill=tk.X)

        self.titulo_label = tk.Label(self.header_frame, text="Jogo Adivinhe a Permutação", font=("Helvetica", 16), bg="#4682b4", fg="white")
        self.titulo_label.pack(pady=5)

        # Configuração do tamanho
        self.tamanho_frame = tk.Frame(self, bg="#f0f8ff", pady=10)
        self.tamanho_frame.pack(pady=10)

        self.tamanho_label = tk.Label(self.tamanho_frame, text="Digite o tamanho da sequência (máx. 4):", bg="#f0f8ff", font=("Helvetica", 12))
        self.tamanho_label.pack(pady=5)

        self.tamanho_entry = tk.Entry(self.tamanho_frame, font=("Helvetica", 12))
        self.tamanho_entry.pack(pady=5)

        self.gerar_button = tk.Button(self.tamanho_frame, text="Gerar Permutação", command=self.gerar_permutacao, font=("Helvetica", 12), bg="#32cd32", fg="white")
        self.gerar_button.pack(pady=10)

        # Adivinhação
        self.adivinhacao_frame = tk.Frame(self, bg="#f0f8ff", pady=10)
        self.adivinhacao_frame.pack(pady=10)

        self.adivinhacao_label = tk.Label(self.adivinhacao_frame, text="Digite sua adivinhação (sequência de números sem espaços):", bg="#f0f8ff", font=("Helvetica", 12))
        self.adivinhacao_label.pack(pady=5)

        self.adivinhacao_entry = tk.Entry(self.adivinhacao_frame, font=("Helvetica", 12))
        self.adivinhacao_entry.pack(pady=5)

        self.tentar_button = tk.Button(self.adivinhacao_frame, text="Tentar", command=self.tentar_adivinhar, font=("Helvetica", 12), bg="#ffa07a", fg="white")
        self.tentar_button.pack(pady=10)

        self.encerrar_button = tk.Button(self.adivinhacao_frame, text="Encerrar Jogo", command=self.encerrar_jogo, font=("Helvetica", 12), bg="#dc143c", fg="white")
        self.encerrar_button.pack(pady=10)

        # Resultado
        self.resultado_frame = tk.Frame(self, bg="#f0f8ff", pady=10)
        self.resultado_frame.pack(pady=10)

        self.resultado_label = tk.Label(self.resultado_frame, text="", bg="#f0f8ff", font=("Helvetica", 12))
        self.resultado_label.pack(pady=10)

        self.chances_label = tk.Label(self.resultado_frame, text=f"Chances restantes: {self.chances}", bg="#f0f8ff", font=("Helvetica", 12))
        self.chances_label.pack(pady=10)

    def gerar_permutacao(self):
        try:
            tamanho = int(self.tamanho_entry.get())
            if tamanho < 2 or tamanho > 4:
                messagebox.showerror("Erro", "O tamanho da sequência deve ser entre 2 e 4.")
                return
            
            numeros = list(range(1, tamanho + 1))
            self.permutacoes = gerar_permutacoes(numeros)
            self.permutacao_correta = random.choice(self.permutacoes)
            self.resultado_label.config(text="Permutação gerada. Faça sua adivinhação.")
            self.chances = 5
            self.chances_label.config(text=f"Chances restantes: {self.chances}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    def tentar_adivinhar(self):
        if self.permutacao_correta is None:
            messagebox.showwarning("Aviso", "Por favor, gere uma permutação primeiro.")
            return

        adivinhacao = self.adivinhacao_entry.get().strip()
        if len(adivinhacao) != len(self.permutacao_correta):
            messagebox.showerror("Erro", "Por favor, insira uma adivinhação com o mesmo número de dígitos da permutação gerada.")
            return

        if adivinhacao == self.permutacao_correta:
            self.resultado_label.config(text="Parabéns! Você adivinhou corretamente.")
            self.chances = 0
            self.destaque_permutacao()
        else:
            self.chances -= 1
            if self.chances > 0:
                if adivinhacao < self.permutacao_correta:
                    dica = "Mais alto!"
                else:
                    dica = "Mais baixo!"
                self.resultado_label.config(text=f"Adivinhação incorreta. {dica} Tentativas restantes: {self.chances}")
            else:
                self.resultado_label.config(text=f"Você perdeu! A permutação correta era: {self.permutacao_correta}")

        self.chances_label.config(text=f"Chances restantes: {self.chances}")

    def destaque_permutacao(self):
        # Função para destacar a permutação correta
        for _ in range(3):  # Número de vezes que a animação ocorre
            self.resultado_label.config(text=f"A permutação correta era: {self.permutacao_correta}", fg="#ff0000")
            self.after(500, lambda: self.resultado_label.config(text=f"A permutação correta era: {self.permutacao_correta}", fg="#000000"))
            self.after(1000, lambda: self.resultado_label.config(text=f"A permutação correta era: {self.permutacao_correta}", fg="#ff0000"))

    def encerrar_jogo(self):
        self.destroy()

if __name__ == "__main__":
    app = PermutacaoJogo()
    app.mainloop()
