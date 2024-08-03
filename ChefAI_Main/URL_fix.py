class RecipeWindow(tk.Toplevel):
    def __init__(self, recipes):
        super().__init__()
        self.title("Recipe Suggestions")
        self.configure(bg="white")

        # Set minimum window size to prevent squishing
        self.minsize(600, 400)

        # Create a canvas and a scrollbar
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        row = 0
        for hit in recipes['hits']:  # Display the first 10 hits
            recipe = hit['recipe']
            label = tk.Label(self.scrollable_frame, text=recipe['label'], wraplength=500, font=("Arial", 12, "bold"))
            label.grid(row=row, column=0, columnspan=6, pady=2, sticky="WS")
            row += 1

            ingredient_label = tk.Label(self.scrollable_frame, text="Ingredients:")
            ingredient_label.grid(row=row, column=0, pady=2, sticky=tk.W)
            ingredients = "\n".join(recipe['ingredientLines'])
            ingredient_text = tk.Text(self.scrollable_frame, height=3, width=50)
            ingredient_text.insert(tk.END, ingredients)
            ingredient_text.grid(row=row, column=1, columnspan=5, pady=2, sticky=tk.W)
            ingredient_text.config(state=tk.DISABLED)
            row += 1

            cals = int(recipe['calories'])
            calories_label = tk.Label(self.scrollable_frame, text=f"Calories: {cals}")
            calories_label.grid(row=row, column=0, pady=2, sticky=tk.W)
            row += 1

            url_label = tk.Label(self.scrollable_frame, text="URL:")
            url_label.grid(row=row, column=0, pady=2, sticky=tk.W)

            # Create a clickable hyperlink label
            url_hyperlink = tk.Label(self.scrollable_frame, text=recipe['url'], fg="blue", cursor="hand2")
            url_hyperlink.grid(row=row, column=1, columnspan=5, pady=2, sticky=tk.W)
            url_hyperlink.bind("<Button-1>", lambda e, url=recipe['url']: self.open_url(url))
            row += 1

    def open_url(self, url):
        webbrowser.open_new(url)
