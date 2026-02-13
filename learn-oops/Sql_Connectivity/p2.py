import sqlite3
#connecting with databse
conn = sqlite3.Connection("suy.db")
a = conn.cursor()
a.execute("""
          CREATE TABLE  IF NOT EXISTS employees(
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          salary INTEGER,
          dept TEXT
          )""")

# a.execute(
#  "INSERT INTO employees (id, name, salary, dept) VALUES (?,?,?,?)",
#  (101, "Test User", 30000, "IT")
# )

emp_data = [
    (102, "Suraj", 50000, "HR"),
    (103, "Bhibhu", 60000, "Finance"),
    (104, "Ankit", 55000, "IT"),
    (105, "Anuj", 70000, "Marketing"),
    (106, "Aman", 40000, "Supervisor")
]

a.executemany("INSERT INTO employees (id,name,salary,dept) VALUES (?,?,?,?)", emp_data)


conn.commit()