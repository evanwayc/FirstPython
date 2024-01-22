import os.path as path #引用os.path模組判斷檔案是否存在

file_var1 = open('sample.txt','w') #寫入檔案
file_var1.write('''\
Hello World
2222222222
3333333333
4444444444
5555555555\
''')
file_var1.close() #關閉檔案

file_var2 = open('sample.txt','r') #讀取檔案
print(file_var2.read()) #讀取檔案內容
file_var2.close() #關閉檔案

with open('sample.txt','r') as file_var3: #讀取檔案
    print(file_var3.readlines()) #讀取檔案內容

print(path.exists('sample.txt')) #判斷檔案是否存在
print(path.exists('sample2.txt')) #判斷檔案是否存在