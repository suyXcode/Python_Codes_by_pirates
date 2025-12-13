# 🎓 Student Management System (Python OOPs Mini Project)

### 👨‍💻 Developed by [Suyash Singh](https://github.com/SuyXcode)

## 📘 Project Overview

This project demonstrates the core concepts of **Object-Oriented Programming (OOP)** in Python by building a simple yet structured **Student Management System**.

It covers:
- Class & Object creation  
- Class Members & Object Members  
- Instance, Class, and Static Methods  
- OOP Pillars — *Encapsulation, Inheritance, Polymorphism, and Abstraction*  

## 🧠 Concepts Used

| Concept | Description | Implementation Example |
|----------|--------------|------------------------|
| **Class** | Blueprint for creating objects | `class Student:` |
| **Object** | Instance of a class | `s1 = Student("Suyash", 101, 88)` |
| **Class Member** | Shared variable among all objects | `college_name = "KNIPSS College"` |
| **Object Member** | Unique data per object | `self.name`, `self.__marks` |
| **Encapsulation** | Data hiding using private variables | `__marks` + getter/setter |
| **Inheritance** | Reusing parent class properties | `class Topper(Student)` |
| **Polymorphism** | Same method behaves differently | Overridden `show_details()` |
| **Abstraction** | Hiding details using abstract base class | `class Person(ABC)` |
| **Instance Method** | Works on instance data | `def show_details(self):` |
| **Class Method** | Works on class data | `@classmethod` |
| **Static Method** | Independent of both class & instance | `@staticmethod` |

## ⚙️ Project Structure

```
min_pro/
│
├── p0.ipynb    # Main project file
└── README.md                # Documentation file
```

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SuyXcode/learn-oops/mini_pro.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd mini_pro
   ```

3. **Run the Python script:**
   ```bash
   python p0.py
   ```

## 📤 Sample Output

```
🎓 WELCOME TO STUDENT MANAGEMENT SYSTEM 🎓

Name: Suyash, Roll: 101, Marks: 88
Name: Aman, Roll: 102, Marks: 76
🏅 Topper: Riya, Roll: 103, Marks: 95, Award: Gold Medal

🏫 College Name: KNIPSS College

Marks before update: 88
Marks after update: 92

Grade of Suyash: A+
Grade of Aman: A

👩‍🏫 Displaying details using Polymorphism:
Name: Suyash, Roll: 101, Marks: 92
Name: Aman, Roll: 102, Marks: 76
🏅 Topper: Riya, Roll: 103, Marks: 95, Award: Gold Medal
```

## 🏗️ OOP Pillars in Action

| Pillar | Implementation |
|--------|----------------|
| **Encapsulation** | Private marks variable with getter/setter |
| **Inheritance** | `Topper` inherits from `Student` |
| **Polymorphism** | `show_details()` overridden in `Topper` |
| **Abstraction** | `Person` abstract base class defines structure |

## 🧑‍💼 Key Learning Outcomes
- Understand how classes and objects structure programs.
- Learn method types and scope of variables.
- See how OOP pillars improve modularity and security.
- Learn to design scalable and maintainable Python programs.

## 🧾 Future Improvements
- Add student database using **SQLite**.  
- Include file handling for data persistence.  
- Create a GUI using **Tkinter or Flask**.  
- Implement admin login system and marks analysis chart.

## 📚 Tech Stack
- **Language:** Python 3  
- **Paradigm:** Object-Oriented Programming  
- **Tools:** VS Code / PyCharm / IDLE  

## 💬 Connect with Me
**👦 Suyash Singh**  
📧 Email: [suyashsingh@example.com](mailto:suyashsingh@example.com)  
🐙 GitHub: [github.com/SuyXcode](https://github.com/SuyXcode)  
💼 LinkedIn: [linkedin.com/in/suyashsingh](https://linkedin.com/in/suyashsingh)

✨ *Turning learning into creation — one project at a time!* 🚀
