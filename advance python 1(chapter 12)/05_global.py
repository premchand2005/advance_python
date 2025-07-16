a = 34
def func1():
    a = 9
    print(f"this is called a local variable : {a}")
func1()    
print(f"this is called a global variable : {a}")