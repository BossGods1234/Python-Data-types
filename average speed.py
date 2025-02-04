a = int(input("Enter a Value"))
b = int(input("Enter Value 2 :"))
c = int(input("Enter Value 3:"))
avg = (a+b+c)/3
print("avg =", avg)
if a < avg:
    print("Speed 1 is slower than average with the difference of", avg-a)
if b < avg:
    print("Speed 2 is slower than average with the difference of", avg-b)
if c < avg:
    print("Speed 3 is slower than average with the difference of", avg-c)