def main():
    fraction = get_input()
    percentage = into_percentage(fraction)
    print_output(percentage)

def get_input():
    while True:
        try:
            fraction = input("Fraction: ")
            if fraction[2] >= fraction[0] and fraction[1] == "/":
                split_fraction = fraction.split("/")
                return [int(split_fraction[0]), int(split_fraction[1])]
        except:
            pass

def into_percentage(fraction):
    percentage = (fraction[0] / fraction[1]) * 100
    return percentage

def print_output(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        new_percentage = round(percentage)
        print(f"{new_percentage}%")

main()
