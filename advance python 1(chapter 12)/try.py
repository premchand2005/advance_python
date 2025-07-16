while(True):
    print("press q to quit")
    a = input("Enter the number:")
    if a == 'q':
        break
    try:
        print("Typing......")
        a = int(a)
        if a>6:
            print("you entered a number greater than 6")
    except Exception as e:
        print(f"your input resulted in an error : {e}")
print("Thanks for playing game....")        