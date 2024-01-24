from command.command import *
from process.process import *
from process_csv.csv import *


def main():
    path = ".\\41-csv練習\\41.csv"
    result = open_csv(path)

    while True:
        command = get_user_command()
        if command == "exit":
            break
        process_command(command)


if __name__ == "__main__":
    main()
