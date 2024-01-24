import csv, json
from encodings import utf_8_sig

def read_csv():
    person_list = []
    try:
        with open("studenter_labb2.csv", "r", encoding="utf-8-sig") as labb2_csv:
            reader = csv.DictReader(labb2_csv)
            for row in reader:
                person_list.append(row)
        print(person_list)
    except FileNotFoundError as ferr:
        print(ferr)

    with open('studenter_labb2.json.py','w',encoding='utf-8') as f_obj:
        json.dump(person_list, f_obj, ensure_ascii=False, indent= 4)
    print("Sparande till json fil lyckades.")


