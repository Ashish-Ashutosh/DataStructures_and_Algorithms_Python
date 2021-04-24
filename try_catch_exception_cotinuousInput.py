#get one input based on 2 validations
while True:
    try:
        weight = input("Please enter your weight: ")
        weight = float(weight)
        #break
    except ValueError:
        print("Not valid weight! Please try again ...")
    try:
        if (weight <= 0):
            print("Enter a positive number")
            raise Exception
        break
    except:
        pass

#get another input based on 2 validations
while True:
    try:
        height = input("Please enter your height: ")
        height = float(height)
        #break
    except ValueError:
        print("Not valid height! Please try again ...")
    try:
        if (height <= 0):
            print("Enter a positive number")
            raise Exception
        break
    except:
        pass

#write rest of the code after validation

















# try:
#     weight = float(input("Enter your weight (in kg only):"))
# except ValueError:
#     print("Enter an integer")
# except


# try:
#  if (weight > 0):
#      raise Exception ("Enter a positive number")
# except:
#     pass


