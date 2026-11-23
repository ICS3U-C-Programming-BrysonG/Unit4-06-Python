#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 11 23, 2026
# This program uses nested loops to print out all the combinations of RGB values

def main():
    # Prints out all the combinations of RGB up to 10
    for red in range(0, 11, 1):
        for green in range(0, 11, 1):
            for blue in range(0, 11, 1):
                print("RGB({}, {}, {})".format(red, green, blue))

if __name__ == "__main__":
    main()