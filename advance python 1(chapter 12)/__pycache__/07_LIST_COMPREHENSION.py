a = [3,4,6,9,2,24,88,43,78]
# b = []
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)        

b = [i for i in a if i%2==0]
print(b)