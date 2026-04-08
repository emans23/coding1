def process_number_ranges():
    while True:
        try:
            start_range = int(input("Enter the starting number of the range: "))
            end_range = int(input("Enter the ending number of the range: "))
            if start_range > end_range:
                print("Starting number cannot be greater than the ending number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")

    square_values = []
    for number in range(start_range, end_range + 1):
        square_values.append(number ** 2)

    print("\nOriginal list of square values: {square_values}")

    odd_squares = []
    even_squares = []

    for square in square_values:
        if square % 2 != 0:
            odd_squares.append(square)
        else:
            even_squares.append(square)

    print(f"List of odd square values: {odd_squares}")
    print(f"List of even square values: {even_squares}")

process_number_ranges()
