# ✈️ ZAMILY Flight Reservation System 😈

A **desktop application** for managing flight reservations, built with **Python**, **Tkinter**, and **SQLite**.
Book flights, view reservations, update details, and delete bookings—all in a **user-friendly interface** with a creative touch! 😉

![Project Screenshot](photo_proj.png)

---

## 🌟 Features

* 🛫 **Book New Flights** – Add passengers and flight details.
* 📋 **View Reservations** – Display all bookings in a neat table.
* ✏️ **Edit/Update Reservations** – Modify passenger info or flight details.
* ❌ **Delete Reservations** – Remove unwanted bookings.
* 🖥 **User-Friendly GUI** – Clean and intuitive interface.
* 💾 **SQLite Database** – Stores all reservation details securely.

---

## 🛠 Technologies Used

* **Python 3.x**
* **Tkinter** – GUI framework
* **SQLite3** – Database management
* **PyInstaller (Optional)** – Create a standalone `.exe`
* **GitHub** – Version control

---

## 💾 Installation & Running the App

1. Clone the repository:

```bash
git clone <repository_url>
cd flight_reservation_app
```

2. Make sure Python 3 is installed.

3. Run the application:

```bash
python main.py
```

> The `flights.db` database will be created automatically if it doesn’t exist.

---

## 🏗 How to Build Executable (Optional)

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run PyInstaller:

```bash
pyinstaller --onefile --windowed --name FlightZAMILY main.py
```

* `--onefile` → Creates a single executable
* `--windowed` → No console window
* `--name FlightZAMILY` → Sets the name of the `.exe`

The executable will appear in the `dist/` folder.

---

## 📂 Project Structure

```
/flight_reservation_app
├── main.py               # Main application entry point
├── database.py           # SQLite database connection and CRUD operations
├── home.py               # Home page UI
├── booking.py            # Flight booking form UI
├── reservations.py       # View all reservations UI
├── edit_reservation.py   # Update/Delete functionality UI
├── flights.db            # SQLite database file
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── demo.mp4              # Demo video of the app
├── photo_proj.png        # Project screenshot
├── Attachment.pdf        # Additional project attachment
└── __pycache__/          # Python cache files
```

---

## 🎬 Demo Video

[Watch Demo](demo.mp4)

---

## 🏆 Author

**Amr Eid – ZAMILY Team**

---

## 🔖 Badges

![Python](https://img.shields.io/badge/Python-3776AB?style=flat\&logo=python\&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6F00?style=flat)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat)
![PyInstaller](https://img.shields.io/badge/PyInstaller-EE2C2C?style=flat)
