import sys

if __name__ == "__main__":
    print(sys.argv[1])

    f = open(sys.argv[2])
    print(f.readlines())