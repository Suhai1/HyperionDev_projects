#Define area function
def calculate_rectangle_a(x, y):
    return x * y

def main():
    x = float(input("Enter the x of the rectangle: "))
    y = float(input("Enter the y of the rectangle: "))
    a = calculate_rectangle_a(x, y)
    print("The a of the rectangle is:", a)

if __name__ == "__main__":
    main()
