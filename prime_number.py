num = int(input("Enter a number: "))

if num < 2:
    print("Non-Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Non-Prime Number")
            break
    else:
        print("Valid Prime Number")
