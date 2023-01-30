import sys

if __name__ == "__main__":
    print(sys.argv[1])

    with open(sys.argv[2], "r") as f:
        print(f.readlines())