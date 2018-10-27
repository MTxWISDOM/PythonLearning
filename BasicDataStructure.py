str = 'hello PYTHON' #字符串
alist = [1,2,3,4,5] #列表 可扩展，可以包含不同的元素， 创建列表可以用列表解析
x = 0
llist  = [x for x in range(100) if  x %2 == 0] #100内的偶数 输出[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
aTuple = ('Sunday', 'Happy') #元组，不可变
pList = [('aaa', 'AAA'), ('kkk', 'KKKK')] #由元组构成的列表
print("hello, {0:<10} world".format(33)) #0表示输出序列，：格式，< 表示最对齐数字默认右对齐，10表示占10列其他用空格补充
ainfo = {'mt':1000, 'lhx':2000, 'lyf':3000} #直接创建字典 输出 {'mt': 1000, 'lhx': 2000, 'hlg': 3000}
binfo = dict(ainfo) #用dict函数创建字典，把元组转换为字典
cinfo = {}.fromkeys(('mt','lhx', 'hlg'), 2000)  #输出{'mt': 2000, 'lhx': 2000, 'hlg': 2000} 统一赋值
k = ainfo.keys() #dict_keys(['mt', 'lhx', 'hlg']输出键的值
v = ainfo.values() #dict_values([1000, 2000, 3000]) 输出值
i = ainfo.items() #dict_items([('mt', 1000), ('lhx', 2000), ('hlg', 3000)]) 以元组的方式输出字典内容
for k, v in ainfo.items():
    print(k, v)   #mt 1000
                       #   lhx 2000
                         # hlg 3000 '''

s1 = str.find("hello") #找出字串字符中的位置
s2 = str.find("hello", 4, 7) # 规定位置查找，结果是-1，没找到
s3 = str.lower() #全部变为小写
s4 = str.split(' ') #把字符串按空格节段,以列表返回
s5 = str.replace("helllo", "HELLO") #替换字符
str2 = ["hello", "world"]
s6 = " ".join(str2)  #str2的元素用空格链接
s7 = b'\xe6\x89\x8e\xe5\xbf\x83\xe4\xba\x86\xef\xbc\x8c\xe8\x80\x81\xe9\x93\x81'
s8 = s7.decode() #输出'扎心了，老铁'

blist  = list("hello,python") #输出['h', 'e', 'l', 'l', 'o', ',', 'p', 'y', 'h', 't', 'o', 'n']
alist[0] = 'H' #替换alist中的第一个元素
alist.pop() #弹出最后一个值
alist.pop(0) #弹出索引值所指的元素
alist.append(6) #增加元素
alist.sort() #排序，升序
sorted(alist) #只生成列表的副本，列表本身没有被排序
clist = [7, 8]
alist.extend(clist) #把clist加到alist里面，一个一个元素加 输出[2, 3, 4, 6, 7, 8]
blist.sort(key=len) #按照元素的长度排序

sorted(aTuple) #元组不能用sort()
def foo(args1, *args2):
    print(args1)
    print(args2) # 输出hello
                        #           ('python', 'java', 'c++')  *把剩下的参数全都传给args2，返回一个元组"""
def fpp():
    return 1,2,3  #输出(1, 2, 3)
foo('hello', 'python', 'java', 'c++')
yes = fpp()



