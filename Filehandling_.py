def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 9876\n")
    except (FileNotFoundError, PermissionError) as e:
        print("Error:", e)
    finally:
        print("File creation process completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except (FileNotFoundError, PermissionError) as e:
        print("Error:", e)
    finally:
        print("File reading process completed.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
    except (FileNotFoundError, PermissionError) as e:
        print("Error:", e)
    finally:
        print("File appending process completed.")

if __name__ == "__main__":
    create_file()
    print()  # Empty line for better readability
    read_file()
    print()  # Empty line for better readability
    append_to_file()

