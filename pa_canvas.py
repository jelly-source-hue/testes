import tkinter as tk

class AplicativoDesenhoCelular:
    def __init__(self, root):
        self.root = root
        self.root.title("Rabiscos no Canvas")
        
        # Canvas ocupando a tela toda
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.ultimo_x = None
        self.ultimo_y = None
        
        # Eventos adaptados para telas de toque
        self.canvas.bind("<Button-1>", self.iniciar_desenho)       # Primeiro toque
        self.canvas.bind("<B1-Motion>", self.desenhar)            # Arrastar o dedo
        self.canvas.bind("<ButtonRelease-1>", self.parar_desenho) # Tirar o dedo da tela
        
        # Botão de limpar maior (melhor para tocar com o dedo)
        self.botao_limpar = tk.Button(root, text="Limpar Tela", font=("Arial", 14), command=self.limpar_canvas)
        self.botao_limpar.pack(pady=10, fill=tk.X)

    def iniciar_desenho(self, event):
        self.ultimo_x = event.x
        self.ultimo_y = event.y

    def desenhar(self, event):
        if self.ultimo_x is not None and self.ultimo_y is not None:
            self.canvas.create_line(
                self.ultimo_x, self.ultimo_y, 
                event.x, event.y, 
                width=5, fill="black", capstyle=tk.ROUND, smooth=True
            )
        self.ultimo_x = event.x
        self.ultimo_y = event.y

    def parar_desenho(self, event):
        # Reseta as variáveis quando o usuário tira o dedo da tela
        self.ultimo_x = None
        self.ultimo_y = None

    def limpar_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    # Linha opcional para abrir em tela cheia no celular, se o seu ambiente suportar:
    # root.attributes('-fullscreen', True)
    app = AplicativoDesenhoCelular(root)
    root.mainloop()
  
