import json, csv
def json_csv():
    # öppnar json filen och enbart läser den.
    with open("studenter_labb2.json.py", "r", encoding="utf-8-sig") as labb2_json:
        person_data = json.load(labb2_json)
    # öppnar .csv fil och sedan skriver över all information som finns i json till .csv.
    # Ta in list och sedan skapar nya rader i .csv tack vore for loop som lägger till nya rader.
    with open("studenter_labb2.csv", 'w', newline = '', encoding = "utf-8-sig") as csvfil:
        # csv_writer som skriver in i CSV, lägger in header för användarnamn, förnamn, efternamn. (Keys)
        # sedan skriver den ut alla values (förnamn, efternamn, användarnamn).
        csv_writer = csv.writer(csvfil)
        header = list(person_data[0].keys())
        csv_writer.writerow(header)
        for row in person_data:
            csv_writer.writerow(row.values())
    print("Sparande till csv fil lyckades.")
