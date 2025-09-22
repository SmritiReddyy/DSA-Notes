# Eg.1 Find the lowest value in an array 
#  1. create a variable minval and set element at index 0 to minval
#  2. go through every value in array 
#  3. if currentval is lesser than minval, change minval to currentval 
#  4. at the end, minval is the smallest value 

my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]    

for i in my_array:     
    if i < minVal:     
        minVal = i
        
print('Lowest value: ',minVal) 

# This algorithm has time complexity of O(n). 
