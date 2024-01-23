import csv


def main():
    f = open("41.csv", "r", encoding="utf-8-sig")
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


command_list = ["list", "add", "edit", "delete", "exit"]


def get_user_command():
    command = input("請輸入命令: ")
    if command not in command_list:
        print("命令錯誤")
    else:
        return command


def process_command(command):
    if command == "list":
        process_list()
    elif command == "add":
        process_add()
    elif command == "edit":
        process_edit()
    elif command == "delete":
        process_delete()


def process_list():
    pass


if __name__ == "__main__":
    main()
