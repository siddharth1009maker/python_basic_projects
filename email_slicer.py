def main():
    print("Welcome to E-Mail slicer: ")
    email = input("Enter the email: ")

    (username, domain) = email.split("@")

    (domain, extension) = domain.split(".", 1)

    print(f"Username: {username}")

    print(f"Domain: {domain}")

    print(f"Extension: {extension}")


main()
