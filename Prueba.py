def editar_articulo(self):
    selected_item = self.comboboxbuscar.get()

    if not selected_item:
        messagebox.showerror("Error", "Seleccione un artículo para editar")
        return
    
    self.cur.execute("SELECT * FROM articulos WHERE articulo = ?", (selected_item,))
    resultado = self.cur.fetchone()

    if not resultado:
        messagebox.showerror("Error", "No se encontró el artículo seleccionado")
        return

    top = tk.Toplevel(self)
    top.title("Editar Artículo")
    top.geometry("700x400+200+50")
    top.config(bg='#C6D9E3')
    top.resizable(False, False)

    top.transient(self.master)
    top.grab_set()
    top.focus_set()
    top.lift()

    (articulo, precio, costo, stock, estado, image_path) = resultado
    tk.Label(top, text="Artículo: ", font='arial 12 bold', bg='#C6D9E3').place(x=20, y=20, width=80, height=25)
    entry_articulo = ttk.Entry(top, font='arial 12 bold')
    entry_articulo.place(x=120, y=20, width=250, height=30)
    entry_articulo.insert(0, articulo)

    tk.Label(top, text="Precio: ", font='arial 12 bold', bg='#C6D9E3').place(x=20, y=60, width=80, height=25)
    entry_precio = ttk.Entry(top, font='arial 12 bold')
    entry_precio.place(x=120, y=60, width=250, height=30)
    entry_precio.insert(0, precio)

    tk.Label(top, text="Costo: ", font='arial 12 bold', bg='#C6D9E3').place(x=20, y=100, width=80, height=25)
    entry_costo = ttk.Entry(top, font='arial 12 bold')
    entry_costo.place(x=120, y=100, width=250, height=30)
    entry_costo.insert(0, costo)

    tk.Label(top, text="Stock: ", font='arial 12 bold', bg='#C6D9E3').place(x=20, y=140, width=80, height=25)
    entry_stock = ttk.Entry(top, font='arial 12 bold')
    entry_stock.place(x=120, y=140, width=250, height=30)
    entry_stock.insert(0, stock)

    tk.Label(top, text="Estado: ", font='arial 12 bold', bg='#C6D9E3').place(x=20, y=180, width=80, height=25)
    entry_estado = ttk.Entry(top, font='arial 12 bold')
    entry_estado.place(x=120, y=180, width=250, height=30)
    entry_estado.insert(0, estado)

    self.frameimg = tk.Frame(top, bg='white', highlightbackground="gray", highlightthickness=1)
    self.frameimg.place(x=440, y=30, width=200, height=200)

    if image_path and os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.LANCZOS)
        self.product_image = ImageTk.PhotoImage(image)
        self.image_path = image_path
        image_label = tk.Label(self.frameimg, image=self.product_image)
        image_label.pack(expand=True, fill='both')

    btnImagen = tk.Button(top, text="Cargar Imagen", font='arial 12 bold', command=self.load_image)
    btnImagen.place(x=470, y=260, width=150, height=40)

    def guardar():
        nuevo_articulo = entry_articulo.get()
        nuevo_precio = entry_precio.get()
        nuevo_costo = entry_costo.get()
        nuevo_stock = entry_stock.get()
        nuevo_estado = entry_estado.get()

        if not nuevo_articulo or not nuevo_precio or not nuevo_costo or not nuevo_stock or not nuevo_estado:
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
        try:
            nuevo_precio = float(nuevo_precio)
            nuevo_costo = float(nuevo_costo)
            nuevo_stock = int(nuevo_stock)
        except ValueError:
            messagebox.showerror("Error", "Precio, costo y stock deben ser números")
            return
        
        if hasattr(self, 'image_path'):
            image_path = self.image_path
        else:
            image_path = (r"fotos/default.jpg")

        self.cur.execute("UPDATE articulos SET articulo = ?, precio = ?, costo = ?, stock = ?, estado = ?, image_path = ? WHERE articulo = ?",
                        (nuevo_articulo, nuevo_precio, nuevo_costo, nuevo_stock, nuevo_estado, image_path, selected_item))
        self.con.commit()

        self.articulos_combobox()

        self.after(0, lambda: self.cargar_articulos(filtro=nuevo_articulo))

        top.destroy()
        messagebox.showinfo("Éxito", "Artículo actualizado correctamente")

    btn_guardar = tk.Button(top, text='Guardar', font='arial 12 bold', command=guardar)
    btn_guardar.place(x=260, y=260, width=150, height=40)