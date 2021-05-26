def get_first_unique_item(my_list):
    for element in my_list:
        if my_list.count(element)>1:
            return element
my_list=['a','b','c','c','a']
first_unique_element = get_first_unique_item(my_list)
print(first_unique_element)

