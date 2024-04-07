# This is a simple Python script to calculate the area of a rectangle and square

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate the area of a square
def calculate_square_area(length):
    return length * length

# Function to calculate the area of a rectangle
def Area_of_rec():
    # Input length and width of the rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate area
    area = calculate_rectangle_area(length, width)

    # Print the result
    print("The area of the rectangle is:", area)

# Function to calculate the area of a square
def Area_of_square():
    # Input length of the square
    length = float(input("Enter the length of the square: "))

    # Calculate area
    area = calculate_square_area(length)

    # Print the result
    print("The area of the square is:", area)

# Ask the user for their choice and call the respective function
choice = input("Enter 'R' for rectangle or 'S' for square: ")

if choice.upper() == 'R':
    Area_of_rec()
elif choice.upper() == 'S':
    Area_of_square()
else:
    print("Invalid choice. Please enter 'R' or 'S'.")


