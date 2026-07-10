#ferramenta para mover as figuras feitas no canvas

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
