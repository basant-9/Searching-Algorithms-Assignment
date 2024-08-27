user_input = list(map(int, input("Enter:").split())) 
user = len(user_input) 
def sec (user_input) :
    if len(user_input)  < 2 :
        return None
    for i in range (0 , user) :
        for x in range (i + 1 , user) :
            if user_input[i] > user_input [x] :
                user_input[i] , user_input[x] = user_input [x] , user_input[i]
    return user_input [-2]
print(sec(user_input))