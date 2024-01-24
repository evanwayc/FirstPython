def get_user_command():
    command_list = ["list", "add", "edit", "delete", "exit"]
    command = input("請輸入命令: ")
    if command not in command_list:
        print("命令錯誤")
    else:
        return command
