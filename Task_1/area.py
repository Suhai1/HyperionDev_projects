# This is a simple Python script to calculate the area of a rectangle

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Main function
def main():
    # Input length and width of the rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate area
    area = calculate_rectangle_area(length, width)

    # Print the result
    print("The area of the rectangle is:", area)

# Call the main function
if __name__ == "__main__":
    main()

