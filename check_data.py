import sqlite3

def check_data():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    print("Employees Table Data:")
    cursor.execute("SELECT * FROM Employees")
    for row in cursor.fetchall():
        print(row)
    
    print("\nDepartments Table Data:")
    cursor.execute("SELECT * FROM Departments")
    for row in cursor.fetchall():
        print(row)
    
    conn.close()

if __name__ == "__main__":
    check_data()