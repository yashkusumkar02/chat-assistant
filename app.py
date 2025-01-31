from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__, template_folder="frontend", static_folder="frontend")


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
    """)
    
    cursor.execute("INSERT OR IGNORE INTO Employees VALUES (1, 'Alice', 'Sales', 50000, '2021-01-15')")
    cursor.execute("INSERT OR IGNORE INTO Employees VALUES (2, 'Bob', 'Engineering', 70000, '2020-06-10')")
    cursor.execute("INSERT OR IGNORE INTO Employees VALUES (3, 'Charlie', 'Marketing', 60000, '2022-03-20')")
    cursor.execute("INSERT OR IGNORE INTO Departments VALUES (1, 'Sales', 'Alice')")
    cursor.execute("INSERT OR IGNORE INTO Departments VALUES (2, 'Engineering', 'Bob')")
    cursor.execute("INSERT OR IGNORE INTO Departments VALUES (3, 'Marketing', 'Charlie')")

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    user_query = request.json.get("query", "").lower()
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    response = "I don't understand that query."
    try:
        if "employees in" in user_query:
            dept = user_query.split("in")[-1].strip().replace("the", "").replace("department", "").strip(" .").capitalize()
            print(f"Extracted Department: '{dept}'")  
            cursor.execute("SELECT Name FROM Employees WHERE Department = ?", (dept,))
            result = cursor.fetchall()
            response = ", ".join([row[0] for row in result]) or "No employees found."
        elif "manager of" in user_query:
            dept = (
                user_query.split("of")[-1]
                .strip()                          
                .replace("the", "")               
                .replace("department", "")        
                .strip(" ?.")                     
                .capitalize()                     
            )
            print(f"Extracted Department for Manager Query: '{dept}'")  
            cursor.execute("SELECT Manager FROM Departments WHERE LOWER(Name) = LOWER(?)", (dept,))
            result = cursor.fetchone()         
            print(f"SQL Query Result for Manager of '{dept}': {result}")  
            response = result[0] if result else "No manager found."
        elif "hired after" in user_query:
            date = user_query.split("after")[-1].strip()
            cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (date,))
            result = cursor.fetchall()
            response = ", ".join([row[0] for row in result]) or "No employees found."
        elif "total salary expense for" in user_query:
            dept = (
                user_query.split("for")[-1]
                .strip()                          
                .replace("the", "")               
                .replace("department", "")        
                .strip(" ?.")                     
                .capitalize()                    
            )
            print(f"Extracted Department: '{dept}'") 
            if not dept:
                response = "Please specify the department name to calculate the total salary expense."
            else:
                cursor.execute("SELECT SUM(Salary) FROM Employees WHERE LOWER(Department) = LOWER(?)", (dept,))
                result = cursor.fetchone()
                print(f"SQL Query Result for '{dept}': {result}")  
                response = f"Total salary expense: {result[0]}" if result and result[0] else "No data found for the specified department."

    except Exception as e:
        print(f"Error: {e}")
        response = "An error occurred while processing your query."

    conn.close()
    return jsonify({"response": response})

if __name__ == "__main__":
    if not os.path.exists("database.db"):
        init_db()
    app.run(debug=True)
