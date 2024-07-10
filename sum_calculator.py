import sys

def sum_calc(args):
    total = 0
    for i in args[1:]: 
        try:
            total += float(i)
        except ValueError:
            print(f"Warning '{i}' is not number will be ignored")

    print(f"Total sum = {total}")


if __name__ == "main":
    sum_calc(sys.argv)