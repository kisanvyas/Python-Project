def cube(number):
    return number*number*number

print("Enter number for cubic find cubic ")
num = int(input())
while (num>0):
    print(cube(num))
    x = cube(num)
    if x>100:
        print("cubic is large")
        break
    else :
        print("cubic is small")
        for i in range(x):
            print(x)
            break


