import sqlite3
#connecting with databse
conn = sqlite3.connect("emp.db")
# to point a particular location in database
a = conn.cursor()
# to write the sql query
# a.execute("""
#           CREATE TABLE  IF NOT EXISTS employees(
#           id INTEGER PRIMARY KEY,
#           name TEXT NOT NULL,
#           salary INTEGER,
#           dept TEXT
#           )""")

# a.execute(
#  "INSERT INTO employees (id, name, salary, dept) VALUES (?,?,?,?)",
#  (101, "Test User", 30000, "IT")
# )

# emp_data = [
#     (102, "Suraj", 50000, "HR"),
#     (103, "Bhibhu", 60000, "Finance"),
#     (104, "Ankit", 55000, "IT"),
#     (105, "Anuj", 70000, "Marketing"),
#     (106, "Aman", 40000, "Supervisor")
# ]

# a.executemany("INSERT INTO employees (id,name,salary,dept) VALUES (?,?,?,?)", emp_data)


# data = a.execute("SELECT * FROM employees")
# row1 = data.fetchone()
# row2 = data.fetchone()
# print(row1)
# print(row2)

# rows = data.fetchmany(10)
# print(rows)

# rows = data.fetchmany(3)
# print(rows)
a.execute(
    "UPDATE employees SET salary = ?, dept = ? WHERE id = ?",
    (58000, "Finance", 104)
)


conn.commit()


# all_rows = data.fetchall()
# for row in all_rows:
#     print(row)
# # to save the changes on the database

# conn.commit()