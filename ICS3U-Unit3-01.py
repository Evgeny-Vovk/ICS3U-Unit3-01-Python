# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Unit3-01.py File, review in python.


def main():

    # input
    first_number = int(input("Please type in the first number(integer): "))
    second_number = int(input("Second number you want to add them up(integer): "))

    # process
    total = first_number + second_number

    # output
    print(
        "\n{0:,} + {1:,} = {2:,}.".format(
            first_number, second_number, total
        )
    )

    print("\n\nDone.")


if __name__ == "__main__":
    main()
