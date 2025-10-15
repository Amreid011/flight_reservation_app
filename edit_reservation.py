# flight_reservation_app/edit_reservation.py
import tkinter as tk
from tkinter import ttk, messagebox
import database

class EditReservationPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, style="TFrame")
        self.controller = controller
        self.reservation_id = None

        form_frame = ttk.Frame(self, padding="20", style="TFrame")
        form_frame.pack(expand=True, pady=20, padx=20)

        title_label = ttk.Label(form_frame, text="Edit Flight Reservation", style="Header.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30), sticky="ew")

        self.fields_map = {
            "name": "Passenger Name:",
            "flight_number": "Flight Number:",
            "departure": "Departure:",
            "destination": "Destination:",
            "date": "Date (YYYY-MM-DD):",
            "seat_number": "Seat Number:"
        }
        self.entries = {}

        row_num = 1
        for key, field_text in self.fields_map.items():
            label = ttk.Label(form_frame, text=field_text, style="TLabel")
            label.grid(row=row_num, column=0, sticky="w", padx=10, pady=10)
            entry = ttk.Entry(form_frame, width=40, style="TEntry")
            entry.grid(row=row_num, column=1, sticky="ew", padx=10, pady=10)
            self.entries[key] = entry
            row_num += 1
        
        form_frame.columnconfigure(1, weight=1)

        # --- Buttons ---
        button_frame = ttk.Frame(form_frame, style="TFrame")
        button_frame.grid(row=row_num, column=0, columnspan=2, pady=(30, 0), sticky="ew")
        button_frame.columnconfigure(0, weight=1) # Center buttons
        button_frame.columnconfigure(1, weight=1)


        update_button = ttk.Button(button_frame, text="Update Reservation", command=self.update_reservation_data, style="Success.TButton", width=20)
        update_button.grid(row=0, column=0, padx=10, sticky="e")

        back_button = ttk.Button(button_frame, text="Back to Reservations",
                                 command=lambda: controller.show_frame("ReservationsPage"), style="TButton", width=20)
        back_button.grid(row=0, column=1, padx=10, sticky="w")


    def load_data(self, reservation_id):
        self.reservation_id = reservation_id
        reservation = database.get_reservation_by_id(self.reservation_id)
        if reservation:
            self.entries['name'].delete(0, tk.END)
            self.entries['name'].insert(0, reservation['name'])
            self.entries['flight_number'].delete(0, tk.END)
            self.entries['flight_number'].insert(0, reservation['flight_number'])
            self.entries['departure'].delete(0, tk.END)
            self.entries['departure'].insert(0, reservation['departure'])
            self.entries['destination'].delete(0, tk.END)
            self.entries['destination'].insert(0, reservation['destination'])
            self.entries['date'].delete(0, tk.END)
            self.entries['date'].insert(0, reservation['date'])
            self.entries['seat_number'].delete(0, tk.END)
            self.entries['seat_number'].insert(0, reservation['seat_number'])
        else:
            messagebox.showerror("Error 😭", f"Could not find reservation with ID: {self.reservation_id}")
            self.controller.show_frame("ReservationsPage")


    def update_reservation_data(self):
        if not self.reservation_id:
            messagebox.showerror("Error 😈", "No reservation selected for update.")
            return

        values = {key: entry.get() for key, entry in self.entries.items()}

        # Basic Validation
        for key, val in values.items():
            if not val:
                messagebox.showerror("Error 😈", f"{self.fields_map[key]} cannot be empty!")
                return
        try:
            database.update_reservation(
                self.reservation_id,
                values['name'],
                values['flight_number'],
                values['departure'],
                values['destination'],
                values['date'],
                values['seat_number']
            )
            messagebox.showinfo("Success ✨", "Reservation updated successfully!")
            self.controller.show_frame("ReservationsPage")
        except Exception as e:
            messagebox.showerror("Database Error 😭", f"Failed to update reservation: {e}")