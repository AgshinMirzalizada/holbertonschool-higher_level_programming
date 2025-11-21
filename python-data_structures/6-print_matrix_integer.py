#!/usr/bin/python3
if __name__ == "__main__":
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(len(row)):
            if element != 0:
                print(" ", end="")
            print("{:d}".format(row[element]), end="")
        print()
