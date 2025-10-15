# flight_reservation_app/database.py
import sqlite3

DB_NAME = 'flights.db'

def get_db_connection():
    """إنشاء اتصال بقاعدة البيانات"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # للوصول للحقول بالاسم
    return conn

def init_db():
    """إنشاء جدول الحجوزات إذا لم يكن موجودًا"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_reservation(name, flight_no, dep, dest, date, seat):
    """إضافة حجز جديد"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, flight_no, dep, dest, date, seat))
    conn.commit()
    conn.close()

def get_all_reservations():
    """الحصول على كل الحجوزات"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations ORDER BY id DESC")
    reservations = cursor.fetchall()
    conn.close()
    return reservations

def get_reservation_by_id(reservation_id):
    """الحصول على حجز معين بواسطة الـ ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations WHERE id = ?", (reservation_id,))
    reservation = cursor.fetchone()
    conn.close()
    return reservation

def update_reservation(res_id, name, flight_no, dep, dest, date, seat):
    """تحديث حجز موجود"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    ''', (name, flight_no, dep, dest, date, seat, res_id))
    conn.commit()
    conn.close()

def delete_reservation(reservation_id):
    """حذف حجز"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
    conn.commit()
    conn.close()

# Initialize the database and table when this module is imported
if __name__ == '__main__':
    init_db()
    print(f"Database '{DB_NAME}' initialized and 'reservations' table created if not exists.")
    # Test adding a reservation
    # add_reservation("Test User", "TU123", "Cairo", "Dubai", "2024-12-31", "1A")
    # print(get_all_reservations())