with open ( 'D:\小滔\python\data3.txt', 'w') as f:
    s = input()
    f.write(s)
    f.close()
with open ('D:\小滔\python\data.txt', 'w') as f:
    f.seek(0,2)
    s = input()
    f.writelines(s)
    f.close()

with open ('D:\小滔\python\data.txt', 'r') as f:
    c = f.read() #读出全部内容
    f.close()
    print(c)
with open ('D:\小滔\python\data3.txt', 'r') as f:
    a = f.read(2) #读出两字节
print(a)