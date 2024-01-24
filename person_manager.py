import json

def add_person():
    try:
        with open("studenter_labb2.json.py", 'r', encoding = "utf_8_sig") as labb2_json:
            person_data = json.load(labb2_json)
    except FileNotFoundError as ferr:
        print(ferr)

    print('Skriv personens uppgifter du vill lägga till.')
    print("Ange efternamn:")
    last_name = input()
    print("Ange förnamn:")
    first_name = input()
    print("Ange användarnamn:")
    user_name = input()
    new_user = {"Förnamn": first_name, "Efternamn": last_name, "Användarnamn": user_name}

    with open ("studenter_labb2.json.py", "w", encoding = "utf-8-sig") as labb2_json:
        person_data.append(new_user)
        json.dump(person_data, labb2_json, ensure_ascii=False, indent=4)
        print("Lyckad inläggning av ny användare.")
def remove_person():
        try:
            with open ("studenter_labb2.json.py", "r", encoding = "utf-8-sig") as labb2_json:
                person_data = json.load(labb2_json)
                for index, value in enumerate(person_data):
                    print(index,value)

                print("Ange siffra för den person du vill ta bort.")
                delete_user = int(input())
                try:
                    person_data.pop(delete_user)
                    print(f"Du lyckades ta bort användare på index: {delete_user}")
                except IndexError:
                    print("Indexvärdet är inte tillgängligt i listan.")
                except TypeError:
                    print('Du måste ange en siffra.')
        except FileNotFoundError as ferr:
            print(ferr)

        with open("studenter_labb2.json.py", "w", encoding ="utf_8_sig ") as labb2_json:
            json.dump(person_data, labb2_json, ensure_ascii=False, indent=4)

def show_person():
        with open ("studenter_labb2.json.py", "r", encoding = "utf-8-sig") as labb2_json:
            person_data = json.load(labb2_json)
            format_data = json.dumps(person_data, ensure_ascii=False, indent = 4)
            print(format_data)

