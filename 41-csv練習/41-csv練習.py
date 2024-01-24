import csv
from command.command import *
from process.process import *

def main():
    f = open(".\\41-csv練習\\41.csv", "r", encoding="utf-8-sig")
    csv_reader = csv.DictReader(f)
    result = {}
    for row in csv_reader:
        print(row)
        name = row.get("姓名")
        result[name] = row
    print(result)

    while True:
        command = get_user_command()
        if command == "exit":
            break
        process_command(command)


if __name__ == "__main__":
    main()
