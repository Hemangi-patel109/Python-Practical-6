# • Create a list that stores only alphabets from given list.

input_list = ['A', '1', 'b', '#', 'C', '5', '!']

def is_alpha(x): 
    return x.isalpha()
print("Given List: ",input_list)
print("Using filter with a function:")
alphabets = list(filter(is_alpha, input_list))
print(alphabets)  
print("Using filter with lambda")
alphabets = list(filter(lambda x: x.isalpha(), input_list))
print(alphabets)  
print("Using List Comprehension:")
alphabets = [x for x in input_list if x.isalpha()]
print(alphabets)  