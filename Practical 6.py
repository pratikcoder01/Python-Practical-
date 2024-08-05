def list_operations_demo():
    # a) Create a list
    my_list = [10, 20, 30, 40, 50]
    print("Original list:", my_list)
    
    # b) Access elements from the list
    print("\nAccessing elements:")
    print("First element:", my_list[0])
    print("Last element:", my_list[-1])
    print("Elements from index 1 to 3:", my_list[1:4])
    
    # c) Update elements in the list
    print("\nUpdating elements:")
    my_list[2] = 100  # Update the third element
    print("Updated list:", my_list)
    
    # d) Delete elements from the list
    print("\nDeleting elements:")
    del my_list[1]  # Delete the second element
    print("List after deleting the second element:", my_list)
    
    my_list.remove(100)  # Remove the element with value 100
    print("List after removing element with value 100:", my_list)
    
    # Optionally, pop an element (removes the last element by default)
    popped_element = my_list.pop()
    print("Popped element:", popped_element)
    print("List after popping the last element:", my_list)

list_operations_demo()
