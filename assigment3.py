while True:
    user_input = input("Enter a positive number or 'done' to exit: ")

    if user_input == 'done':
        break

    try:
        num = int(user_input)
        if num > 0:
            count = sum(1 for i in range(1, num + 1) if i % 3 == 0)
            print(f"Number of multiples of 3 from 1 to {num}: {count}")
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input!!! Please enter a positive number or 'done'.")
