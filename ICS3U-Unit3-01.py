# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Unit3-01.py File, review in python.


def main():

    # input
    first_number = float(input("Please type in the first number: "))
    second_number = float(input("Second number you want to add them up: "))

    # process
    total = first_number + second_number

    # output
    print(
        "\nThe total of numbers {0:,} and {1:,} is {2:,}.".format(
            first_number, second_number, total
        )
    )

    print("\n\nDone.")


if __name__ == "__main__":
    main()
