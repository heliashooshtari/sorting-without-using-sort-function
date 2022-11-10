#tamrin5
list=input('numbers:'). strip(). split(' ')
# A=list(A)
new_list = []

while list:
    minimum = list[0]  # arbitrary number in list 
    for x in list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    list.remove(minimum)    

print (new_list)