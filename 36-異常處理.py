# try:
#     可能產生異常的部分
# except:
#     如果發生了就運行這部分

import os
os.system('cls' if os.name == 'nt' else 'clear')


try:
    num = int(input('請輸入數字：'))
    res = 10 / num
    print(res)
except:
    print('有錯誤')
else:
    print('沒有錯誤')
