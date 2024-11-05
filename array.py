import numpy as np

# Create a sample multidimensional array
original_array = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], dtype=float)

# Save the array to a text file using NumPy
np.savetxt('array_numpy.txt', original_array, delimiter=',')

# Load the array from the text file using NumPy
loaded_array_numpy = np.loadtxt('array_numpy.txt', delimiter=',', dtype=float)

print("Original array (NumPy):")
print(original_array)

print("Loaded array (NumPy):")
print(loaded_array_numpy)

# Save the array to a text file using Python's built-in file handling
with open('array_python.txt', 'w') as file:
    for row in original_array:
        file.write(','.join(map(str, row)) + '\n')

# Initialize an empty array to hold the loaded data
loaded_array_python = []

# Load the array from the text file using Python's built-in file handling
with open('array_python.txt', 'r') as file:
    for line in file:
        loaded_array_python.append(list(map(float, line.strip().split(','))))

print("Original array (Python):")
print(original_array)

print("Loaded array (Python):")
print(np.array(loaded_array_python))  # Convert to NumPy array for consistency
