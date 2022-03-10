def print_matrix1(matrix):
    print("classic nested loops using ij indexes")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


def print_matrix2(matrix):
    print("enhanced nested loops")
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print()


def print_matrix3(matrix):
    print("for loop with shortcut (*) row expansion")
    for row in matrix:
        print(*row)


def test_matrices():

    keyboard = [["`", 1, 2, 3, 4, 5, 6, 7, 8, 9, "-", "="],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
                ["Z", "X", "C", "V", "B", "N" "M", ",", ".", "/"]]


    matrices = [["keyboard", keyboard],]

    for title, matrix in matrices:
        print(title, len(matrix), "x", "~" + str(len(matrix[0])))
        print_matrix1(matrix)
        print_matrix2(matrix)
        print_matrix3(matrix)
        print()


if __name__ == "__main__":
    test_matrices()