import sys

def hello(args):
    if len(args) ==1:
        print("Hello world!")
    elif len(args) == 2:
        print("Hello, {args(1)}")

if __name__ == "__main__":
    hello()