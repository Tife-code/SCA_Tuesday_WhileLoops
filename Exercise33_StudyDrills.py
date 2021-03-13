#this code answers numbers 1-4 of the study drill, exercise 33.

def Drill(n,y):
    i = 0
    numbers = []
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

enter = int(input("Enter a number: "))
increment = int(input("By how much do you want it to increment/increase? "))   
run = Drill(enter, increment)
print(run)

