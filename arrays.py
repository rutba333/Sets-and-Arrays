import array as arr
#create an array
array_num=arr.array('i',[1,3,5,3,7,9,3])
print("Original array:"+str(array_num))
#count the numbers of occurences
print("Number of occurences of the number 3 in the said array:"+str(array_num.count(3)))
#reverse the array
array_num.reverse()
print("reverse the orderd of the items:")
print(str(array_num))