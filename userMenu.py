import csv_to_json
import json_to_csv
import person_manager


def menu_choice():
    # Visuell meny alternativ för användaren.
    print("[1]  Hämta CSV data och spara till json fil.")
    print("[2]  Lägg till person i json fil.")
    print("[3]  Ta bort person i json fil.")
    print("[4]  Visa data som är sparad i json fil.")
    print("[5]  Spara data till csv fil.")
    print("[6]  Avsluta program.")


# Användarens alternativ är mellan 1-6.
def menu_select(choice):
    if choice == 1:
        csv_to_json.read_csv()
    elif choice == 2:
        person_manager.add_person()
    elif choice == 3:
        person_manager.remove_person()
    elif choice == 4:
        person_manager.show_person()
    elif choice == 5:
        json_to_csv.json_csv()
    elif choice == 6:
        exit()
    else:
        print("Ogiltigt val, var vänlig ange rätt alternativ.")

# Funktion som letar efter vilket val det är som användaren har skrivit in. Kopplad till funktion menu_operator.
def main():
    while True:
        menu_choice()
        try:
            choice = int(input("Vänligen ange ditt val."))
            menu_select(choice)
        except ValueError:
            print("Ogiltig inmatning.")

# Kontrollerar om python-filen körs direkt eller om den importeras som en modul i ett annat program.
if __name__ == "__main__":
    main()