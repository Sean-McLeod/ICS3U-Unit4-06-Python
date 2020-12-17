#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can show the user the rgb values


def main():
    # this function can print rgb values

    counter1 = 0
    counter2 = 0
    counter3 = 0

    print("This program can print out RGB values")
    print("\n", end="")

    # process & output
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("RGB({0},{1},{2})".format(counter1, counter2, counter3))


if __name__ == "__main__":
    main()
