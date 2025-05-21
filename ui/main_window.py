import os
import datetime
import customtkinter as ctk
from tkinter import messagebox, simpledialog
from core.parser_handler import handle_parse
from core.merger import handle_merge

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("520x440")
        self.title("PiNMetrica 3.0")
        self.resizable(False, False)

        self.frame = ctk.CTkFrame(self, corner_radius=20)
        self.frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.label_title = ctk.CTkLabel(self.frame, text="PiNMetrica 3.0", font=ctk.CTkFont(size=26, weight="bold"))
        self.label_title.pack(pady=(10, 20))

        self.btn_parse = ctk.CTkButton(self.frame, text="1. Збір даних", command=self.menu_parse, height=44)
        self.btn_parse.pack(fill="x", padx=40, pady=(0, 20))

        self.btn_merge = ctk.CTkButton(self.frame, text="2. Фільтрація таблиць", command=self.menu_merge, height=44)
        self.btn_merge.pack(fill="x", padx=40, pady=(0, 20))

        self.status = ctk.CTkLabel(self.frame, text="", font=ctk.CTkFont(size=14))
        self.status.pack(pady=(10, 0))

    def menu_parse(self):
        queries = simpledialog.askstring("Пошук Pinterest", "Введіть пошукові запити або посилання через кому:", parent=self)
        if not queries:
            return
        queries_list = [q.strip() for q in queries.split(",") if q.strip()]
        if not queries_list:
            return

        date_folder = datetime.datetime.now().strftime("%d.%m.%y %H-%M-%S")
        base_path = os.path.join(os.getcwd(), "Search", date_folder)
        os.makedirs(base_path, exist_ok=True)

        for q in queries_list:
            handle_parse(q, base_path)

        self.status.configure(text="Парсинг завершено")

        clear_empty = messagebox.askyesno("Очистка", "Очистити пусті рядки?", parent=self)
        if clear_empty:
            pass

        msg = f"Готово! Файли збережено у:\n{base_path}"
        messagebox.showinfo("Результат", msg, parent=self)
        self.status.configure(text=msg)

    def menu_merge(self):
        filters_path = os.path.join(os.getcwd(), "Filters")
        if not os.path.exists(filters_path):
            messagebox.showerror("Помилка", "Папка Filters не існує", parent=self)
            return

        y_n = messagebox.askyesno("Фільтрація", "Надіслали файли у Filters?", parent=self)
        if not y_n:
            return

        date_folder = datetime.datetime.now().strftime("%d.%m.%y %H-%M-%S")
        out_folder = os.path.join(filters_path, date_folder)
        os.makedirs(out_folder, exist_ok=True)

        handle_merge(out_folder)

        msg = f"Фільтрація завершена!\nФайл у:\n{out_folder}"
        messagebox.showinfo("Результат", msg, parent=self)
        self.status.configure(text=msg)