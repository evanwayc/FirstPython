import csv


def main():
    while True:
        command = get_user_command()
        if command == "exit":
            break
        process_command(command)


def get_user_command():
    command = input("請輸入命令: ")
    return command


if __name__ == '__main__':
    main()