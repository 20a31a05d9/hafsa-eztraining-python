a=10

try :
     b=int(input("enter a number:"))
     print("resource open")
     print(a/b)
except ZeroDivisionError as e:    # 0 input la iste vastadi 
    print("num cant be div by 0",e)       #e annadi ekkada system error kuda print avvadniki istaam
except ValueError as e:            # float gani string or char input la iste vastadi 
    print("invalid input",e)
except Exception as e:    #if not any above errors
    print("other error",e)
finally:            # this will excetued if theres an error or not
    print("resource closed ")