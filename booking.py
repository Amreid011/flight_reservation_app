# # flight_reservation_app/booking.py
# import tkinter as tk
# from tkinter import ttk, messagebox
# import database

# class BookingPage(ttk.Frame):
#     def __init__(self, parent, controller):
#         ttk.Frame.__init__(self, parent, style="TFrame")
#         self.controller = controller

#         # --- Form Layout ---
#         form_frame = ttk.Frame(self, padding="20", style="TFrame")
#         form_frame.pack(expand=True, pady=20, padx=20)

#         title_label = ttk.Label(form_frame, text="Book a New Flight", style="Header.TLabel")
#         title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30), sticky="ew")

#         fields = ["Passenger Name:", "Flight Number:", "Departure:", "Destination:", "Date (YYYY-MM-DD):", "Seat Number:"]
#         self.entries = {}

#         for i, field_text in enumerate(fields):
#             label = ttk.Label(form_frame, text=field_text, style="TLabel")
#             label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=10)
#             entry = ttk.Entry(form_frame, width=40, style="TEntry")
#             entry.grid(row=i + 1, column=1, sticky="ew", padx=10, pady=10)
#             self.entries[field_text.split(":")[0].lower().replace(" ", "_").replace("(yyyy-mm-dd)", "").strip()] = entry

#         form_frame.columnconfigure(1, weight=1) # Make entry column expandable

#         # --- Buttons ---
#         button_frame = ttk.Frame(form_frame, style="TFrame")
#         button_frame.grid(row=len(fields) + 1, column=0, columnspan=2, pady=(30, 0), sticky="ew")
#         button_frame.columnconfigure(0, weight=1) # Center buttons
#         button_frame.columnconfigure(1, weight=1)

#         submit_button = ttk.Button(button_frame, text="Submit Reservation", command=self.submit_reservation, style="Success.TButton", width=20)
#         submit_button.grid(row=0, column=0, padx=10, sticky="e")

#         back_button = ttk.Button(button_frame, text="Back to Home",
#                                  command=lambda: controller.show_frame("HomePage"), style="TButton", width=20)
#         back_button.grid(row=0, column=1, padx=10, sticky="w")


#     def submit_reservation(self):
#         values = {key: entry.get() for key, entry in self.entries.items()}

#         # Basic Validation
#         for key, val in values.items():
#             if not val:
#                 messagebox.showerror("Error 😈", f"{key.replace('_', ' ').title()} cannot be empty!")
#                 return

#         try:
#             database.add_reservation(
#                 values['passenger_name'],
#                 values['flight_number'],
#                 values['departure'],
#                 values['destination'],
#                 values['date_'],
#                 values['seat_number']
#             )
#             messagebox.showinfo("Success 🥳", "Flight reservation successful!")
#             for entry in self.entries.values():
#                 entry.delete(0, tk.END) # Clear fields
#             self.controller.show_frame("ReservationsPage") # Go to reservations list
#         except Exception as e:
#             messagebox.showerror("Database Error 😭", f"Failed to add reservation: {e}")

#     def refresh_data(self): # Called when frame is shown
#         for entry in self.entries.values():
#             entry.delete(0, tk.END)


# flight_reservation_app/booking.py
import tkinter as tk
from tkinter import ttk, messagebox
import database

class BookingPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent, style="TFrame")
        self.controller = controller

        # --- Form Layout ---
        form_frame = ttk.Frame(self, padding="20", style="TFrame")
        form_frame.pack(expand=True, pady=20, padx=20)

        title_label = ttk.Label(form_frame, text="Book a New Flight", style="Header.TLabel")
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 30), sticky="ew")

        # تعريف أسماء الحقول والـ keys اللي هنستخدمها ليهم في الـ dictionary
        # ده هيخلي الكود أوضح وأسهل في الصيانة
        self.field_keys = {
            "Passenger Name:": "passenger_name",
            "Flight Number:": "flight_number",
            "Departure:": "departure",
            "Destination:": "destination",
            "Date (YYYY-MM-DD):": "date_value", # هنغير ده عشان يبقى أوضح
            "Seat Number:": "seat_number"
        }
        
        self.entries = {}

        for i, (field_text, field_key) in enumerate(self.field_keys.items()):
            label = ttk.Label(form_frame, text=field_text, style="TLabel")
            label.grid(row=i + 1, column=0, sticky="w", padx=10, pady=10)
            entry = ttk.Entry(form_frame, width=40, style="TEntry")
            entry.grid(row=i + 1, column=1, sticky="ew", padx=10, pady=10)
            self.entries[field_key] = entry # هنستخدم الـ key المعرف مسبقاً

        form_frame.columnconfigure(1, weight=1) # Make entry column expandable

        # --- Buttons ---
        button_frame = ttk.Frame(form_frame, style="TFrame")
        button_frame.grid(row=len(self.field_keys) + 1, column=0, columnspan=2, pady=(30, 0), sticky="ew")
        button_frame.columnconfigure(0, weight=1) 
        button_frame.columnconfigure(1, weight=1)

        submit_button = ttk.Button(button_frame, text="Submit Reservation", command=self.submit_reservation, style="Success.TButton", width=20)
        submit_button.grid(row=0, column=0, padx=10, sticky="e")

        back_button = ttk.Button(button_frame, text="Back to Home",
                                 command=lambda: controller.show_frame("HomePage"), style="TButton", width=20)
        back_button.grid(row=0, column=1, padx=10, sticky="w")


    def submit_reservation(self):
        values = {key: entry.get() for key, entry in self.entries.items()}

        # Basic Validation
        for field_key, val in values.items():
            if not val:
                # نحاول نجيب اسم الحقل من الـ field_keys عشان يبقى اسم مفهوم للمستخدم
                # ده محتاج نعمل mapping عكسي أو نحسن طريقة عرض اسم الحقل
                # للتبسيط الآن، سنستخدم الـ key مباشرة
                display_name = field_key.replace('_', ' ').title()
                if field_key == "date_value": # حالة خاصة لاسم حقل التاريخ
                    display_name = "Date"

                messagebox.showerror("Error 😈", f"{display_name} cannot be empty!")
                return

        try:
            # هنا هنستخدم الـ keys اللي عرفناها فوق
            database.add_reservation(
                values['passenger_name'],
                values['flight_number'],
                values['departure'],
                values['destination'],
                values['date_value'],    # <<< هنا بنستخدم الـ key الجديد 'date_value'
                values['seat_number']
            )
            messagebox.showinfo("Success 🥳", "Flight reservation successful!")
            for entry in self.entries.values():
                entry.delete(0, tk.END) # Clear fields
            self.controller.show_frame("ReservationsPage") # Go to reservations list
        except KeyError as e:
            messagebox.showerror("Programming Error 😈", f"A form field key is missing: {e}. Please check the code logic.")
        except Exception as e:
            messagebox.showerror("Database Error 😭", f"Failed to add reservation: {e}")

    def refresh_data(self): # Called when frame is shown
        for entry in self.entries.values():
            entry.delete(0, tk.END)