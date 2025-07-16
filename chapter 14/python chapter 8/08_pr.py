def remove_and_split(string,word):
    newstr = string.replace(word,"")
    return newstr.strip()

this = "   prem is good    "
n = remove_and_split(this,"prem")
print(n)