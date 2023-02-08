#without arguments and without return values

def display():
    n=int(input("enter a number:"))
    if n==1:
        display()    #fuc calls itself ,,1 enter chyste malli ade chupistadi 
    else:             #,,other than 1 enter chyste over ani vastadi
        print("over")
display()