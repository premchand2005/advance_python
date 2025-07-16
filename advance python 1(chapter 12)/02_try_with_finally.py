try:
    i = int(input("Enter the number:"))
    c = 1/i
    print(c)
except Exception as e:
    print(e)
    exit()
    
finally:
    print("we are done this problem......")