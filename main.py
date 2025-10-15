# flight_reservation_app/main.py
import tkinter as tk
from tkinter import ttk, messagebox
import database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

# --- Theme and Styling (Keep these as module-level for now, or move them into __init__) ---
BG_COLOR = "#2c3e50"
FG_COLOR = "#ecf0f1"
BTN_BG_COLOR = "#3498db"
BTN_FG_COLOR = "white"
INPUT_BG_COLOR = "#34495e"
INPUT_FG_COLOR = "white"
ACCENT_COLOR_SUCCESS = "#2ecc71"
ACCENT_COLOR_DANGER = "#e74c3c"
# FONT_FAMILY = "Arial" # <<< هننقل ده جوه الـ __init__

class FlightApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # --- Define Style Attributes on the instance ---
        self.FONT_FAMILY = "Arial" # Or "Segoe UI"
        self.BG_COLOR = BG_COLOR
        self.FG_COLOR = FG_COLOR
        self.BTN_BG_COLOR = BTN_BG_COLOR
        self.BTN_FG_COLOR = BTN_FG_COLOR
        self.INPUT_BG_COLOR = INPUT_BG_COLOR
        self.INPUT_FG_COLOR = INPUT_FG_COLOR
        self.ACCENT_COLOR_SUCCESS = ACCENT_COLOR_SUCCESS
        self.ACCENT_COLOR_DANGER = ACCENT_COLOR_DANGER
        # --- End Style Attributes ---

        database.init_db()

        self.title("✈️ ZAMILY Flight Reservation System 😈")
        self.geometry("800x650")
        self.configure(bg=self.BG_COLOR) # Use self.BG_COLOR

        # --- Styling using ttk.Style ---
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("TFrame", background=self.BG_COLOR)
        style.configure("TLabel", background=self.BG_COLOR, foreground=self.FG_COLOR, font=(self.FONT_FAMILY, 12))
        style.configure("Title.TLabel", background=self.BG_COLOR, foreground=self.FG_COLOR, font=(self.FONT_FAMILY, 24, "bold"))
        style.configure("Header.TLabel", background=self.BG_COLOR, foreground=self.FG_COLOR, font=(self.FONT_FAMILY, 16, "bold"))

        style.configure("TButton",
                        background=self.BTN_BG_COLOR,
                        # foreground=self.BTN_FG_COLOR, # ttk.Button foreground can be tricky
                        font=(self.FONT_FAMILY, 12, "bold"),
                        padding=10)
                        # relief=tk.RAISED, # ttk buttons handle relief differently
                        # borderwidth=2)
        style.map("TButton",
                  background=[('active', '#2980b9'), ('pressed', '#2980b9')],
                  foreground=[('active', 'white'), ('!disabled', self.BTN_FG_COLOR)]) # Ensure foreground is set

        style.configure("Success.TButton", background=self.ACCENT_COLOR_SUCCESS, foreground=self.BTN_FG_COLOR) # Use BTN_FG_COLOR for consistency
        style.map("Success.TButton", background=[('active', '#27ae60')])
        style.configure("Danger.TButton", background=self.ACCENT_COLOR_DANGER, foreground=self.BTN_FG_COLOR)
        style.map("Danger.TButton", background=[('active', '#c0392b')])

        style.configure("TEntry",
                        fieldbackground=self.INPUT_BG_COLOR,
                        foreground=self.INPUT_FG_COLOR,
                        insertcolor=self.FG_COLOR,
                        font=(self.FONT_FAMILY, 12))

        style.configure("Treeview.Heading", font=(self.FONT_FAMILY, 12, "bold"), background="#5D6D7E", foreground="white")
        style.configure("Treeview",
                        background=self.INPUT_BG_COLOR,
                        foreground=self.FG_COLOR,
                        fieldbackground=self.INPUT_BG_COLOR,
                        font=(self.FONT_FAMILY, 11))
        style.map("Treeview", background=[('selected', self.BTN_BG_COLOR)])

        container = ttk.Frame(self, padding="20 20 20 20")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self) # controller is self (FlightApp instance)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name, data=None):
        frame = self.frames[page_name]
        if data is not None and hasattr(frame, 'load_data'):
            frame.load_data(data)
        elif hasattr(frame, 'refresh_data'):
             frame.refresh_data()
        frame.tkraise()

    # The get_app_style method is now less necessary if styles are defined on self
    # or directly in ttk.Style configurations. But can be kept if you prefer it.
    # def get_app_style(self, widget_type): ... (remove or adapt)

if __name__ == "__main__":
    app = FlightApp()
    app.mainloop()
