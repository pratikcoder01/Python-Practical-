import numpy as np  # Import the NumPy package

def create_arrays():
    print("Creating NumPy Arrays:")
    
    # Creating a 1D array
    array_1d = np.array([1, 2, 3, 4, 5])
    print("1D array:", array_1d)
    
    # Creating a 2D array
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("2D array:\n", array_2d)
    
    # Creating an array with zeros
    zeros_array = np.zeros((3, 3))
    print("Array of zeros:\n", zeros_array)
    
    # Creating an array with ones
    ones_array = np.ones((2, 4))
    print("Array of ones:\n", ones_array)
    
    # Creating an array with a range of values
    range_array = np.arange(10, 21)
    print("Array with a range of values:", range_array)
    
    # Creating an array with evenly spaced values
    linspace_array = np.linspace(0, 1, 5)
    print("Array with evenly spaced values:", linspace_array)
    
    print()

def access_array_elements():
    print("Accessing Array Elements:")
    
    # Creating a sample 2D array
    array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
    print("2D array:\n", array_2d)
    
    # Accessing a single element
    single_element = array_2d[1, 2]  # Accessing element at row 2, column 3
    print("Element at row 2, column 3:", single_element)
    
    # Accessing a row
    row = array_2d[1, :]
    print("Second row:", row)
    
    # Accessing a column
    column = array_2d[:, 1]
    print("Second column:", column)
    
    # Slicing a subarray
    subarray = array_2d[0:2, 1:3]
    print("Subarray (first 2 rows, last 2 columns):\n", subarray)
    
    print()

def perform_array_operations():
    print("Performing Array Operations:")
    
    # Creating two arrays for operations
    array_1 = np.array([1, 2, 3, 4, 5])
    array_2 = np.array([10, 20, 30, 40, 50])
    
    # Element-wise addition
    add_result = np.add(array_1, array_2)
    print("Element-wise addition:", add_result)
    
    # Element-wise subtraction
    subtract_result = np.subtract(array_1, array_2)
    print("Element-wise subtraction:", subtract_result)
    
    # Element-wise multiplication
    multiply_result = np.multiply(array_1, array_2)
    print("Element-wise multiplication:", multiply_result)
    
    # Element-wise division
    divide_result = np.divide(array_1, array_2)
    print("Element-wise division:", divide_result)
    
    # Matrix multiplication
    matrix_1 = np.array([[1, 2], [3, 4]])
    matrix_2 = np.array([[5, 6], [7, 8]])
    matrix_product = np.dot(matrix_1, matrix_2)
    print("Matrix multiplication:\n", matrix_product)
    
    # Transposing a matrix
    transpose = np.transpose(matrix_1)
    print("Transpose of matrix:\n", transpose)
    
    print()

def main():
    create_arrays()
    access_array_elements()
    perform_array_operations()

if __name__ == "__main__":
    main()
