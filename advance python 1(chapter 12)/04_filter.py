def greater_than_5(num):
    if num>5:
        return True
    else:
        return False
l = [1,2,3,4,5,6,7,8,9,87,65,4,5,23,21,32,43,23]
print(list(filter(greater_than_5,l)))    