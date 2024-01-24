import json, csv
def json_csv():
    with open("studenter_labb2.json.py", "r", encoding="utf-8-sig") as labb2_json:
        person_data = json.load(labb2_json)

    with open("studenter_labb2.csv", 'w', newline = '', encoding = "utf-8-sig") as csvfil:
        csv_writer = csv.writer(csvfil)
        header = list(person_data[0].keys())
        csv_writer.writerow(header)
        for row in person_data:
            csv_writer.writerow(row.values())
    print("Sparande till csv fil lyckades.")
