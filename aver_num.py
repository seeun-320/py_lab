#!/usr/bin/python3

num = int(input("Input N : "))

sum=0

for i in range(num):
	temp=int(input())
	sum+=temp

avg=sum/num
print(avg)
