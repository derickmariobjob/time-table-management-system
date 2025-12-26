import mysql.connector as sql

# Database Connection (NO PASSWORD)
db = sql.connect(
    host="localhost",
    user="root",
    database="timetable"
)

cursor = db.cursor()

print("\n------ TIME TABLE MANAGEMENT SYSTEM ------\n")
print("1. MR. RAMARAJ")
print("2. MR. MOHAN")
print("3. MR. RAJASEKAR")
print("4. MR. MANIKANDAN")
print("5. MR. VINOTH")

ch = int(input("\nEnter your serial number: "))

def show_timetable(table_name):
    print("\n1. WHOLE WEEK")
    print("2. DAY")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        cursor.execute("SELECT * FROM " + table_name)
        result = cursor.fetchall()
        print("\nSNO  DAY        P1     P2     P3     P4     P5")
        for row in result:
            print(row)

    elif choice == 2:
        print("\n1. MONDAY")
        print("2. TUESDAY")
        print("3. WEDNESDAY")
        print("4. THURSDAY")
        print("5. FRIDAY")
        print("6. SATURDAY")

        day = int(input("Enter your choice: "))
        cursor.execute(
            "SELECT * FROM " + table_name + " WHERE s_no=" + str(day)
        )
        result = cursor.fetchall()
        for row in result:
            print("\nSNO  DAY        P1     P2     P3     P4     P5")
            print(row)

    else:
        print("Invalid choice")

# Menu Mapping
if ch == 1:
    show_timetable("ramaraj")
elif ch == 2:
    show_timetable("mohan")
elif ch == 3:
    show_timetable("rajasekar")
elif ch == 4:
    show_timetable("manikandan")
elif ch == 5:
    show_timetable("vinoth")
else:
    print("Invalid teacher selection")

db.close()
print("\nDatabase connection closed.")
