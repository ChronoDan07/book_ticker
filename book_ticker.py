import tkinter as tk
from PyPDF2 import PdfReader

class BookTickerApp:
    def __init__(self, pdf_file):
        self.current_page = 0
        self.page_display = 1
        self.paused = False
        self.text_offset = 0
        self.speed = 1
        self.pdf_file = pdf_file
        self.pg_nm = 0

        self.root = tk.Tk()
        self.root.title("Book Ticker")
        self.create_widgets()

    def extract_text(self, page_num):
        text = ""
        with open(self.pdf_file, "rb") as file:
            reader = PdfReader(file)
            self.pg_nm = len(reader.pages)
            if page_num < len(reader.pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                text = text.replace("\n", " ")
        return text

    def next_page(self):
        if self.pg_nm == 1 or self.current_page + 1 == self.pg_nm:
            return
        self.text_offset = 700
        self.current_page += 1
        self.page_display += 1
        self.page_label.config(text=f"Page: {self.page_display}")
        self.update_text()

    def previous_page(self):
        self.text_offset = 700
        if self.current_page > 0:
            self.current_page -= 1
            self.page_display -= 1
            self.page_label.config(text=f"Page: {self.page_display}")
            self.update_text()
        if self.current_page == 0:
            self.update_text()

    def update_text(self):
        txt = self.extract_text(self.current_page)
        self.text_widget.config(text=txt)

    def create_widgets(self):
        self.root.maxsize(900,150)
        self.root.minsize(700,130)
        text_color = "black"
        self.text_widget = tk.Label(self.root, text="")
        self.text_widget.pack(padx=10, pady=10)
        self.text_widget.config(font=("Times New Roman", 30), foreground=text_color)
        text_width = self.text_widget.winfo_reqwidth()
        self.text_offset = 700

        bt_fr = tk.Frame(self.root, bg="lightgray")
        bt_fr.pack(side="bottom", pady=0)
        prev = tk.Button(bt_fr, text="⏮", width=1, height=1, command=self.previous_page)
        self.play_pause = tk.Button(bt_fr, text="II", width=2, height=1, command=self.toggle_pause_play)
        decel = tk.Button(bt_fr, text="⯬", width=1, height=1, command=self.toggle_speed_down)
        accel = tk.Button(bt_fr, text="⯮", width=1, height=1, command=self.toggle_speed_up)
        next_btn = tk.Button(bt_fr, text="⏭", width=1, height=1, command=self.next_page)
        self.speed_label = tk.Label(self.root, text=f"Speed: {self.speed}x")
        self.speed_label.pack(side="top")
        self.page_label = tk.Label(self.root, text=f"Page: {self.page_display}")
        self.page_label.pack(side="top", pady=0)

        prev.pack(side="left", padx=0, pady=5)
        decel.pack(side="left", padx=0, pady=5)
        self.play_pause.pack(side="left", padx=0, pady=5)
        accel.pack(side="left", padx=0, pady=5)
        next_btn.pack(side="left", padx=0, pady=5)

        self.move_text(self.text_widget, self.root.winfo_width(), self.root.winfo_height(), text_width)
        self.update_text()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def move_text(self, text_widget, win_width, win_height, text_width):
        if not self.paused:
            win_width = self.root.winfo_width()
            win_height = self.root.winfo_height()
            text_widget.place(x=self.text_offset, y=win_height//2, anchor="w")
            self.text_offset -= self.speed
        text_widget.after(10, self.move_text, text_widget, win_width, win_height, text_width)

    def toggle_pause_play(self):
        self.paused = not self.paused
        if self.paused:
            self.play_pause.config(text="▶")
        else:
            self.play_pause.config(text="II")

    def toggle_speed_up(self):
        if self.speed >= 10:
            return
        self.speed += 1
        self.speed_label.config(text=f"Speed: {self.speed}x")

    def toggle_speed_down(self):
        if self.speed == 1:
            return
        self.speed -= 1
        self.speed_label.config(text=f"Speed: {self.speed}x")

    def run(self):
        self.center_window(700,130)
        self.root.mainloop()


def main():
    app = BookTickerApp("mock-pdf-2.pdf")
    app.run()

if __name__ == "__main__":
    main()
