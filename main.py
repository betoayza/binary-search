# Binary Search is a mechanism which allows compare middle number with a list
# If middle number is > searched focus lef sublist
# if middle < searched focus rigth sublist
# Keeps spliting until get the number

def binary_search(the_list, searched_number):
    global is_found
    global position

    if len(the_list) and not is_found:
        index_middle = len(the_list) // 2       

        if the_list[index_middle] == searched_number:            
            position = ordered_list.index(the_list[index_middle])
            is_found = True

        elif len(the_list) > 1:
            if the_list[index_middle] > searched_number:
                sub_list_1 = the_list[0:index_middle]
                binary_search(sub_list_1, searched_number)
            elif the_list[index_middle] < searched_number:
                sub_list_2 = the_list[index_middle+1:]
                binary_search(sub_list_2, searched_number)

    return is_found

# -----
print("\nWellcome to Binary Search")

# initial variables
position = None
is_found = False
is_running = True
is_list_completed = False
is_tam_defined = False
list_tam = 0
the_list = []
ordered_list = []

# Preparations
while is_running and not is_list_completed:
    try:        
        if not is_tam_defined:
            list_tam = int(input("\nEnter list tam: "))
            is_tam_defined = True

        while len(the_list) < list_tam:
            new_number = int(input("Add a number to the list: "))
            the_list.append(new_number)

        is_list_completed = True
        is_running = False
    except ValueError:
        print("You must enter a just a number...")

# updated variables
ordered_list = sorted(the_list)
print("\nThe list is:", ordered_list)
find = int(input("\nEnter the number to find: "))        
is_found = binary_search(ordered_list, find)

# result
if is_found:
    print("\nNumber found in position:", position,"!")
else:
    print("\nNumber not found :(")

# exit
print("\nThanks for trying.")
