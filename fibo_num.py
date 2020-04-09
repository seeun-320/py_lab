#!/usr/bin/python3

num=int(input("fibonacci number? "))
list = [0, 1]
for i in range(2,num+1, 1):
	list.append(int(list[i-1]) + int(list[i-2]))

for i in range(1, num):
	print(list[i], end = "")
	print(", ", end = "")
print(list[num])

print("F%d = %d"%(num,list[num]))
