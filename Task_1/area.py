# This is a simple Python script to calculate the area_of_rectangle of a rectangle

# Function to calculate the area_of_rectangle of a rectangle
def calculate_rectangle_area_of_rectangle(length_of_rectangle, width_of_rectangle):
    return length_of_rectangle * width_of_rectangle

# Main function
def main():
    # Input length_of_rectangle and width_of_rectangle of the rectangle
    length_of_rectangle = float(input("Enter the length_of_rectangle of the rectangle: "))
    width_of_rectangle = float(input("Enter the width_of_rectangle of the rectangle: "))

    # Calculate area_of_rectangle
    area_of_rectangle = calculate_rectangle_area_of_rectangle(length_of_rectangle, width_of_rectangle)

    # Print the result
    print("The area_of_rectangle of the rectangle is:", area_of_rectangle)

# Call the main function
if __name__ == "__main__":
    main()

