#this code answers number 5 of the study drill. "Write it to use for-loops and range."

def Drill(n,y):
    i = 0
    numbers = []
    for integer in range(i, n, y):
        print(f"At the top i is {i}")
        numbers.append(i)

        #"Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?"
        #yes i need the incrementor (i = i + y). If i do not get rid of it, it will help increase the value of i , while i < n
        #but if i remove it, it doesnt increase the vallue of i, meaning the code runs using the given value of i(i = 0)
        
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

