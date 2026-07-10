import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint com Seleção")
        
        # Canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Criando algumas figuras iniciais para teste
        # Note que adicionamos a tag "movivel" para identificar o que pode ser selecionado
        self.canvas.create_rectangle(50, 50, 150, 150, fill="blue", tags="movivel")
        self.canvas.create_oval(200, 50, 300, 150, fill="red", tags="movivel")
        
        # Variáveis de controle para a seleção
        self.objeto_selecionado = None
        self.start_x = 0
        self.start_y = 0
        
        # Binds do mouse
        self.canvas.bind("<Button-1>", self.ao_clicar)
        self.canvas.bind("<B1-Motion>", self.ao_arrastar)
        self.canvas.bind("<ButtonRelease-1>", self.ao_soltar)

    def ao_clicar(self, event):
        # Encontra o objeto mais próximo do clique do mouse
        # O método find_closest retorna uma tupla com o ID do objeto
        item = self.canvas.find_closest(event.x, event.y)
        
        if item:
            tags = self.canvas.gettags(item[0])
            # Verifica se o objeto clicado tem a tag "movivel"
            if "movivel" in tags:
                self.objeto_selecionado = item[0]
                self.start_x = event.x
                self.start_y = event.y
                
                # Opcional: Dar um feedback visual (ex: adicionar uma borda preta)
                self.canvas.itemconfig(self.objeto_selecionado, outline="black", width=3)

    def ao_arrastar(self, event):
        if self.objeto_selecionado:
            # Calcula o quanto o mouse se moveu desde o último frame
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            
            # Move o objeto selecionado pela diferença de distância
            self.canvas.move(self.objeto_selecionado, dx, dy)
            
            # Atualiza a posição inicial para o próximo movimento
            self.start_x = event.x
            self.start_y = event.y

    def ao_soltar(self, event):
        if self.objeto_selecionado:
            # Remove o feedback visual ao soltar o clique
            self.canvas.itemconfig(self.objeto_selecionado, outline="", width=1)
            self.objeto_selecionado = None

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
