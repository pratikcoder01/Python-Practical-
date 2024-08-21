# Dictionary Operations in Python

def create_dictionary():
    # Creating a dictionary
    my_dict = {
        'name': 'Pratik',
        'age': 17,
        'course': 'Electronics and Telecommunication',
        'year': 2
    }
    print("Dictionary Created: ", my_dict)
    return my_dict

def access_dictionary(my_dict):
    # Accessing elements from a dictionary
    print("Accessing Elements:")
    print("Name:", my_dict['name'])
    print("Age:", my_dict['age'])
    print("Course:", my_dict.get('course'))  # Using get() method

def update_dictionary(my_dict):
    # Updating dictionary elements
    print("\nUpdating Dictionary:")
    my_dict['age'] = 21  # Updating existing value
    my_dict['college'] = 'Athskur Polytechnic'  # Adding a new key-value pair
    print("Updated Dictionary: ", my_dict)

def delete_dictionary_element(my_dict):
    # Deleting elements from a dictionary
    print("\nDeleting Elements:")
    my_dict.pop('year')  # Deleting using pop()
    print("Dictionary after deletion: ", my_dict)
    del my_dict['college']  # Deleting using del keyword
    print("Dictionary after another deletion: ", my_dict)

def loop_through_dictionary(my_dict):
    # Looping through a dictionary
    print("\nLooping through Dictionary:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")

# Main Program
if __name__ == "__main__":
    # Create a dictionary
    my_dict = create_dictionary()

    # Access dictionary elements
    access_dictionary(my_dict)

    # Update dictionary elements
    update_dictionary(my_dict)

    # Delete dictionary elements
    delete_dictionary_element(my_dict)

    # Loop through the dictionary
    loop_through_dictionary(my_dict)
#made by pratik dnyaneshwar nagrale  