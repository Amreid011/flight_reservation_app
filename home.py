# flight_reservation_app/home.py
import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, style="TFrame")
        self.controller = controller

        label = ttk.Label(self, text="✈️ ZAMILY Flight Reservations ✈️", style="Title.TLabel")
        label.pack(pady=(50, 30)) # More padding at top

        sub_label = ttk.Label(self, text="Your Ultimate Booking Partner! 😈", font=(controller.FONT_FAMILY, 16, "italic"))
        sub_label.pack(pady=(0, 50))


        btn_book_flight = ttk.Button(self, text="Book New Flight",
                                      command=lambda: controller.show_frame("BookingPage"),
                                      style="TButton", width=25)
        btn_book_flight.pack(pady=15)

        btn_view_reservations = ttk.Button(self, text="View All Reservations",
                                           command=lambda: controller.show_frame("ReservationsPage"),
                                           style="TButton", width=25)
        btn_view_reservations.pack(pady=15)

        btn_exit = ttk.Button(self, text="Exit Application",
                              command=self.controller.quit,
                              style="Danger.TButton", width=25)
        btn_exit.pack(pady=(30,15))