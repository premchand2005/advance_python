# bina function ka problem
marks1 = [45,56,34,54]
percentage1 = (sum(marks1)/400)*100

marks2 = [34,66,43,23]
percentage2 = (sum(marks2)/400)*100
print(percentage1 , percentage2)        

# jab ham function ko use katre hai tab
def percent(marks):
    return((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
marks1 = [45,56,34,54]
percentage1 = percent(marks1)
marks2 = [34,57,43,23]
percentage2 = percent(marks2)
print(percentage1 , percentage2)