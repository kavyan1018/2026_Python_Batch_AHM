# count total no of notes in given amount - 1552
# 	500 - 3
# 	200-0
# 	100-0
# 	50 - 1
# 	10-0
# 	5-0
# 	1 - 2


amount = int(input("Enter the amount: "))

temp = amount

n500 = temp // 500      # -> 1552 ->  3    -> rem : 52
temp = temp % 500      # -> remd


n200 = temp // 200
temp = temp % 200

n100 = temp // 100
temp = temp % 100

n50 = temp // 50
temp = temp % 50

n10 = temp // 10
temp = temp % 10

n5 = temp // 5
temp = temp % 5

n2 = temp // 2
temp = temp % 2

n1 = temp // 1
temp = temp % 1


total = n500 + n200 + n100 + n50 + n10 + n5 + n2 + n1


print("500 - ", n500)
print("200 - ", n200)
print("100 - ", n100)
print("50 - ", n50)
print("10 - ", n10)
print("5 - ", n5)
print("2 - ", n2)
print("1 - ", n1)

print("Total notes: ", total)