# flight_reservation_app/README.md

# ✈️ ZAMILY Flight Reservation System 😈

A simple desktop application for managing flight reservations, built with Python, Tkinter for the GUI, and SQLite for database management.

## Features

*   Book new flight reservations.
*   View a list of all existing reservations.
*   Update details of existing reservations.
*   Delete reservations.
*   User-friendly interface with a "creative" and "awesome" touch by ZAMILY! 😉

## Project Structure

/flight_reservation_app
├── main.py # Main application entry point
├── database.py # SQLite database connection and CRUD operations
├── home.py # Home page UI
├── booking.py # Flight booking form UI
├── reservations.py # View all reservations UI
├── edit_reservation.py # Update/Delete functionality UI
├── flights.db # SQLite database file (created on first run)
├── requirements.txt # Required Python libraries (mainly for building)
├── README.md # This file
└── .gitignore # Specifies intentionally untracked files that Git should ignore


## Tools Used

*   **Python 3.x**
*   **Tkinter** (for GUI)
*   **SQLite3** (for database)
*   **GitHub** (for version control - you're looking at it!)
*   **(Optional) PyInstaller** (for creating a standalone executable)


## How to Run

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <repository_url>
    cd flight_reservation_app
    ```
2.  **Ensure Python 3 is installed.**
3.  **Run the main application file:**
    ```bash
    python main.py
    ```
    The `flights.db` database file will be created automatically in the same directory if it doesn't exist.

## How to Build Executable (Optional)

1.  **Install PyInstaller:**
    ```bash
    pip install pyinstaller
    ```
2.  **Navigate to the project directory in your terminal.**
3.  **Run PyInstaller:**
    ```bash
    pyinstaller --onefile --windowed --name FlightZAMILY main.py
    ```
    *   `--onefile`: Creates a single executable file.
    *   `--windowed`: Prevents the console window from appearing when the GUI app runs.
    *   `--name FlightZAMILY`: Sets the name of the executable.
    *   You can also add `--icon=path/to/your/icon.ico` if you have an icon file.

    The executable will be found in the `dist` folder created by PyInstaller.

## 😈 Brought to you by the ZAMILY Team! 😈
