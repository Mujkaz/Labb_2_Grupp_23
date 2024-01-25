import csv, json
from encodings import utf_8_sig
# Läser CSV till JSON.
def read_csv():
    person_list = []
    # Öppnar "Studenter_labb2.csv" i läsläge.
    try:
        with open("studenter_labb2.csv", "r", encoding="utf-8-sig") as labb2_csv:
            reader = csv.DictReader(labb2_csv)
            for row in reader:
                person_list.append(row)
        print(person_list)
        # Felmeddelande om filen inte finns eller om filen inte går att hitta.
    except FileNotFoundError as ferr:
        print(ferr)
    # Öppnar "studenter_labb2.json.py" i skrivarläge, där man dumpar ner all information man lagt till -
    # - I person_list.
    with open('studenter_labb2.json.py','w',encoding='utf-8') as f_obj:
        json.dump(person_list, f_obj, ensure_ascii=False, indent= 4)
    print("Sparande till json fil lyckades.")


