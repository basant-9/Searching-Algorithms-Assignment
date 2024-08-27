num = [1,2,3,4,5,7]
def missing () :
    for i in range (1,8) :
        if i not in num:
            return i
print(missing()) 