ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list .Let's fix that")

#通过指定分隔符对字符串进行切片
stuff = ten_things.split(" ")
more_suff = ["Day","Night","Song","Feisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	next_one = more_suff.pop()
	print("Adding:",next_one)
	stuff.append(next_one)
	print("There are %d items now." % len(stuff))
	
print("There we go:",stuff)

print("Let't do some things with stuff")

print(stuff[1])
print(stuff[-1]) #whoa fancy
#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
print(stuff.pop())
print(' '.join(stuff)) #what cool
#使用#号连接基数为3和4的值
print('#'.join(stuff[3:5])) #super stellar
