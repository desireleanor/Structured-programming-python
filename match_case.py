options = ("""
1. Add
2. View
3. Exit""")
print(options)

while True:
    try:
        option = input("Select an option: ")
    except ValueError:
        print("Select a valid option.")

    match option:
        case "1":
            print("Adding...")
        case "2":
            print("Viewing...")
        case "3":
            print("Exiting...")
            break
        case _:
            print("Invalid input")