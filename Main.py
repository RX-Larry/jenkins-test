import sys

if __name__ == "__main__":
    print(sys.argv[1])

    f = open("test.txt")
    print(f.readlines())