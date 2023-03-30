def main():
    rupees = int(input("Enter the value in rupees: "))

    convert_to_dollars = dollars(rupees)

    print(f"The converted value in dollars is {convert_to_dollars}")


def dollars(a): return a*80


main()
