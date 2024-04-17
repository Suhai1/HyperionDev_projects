# Define area function for rectangle
def calculate_rectangle_area(x, y):
    return x * y

# Define area function for square
def calculate_square_area(s):
    return s * s

def main():
    # Input for rectangle
    x = float(input("Enter the width of the rectangle: "))
    y = float(input("Enter the height of the rectangle: "))
    area_rectangle = calculate_rectangle_area(x, y)
    print("The area of the rectangle is:", area_rectangle)
    
    # Input for square
    s = float(input("Enter the side length of the square: "))
    area_square = calculate_square_area(s)
    print("The area of the square is:", area_square)

# Run main function
if __name__ == "__main__":
    main()

