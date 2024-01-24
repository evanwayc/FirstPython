import csv


def open_csv(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        csv_reader = csv.DictReader(f)
        result = {}
        for row in csv_reader:
            print(row)
            name = row.get("姓名")
            result[name] = row
        print(result)
        return result
