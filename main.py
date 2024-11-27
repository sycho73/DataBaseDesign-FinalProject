import tkinter as tk
from tkinter import messagebox
import mysql.connector

# MySQL 데이터베이스 연결 설정
db_config = {
    'host': 'localhost',
    'user': 'root',  # MySQL 사용자 이름
    'password': '',  # MySQL 비밀번호
    'database': 'databasedesign'   # 생성된 데이터베이스 이름
}

# MySQL 데이터베이스 연결
def connect_to_db():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to the database: {err}")
        return None
# 계정 만들기 함수
def create_account():
    def save_account():
        name = entry_name.get()
        family_name = entry_family_name.get()

        if not name or not family_name:
            messagebox.showerror("Input Error", "All fields must be filled!")
            return

        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "INSERT INTO Users (name, familyname) VALUES (%s, %s)",
                    (name, family_name)
                )
                conn.commit()
                messagebox.showinfo("Success", "Account created successfully!")
                create_account_window.destroy()
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Name must be unique!")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    create_account_window = tk.Toplevel()
    create_account_window.title("Create Account")

    tk.Label(create_account_window, text="Name").pack(pady=5)
    entry_name = tk.Entry(create_account_window)
    entry_name.pack(pady=5)

    tk.Label(create_account_window, text="Family Name").pack(pady=5)
    entry_family_name = tk.Entry(create_account_window)
    entry_family_name.pack(pady=5)

    tk.Button(create_account_window, text="Save", command=save_account).pack(pady=10)


# 고정 수입 입력
def input_fixed_income(user_id):
    def save_fixed_income():
        year = entry_year.get()
        income = entry_income.get()

        if not year.isdigit() or not income.isdigit():
            messagebox.showerror("Input Error", "Year and Income must be numbers!")
            return

        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            try:
                # 기존 데이터 존재 확인
                cursor.execute(
                    "SELECT id FROM Fixedcost WHERE user_id = %s AND year = %s",
                    (user_id, year)
                )
                record = cursor.fetchone()
                if record:
                    # Update
                    cursor.execute(
                        "UPDATE Fixedcost SET fixed_income = %s WHERE id = %s",
                        (income, record[0])
                    )
                else:
                    # Insert
                    cursor.execute(
                        "INSERT INTO Fixedcost (user_id, year, fixed_income) VALUES (%s, %s, %s)",
                        (user_id, year, income)
                    )
                conn.commit()
                messagebox.showinfo("Success", "Fixed income saved successfully!")
                income_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    income_window = tk.Toplevel()
    income_window.title("Input Fixed Income")

    tk.Label(income_window, text="Year").pack(pady=5)
    entry_year = tk.Entry(income_window)
    entry_year.pack(pady=5)

    tk.Label(income_window, text="Fixed Income").pack(pady=5)
    entry_income = tk.Entry(income_window)
    entry_income.pack(pady=5)

    tk.Button(income_window, text="Save", command=save_fixed_income).pack(pady=10)

# 고정 지출 입력
def input_fixed_expense(user_id):
    def save_fixed_expense():
        year = entry_year.get()
        expense = entry_expense.get()

        if not year.isdigit() or not expense.isdigit():
            messagebox.showerror("Input Error", "Year and Expense must be numbers!")
            return

        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            try:
                # 기존 데이터 존재 확인
                cursor.execute(
                    "SELECT id FROM Fixedcost WHERE user_id = %s AND year = %s",
                    (user_id, year)
                )
                record = cursor.fetchone()
                if record:
                    # Update
                    cursor.execute(
                        "UPDATE Fixedcost SET fixed_expense = %s WHERE id = %s",
                        (expense, record[0])
                    )
                else:
                    # Insert
                    cursor.execute(
                        "INSERT INTO Fixedcost (user_id, year, fixed_expense) VALUES (%s, %s, %s)",
                        (user_id, year, expense)
                    )
                conn.commit()
                messagebox.showinfo("Success", "Fixed expense saved successfully!")
                expense_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    expense_window = tk.Toplevel()
    expense_window.title("Input Fixed Expense")

    tk.Label(expense_window, text="Year").pack(pady=5)
    entry_year = tk.Entry(expense_window)
    entry_year.pack(pady=5)

    tk.Label(expense_window, text="Fixed Expense").pack(pady=5)
    entry_expense = tk.Entry(expense_window)
    entry_expense.pack(pady=5)

    tk.Button(expense_window, text="Save", command=save_fixed_expense).pack(pady=10)

# 고정 저축 입력
def input_fixed_saving(user_id):
    def save_fixed_saving():
        year = entry_year.get()
        saving = entry_saving.get()

        if not year.isdigit() or not saving.isdigit():
            messagebox.showerror("Input Error", "Year and Savings must be numbers!")
            return

        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            try:
                # 기존 데이터 존재 확인
                cursor.execute(
                    "SELECT id FROM Fixedcost WHERE user_id = %s AND year = %s",
                    (user_id, year)
                )
                record = cursor.fetchone()
                if record:
                    # Update
                    cursor.execute(
                        "UPDATE Fixedcost SET fixed_saving = %s WHERE id = %s",
                        (saving, record[0])
                    )
                else:
                    # Insert
                    cursor.execute(
                        "INSERT INTO Fixedcost (user_id, year, fixed_saving) VALUES (%s, %s, %s)",
                        (user_id, year, saving)
                    )
                conn.commit()
                messagebox.showinfo("Success", "Fixed saving saved successfully!")
                saving_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    saving_window = tk.Toplevel()
    saving_window.title("Input Fixed Saving")

    tk.Label(saving_window, text="Year").pack(pady=5)
    entry_year = tk.Entry(saving_window)
    entry_year.pack(pady=5)

    tk.Label(saving_window, text="Fixed Saving").pack(pady=5)
    entry_saving = tk.Entry(saving_window)
    entry_saving.pack(pady=5)

    tk.Button(saving_window, text="Save", command=save_fixed_saving).pack(pady=10)

# 메인 화면으로 이동
def main_menu(user_id):
    menu_window = tk.Toplevel()
    menu_window.title("Main Menu")

    tk.Label(menu_window, text="Main Menu", font=("Arial", 16)).pack(pady=20)

    tk.Button(menu_window, text="1. 재산관리", width=20, command=lambda: manage_monthly_assets(user_id)).pack(pady=10)
    tk.Button(menu_window, text="2. 고정수입입력", width=20, command=lambda: input_fixed_income(user_id)).pack(pady=10)
    tk.Button(menu_window, text="3. 고정지출입력", width=20, command=lambda: input_fixed_expense(user_id)).pack(pady=10)
    tk.Button(menu_window, text="4. 고정저축입력", width=20, command=lambda: input_fixed_saving(user_id)).pack(pady=10)
    tk.Button(menu_window, text="5. 구성원 정산", width=20).pack(pady=10)

# 재산관리
def manage_monthly_assets(user_id):
    def save_monthcost():
        year = entry_year.get()
        month = entry_month.get()

        if not year.isdigit() or not month.isdigit() or not (1 <= int(month) <= 12):
            messagebox.showerror("Input Error", "Year and Month must be valid numbers!")
            return

        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            try:
                # 월 데이터 존재 확인
                cursor.execute(
                    "SELECT id FROM Monthcost WHERE user_id = %s AND year = %s AND month = %s",
                    (user_id, year, month)
                )
                record = cursor.fetchone()
                if not record:
                    # Insert
                    cursor.execute(
                        "INSERT INTO Monthcost (user_id, year, month) VALUES (%s, %s, %s)",
                        (user_id, year, month)
                    )
                    conn.commit()
                monthcost_id = record[0] if record else cursor.lastrowid
                # 수정: user_id 추가 전달
                monthly_management_window(user_id, year, month, monthcost_id)
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    asset_window = tk.Toplevel()
    asset_window.title("Manage Monthly Assets")

    tk.Label(asset_window, text="Year").pack(pady=5)
    entry_year = tk.Entry(asset_window)
    entry_year.pack(pady=5)

    tk.Label(asset_window, text="Month (1-12)").pack(pady=5)
    entry_month = tk.Entry(asset_window)
    entry_month.pack(pady=5)

    tk.Button(asset_window, text="Proceed", command=save_monthcost).pack(pady=10)


# 월별 자산 관리
def monthly_management_window(user_id, year, month, monthcost_id):
    def add_income():
        add_transaction("Income", monthcost_id)

    def add_expense():
        add_transaction("Expense", monthcost_id)

    def add_saving():
        add_transaction("Saving", monthcost_id)

    def view_assets():
        conn = connect_to_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                # Fixed Costs
                cursor.execute(
                    "SELECT fixed_income, fixed_expense, fixed_saving FROM Fixedcost WHERE user_id = %s AND year = %s",
                    (user_id, year)
                )
                fixed = cursor.fetchone() or {"fixed_income": 0, "fixed_expense": 0, "fixed_saving": 0}

                # Additional Transactions
                cursor.execute(
                    "SELECT SUM(cost) AS total_income FROM Income WHERE month_id = %s", (monthcost_id,)
                )
                additional_income = cursor.fetchone()["total_income"] or 0

                cursor.execute(
                    "SELECT SUM(cost) AS total_expense FROM Expense WHERE month_id = %s", (monthcost_id,)
                )
                additional_expense = cursor.fetchone()["total_expense"] or 0

                cursor.execute(
                    "SELECT SUM(cost) AS total_saving FROM Saving WHERE month_id = %s", (monthcost_id,)
                )
                additional_saving = cursor.fetchone()["total_saving"] or 0

                # Calculations
                monthly_asset = (
                    fixed["fixed_income"]
                    - fixed["fixed_expense"]
                    - fixed["fixed_saving"]
                    + additional_income
                    - additional_expense
                    - additional_saving
                )
                monthly_saving = fixed["fixed_saving"] + additional_saving

                messagebox.showinfo(
                    "Monthly Assets",
                    f"이번달 자산: {monthly_asset}\n이번달 저축량: {monthly_saving}"
                )
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    # Create the management window
    management_window = tk.Toplevel()
    management_window.title(f"{month}월 자산 관리")

    tk.Label(management_window, text=f"{month}월 자산 관리", font=("Arial", 16)).pack(pady=20)
    tk.Button(management_window, text="1. 추가 수입", width=20, command=add_income).pack(pady=10)
    tk.Button(management_window, text="2. 추가 지출", width=20, command=add_expense).pack(pady=10)
    tk.Button(management_window, text="3. 추가 저축", width=20, command=add_saving).pack(pady=10)
    tk.Button(management_window, text="4. 이번달 자산 확인", width=20, command=view_assets).pack(pady=10)


# 추가 거래 (수입/지출/저축)
def add_transaction(table, monthcost_id, year, month):
    def save_transaction():
        day = entry_day.get()
        cost = entry_cost.get()
        content = entry_content.get()

        if not day.isdigit() or not (1 <= int(day) <= 31):
            messagebox.showerror("Input Error", "Day must be a valid number between 1 and 31!")
            return
        if not cost.isdigit() or not content:
            messagebox.showerror("Input Error", "Please provide valid inputs for all fields!")
            return

        # 날짜 구성: YYYY-MM-DD
        date = f"{year}-{int(month):02d}-{int(day):02d}"

        conn = connect_to_db()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    f"INSERT INTO {table} (month_id, date, cost, content) VALUES (%s, %s, %s, %s)",
                    (monthcost_id, date, cost, content)
                )
                conn.commit()
                messagebox.showinfo("Success", f"{table} added successfully!")
                transaction_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    transaction_window = tk.Toplevel()
    transaction_window.title(f"Add {table}")

    tk.Label(transaction_window, text="Day (1-31)").pack(pady=5)
    entry_day = tk.Entry(transaction_window)
    entry_day.pack(pady=5)

    tk.Label(transaction_window, text="Cost").pack(pady=5)
    entry_cost = tk.Entry(transaction_window)
    entry_cost.pack(pady=5)

    tk.Label(transaction_window, text="Details").pack(pady=5)
    entry_content = tk.Entry(transaction_window)
    entry_content.pack(pady=5)

    tk.Button(transaction_window, text="Save", command=save_transaction).pack(pady=10)



# 로그인 함수
def login():
    def verify_login():
        name = entry_name.get()

        if not name:
            messagebox.showerror("Input Error", "Name must be filled!")
            return

        conn = connect_to_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT id FROM Users WHERE name = %s", (name,))
                user = cursor.fetchone()
                if user:
                    messagebox.showinfo("Login Success", f"Welcome, {name}!")
                    login_window.destroy()
                    main_menu(user['id'])
                else:
                    messagebox.showwarning("Login Failed", "Invalid name!")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    login_window = tk.Toplevel()
    login_window.title("Login")

    tk.Label(login_window, text="Name").pack(pady=5)
    entry_name = tk.Entry(login_window)
    entry_name.pack(pady=5)

    tk.Button(login_window, text="Login", command=verify_login).pack(pady=10)

# 메인 화면
def main_screen():
    root = tk.Tk()
    root.title("User System")

    tk.Label(root, text="Welcome to User System", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Login", command=login, width=15).pack(pady=10)
    tk.Button(root, text="Create Account", command=create_account, width=15).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_screen()
