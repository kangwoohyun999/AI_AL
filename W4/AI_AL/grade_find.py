FILENAME = "grade.txt"

def load_grades():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        return [line.strip().split() for line in f]

def save_grades(grades):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for g in grades:
            f.write(' '.join(g) + '\n')
    print("Saved.")

def print_grades(grades):
    print("------------------------------")
    for name, sid, grade in grades:
        print(f"{name}     {sid}     {grade}")
    print("------------------------------")

def search_grade(grades):
    name = input("Search name: ")
    for g in grades:
        if g[0] == name:
            print(f"{g[0]} {g[1]} {g[2]}")
            return
    print("No find name.")

def change_grade(grades):
    name = input("Name: ")
    for g in grades:
        if g[0] == name:
            g[2] = input(f"Grade: ")
            print("Record changed.")
            return
    print("No find student.")

def main():
    grades = load_grades()
    while True:
        cmd = input("\nP: Print all records\nS: Search record\nC: Change record\nW: Write record\nQ: Save and quit\nCommand> ").upper()
        if cmd == 'P': print_grades(grades)
        elif cmd == 'S': search_grade(grades)
        elif cmd == 'C': change_grade(grades)
        elif cmd == 'W': save_grades(grades)
        elif cmd == 'Q':
            print("End."); break
        else: print("Error")

if __name__ == "__main__":
    main()
