# flight_reservation_app/reservations.py
import tkinter as tk
from tkinter import ttk, messagebox
import database

class ReservationsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, style="TFrame")
        self.controller = controller

        title_label = ttk.Label(self, text="All Flight Reservations", style="Header.TLabel")
        title_label.pack(pady=(20, 10))

        # --- Treeview for displaying reservations ---
        columns = ("id", "name", "flight_no", "departure", "destination", "date", "seat")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", style="Treeview", height=15)

        # Define headings
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Passenger")
        self.tree.heading("flight_no", text="Flight No.")
        self.tree.heading("departure", text="Departure")
        self.tree.heading("destination", text="Destination")
        self.tree.heading("date", text="Date")
        self.tree.heading("seat", text="Seat")

        # Define column widths (adjust as needed)
        self.tree.column("id", width=50, anchor=tk.CENTER)
        self.tree.column("name", width=150)
        self.tree.column("flight_no", width=100, anchor=tk.CENTER)
        self.tree.column("departure", width=120)
        self.tree.column("destination", width=120)
        self.tree.column("date", width=100, anchor=tk.CENTER)
        self.tree.column("seat", width=80, anchor=tk.CENTER)

        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # --- Scrollbar for Treeview ---
        scrollbar = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")


        # --- Buttons ---
        button_frame = ttk.Frame(self, style="TFrame")
        button_frame.pack(pady=(10,20), fill="x", padx=20)

        edit_button = ttk.Button(button_frame, text="Edit Selected", command=self.edit_selected, style="TButton", width=15)
        edit_button.pack(side=tk.LEFT, padx=10)

        delete_button = ttk.Button(button_frame, text="Delete Selected", command=self.delete_selected, style="Danger.TButton", width=15)
        delete_button.pack(side=tk.LEFT, padx=10)

        refresh_button = ttk.Button(button_frame, text="Refresh List", command=self.refresh_data, style="TButton", width=15)
        refresh_button.pack(side=tk.LEFT, padx=10)
        
        back_button = ttk.Button(button_frame, text="Back to Home",
                                 command=lambda: controller.show_frame("HomePage"), style="TButton", width=15)
        back_button.pack(side=tk.RIGHT, padx=10)


        self.refresh_data()

    def refresh_data(self):
        # Clear existing items in the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Fetch new data
        reservations = database.get_all_reservations()
        for res in reservations:
            self.tree.insert("", tk.END, values=(res['id'], res['name'], res['flight_number'],
                                                res['departure'], res['destination'], res['date'],
                                                res['seat_number']))

    def get_selected_reservation_id(self):
        selected_item = self.tree.focus() # Get selected item
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a reservation from the list first. 😈")
            return None
        item_details = self.tree.item(selected_item)
        return item_details['values'][0] # ID is the first value

    def edit_selected(self):
        reservation_id = self.get_selected_reservation_id()
        if reservation_id:
            self.controller.show_frame("EditReservationPage", data=reservation_id)

    def delete_selected(self):
        reservation_id = self.get_selected_reservation_id()
        if reservation_id:
            res_details = database.get_reservation_by_id(reservation_id)
            passenger_name = res_details['name'] if res_details else "this reservation"
            
            confirm = messagebox.askyesno("Confirm Delete 😈",
                                          f"Are you sure you want to delete the reservation for '{passenger_name}' (ID: {reservation_id})?")
            if confirm:
                try:
                    database.delete_reservation(reservation_id)
                    messagebox.showinfo("Deleted 👍", f"Reservation ID {reservation_id} deleted successfully.")
                    self.refresh_data()
                except Exception as e:
                    messagebox.showerror("Error 😭", f"Failed to delete reservation: {e}")