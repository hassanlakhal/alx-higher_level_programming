#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 0:
        print("{0} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) > 1:
        print("{0} arguments:".format(len(sys.argv) - 1))
        for i in range(0, len(sys.argv) - 1):
            print("{0}: {1}".format(i, sys.argv[i]))
