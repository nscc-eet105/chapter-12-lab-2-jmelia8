#Joe Melia EET-107

def main():
    print("Unique Word Counter\n")
    again ="y"
    while again == "y":
        try:
            name = input("Enter the name of the file you wish to process: ")
            file = open(name, "r")
            contents = file.read()
            file.close()
            result = count(contents, name)
            print(result)
            again = "n"
        except FileNotFoundError:
            again = input("File could not be found. Would you like to try again? (y)es or (n)o?").lower()
def count(contents, name):
    unique = []
    for word in contents.split():
        if word not in unique:
            unique.append(word)
    count = len(unique)
    result = f"There are {count} unique words in {name}\n \nThanks for using the program!"
    return result
main()
        
