'''import tkinter as tk

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
    root.mainloop()'''

import tkinter as tk

class SimplePaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Paint - Tkinter")
        
        # Variáveis de controle
        self.current_tool = "Retângulo"  # Ferramenta inicial
        self.start_x = None
        self.start_y = None
        self.current_shape = None
        self.selected_item = None
        
        # --- Interface Gráfica (GUI) ---
        
        # Painel de ferramentas (Top)
        self.toolbar = tk.Frame(root, bg="lightgray", padding=5)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Botões de ferramentas
        self.btn_rect = tk.Button(self.toolbar, text="Retângulo", command=lambda: self.set_tool("Retângulo"), relief=tk.SUNKEN)
        self.btn_rect.pack(side=tk.LEFT, padx=5)
        
        self.btn_oval = tk.Button(self.toolbar, text="Oval", command=lambda: self.set_tool("Oval"))
        self.btn_oval.pack(side=tk.LEFT, padx=5)
        
        self.btn_move = tk.Button(self.toolbar, text="Mover", command=lambda: self.set_tool("Mover"))
        self.btn_move.pack(side=tk.LEFT, padx=5)
        
        # Área de desenho (Canvas)
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Eventos do Mouse
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def set_tool(self, tool_name):
        """Altera a ferramenta atual e atualiza o visual dos botões."""
        self.current_tool = tool_name
        
        # Reset visual dos botões
        self.btn_rect.config(relief=tk.RAISED)
        self.btn_oval.config(relief=tk.RAISED)
        self.btn_move.config(relief=tk.RAISED)
        
        # Destaca o botão ativo
        if tool_name == "Retângulo":
            self.btn_rect.config(relief=tk.SUNKEN)
        elif tool_name == "Oval":
            self.btn_oval.config(relief=tk.SUNKEN)
        elif tool_name == "Mover":
            self.btn_move.config(relief=tk.SUNKEN)

    def on_button_press(self, event):
        """Detecta o primeiro clique do mouse."""
        self.start_x = event.x
        self.start_y = event.y

        if self.current_tool == "Mover":
            # Encontra o objeto mais próximo do clique
            shape = self.canvas.find_closest(event.x, event.y)
            if shape:
                self.selected_item = shape[0]
        else:
            # Cria a forma temporária (com contorno azul para destacar a criação)
            if self.current_tool == "Retângulo":
                self.current_shape = self.canvas.create_rectangle(
                    self.start_x, self.start_y, self.start_x, self.start_y, 
                    outline="blue", fill="lightblue", width=2
                )
            elif self.current_tool == "Oval":
                self.current_shape = self.canvas.create_oval(
                    self.start_x, self.start_y, self.start_x, self.start_y, 
                    outline="blue", fill="lightgreen", width=2
                )

    def on_move_press(self, event):
        """Detecta o movimento do mouse enquanto o botão está pressionado."""
        cur_x, cur_y = event.x, event.y

        if self.current_tool == "Mover" and self.selected_item:
            # Calcula a distância movida
            dx = cur_x - self.start_x
            dy = cur_y - self.start_y
            # Move o objeto selecionado
            self.canvas.move(self.selected_item, dx, dy)
            # Atualiza o ponto inicial para o próximo movimento
            self.start_x = cur_x
            self.start_y = cur_y
        elif self.current_shape:
            # Redimensiona a figura que está sendo criada em tempo real
            self.canvas.coords(self.current_shape, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        """Finaliza a ação ao soltar o botão do mouse."""
        if self.current_shape:
            # Muda a cor da borda para preto para indicar que a criação terminou
            self.canvas.itemconfig(self.current_shape, outline="black")
        
        # Limpa as variáveis de controle de criação/seleção
        self.current_shape = None
        self.selected_item = None


# Inicialização do programa
if __name__ == "__main__":
    root = tk.Tk()
    app = SimplePaint(root)
    root.mainloop()
    
