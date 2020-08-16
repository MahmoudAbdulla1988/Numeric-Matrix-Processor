import math
while True:
    def operations_choice():
        print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    operations_choice()
    user_selection = str(input("Your choice:"))   

    def adding_matrices():
        dimensions_matrix_1 = [int(x) for x in input("Enter size of first matrix:").split()]
        print("Enter first matrix:")
        matrix_1 = []
        for _i in range(1, dimensions_matrix_1[0] + 1):
            rows_matrix_1 = [float(y) for y in input().split()]
            if len(rows_matrix_1) == dimensions_matrix_1[1]:
                matrix_1.append(rows_matrix_1)
            else:
                break
        
        dimensions_matrix_2 = [int(a) for a in input("Enter size of second matrix:").split()]
        print("Enter second matrix:")
        matrix_2 = []
        for _o in range(1, dimensions_matrix_2[0] + 1):
            rows_matrix_2 = [float(b) for b in input().split()]
            if len(rows_matrix_2) == dimensions_matrix_2[1]:
                matrix_2.append(rows_matrix_2)
            else:
                break

        adding_list = []
        final_result = []
        if dimensions_matrix_1[0] != dimensions_matrix_2[0] and dimensions_matrix_1[1] != dimensions_matrix_2[1]:
            print("The operation cannot be performed.")
        elif dimensions_matrix_1[0] == dimensions_matrix_2[0] and dimensions_matrix_1[1] == dimensions_matrix_2[1]:
                for c in range(len(matrix_1)):
                    for k in range(dimensions_matrix_1[1]):
                        add = matrix_1[c][k] + matrix_2[c][k]
                        adding_list.append(add)
                    final_result.append(adding_list)
                    adding_list = []
                print("The result is:")
                for r in final_result:
                    print(*r)
                print()
    def multiply_constant():
        dimensions_matrix = [int(x) for x in input("Enter size of matrix:").split()]
        matrix = []
        print("Enter matrix:")
        for i in range(1, dimensions_matrix[0] + 1):
            rows_matrix = [float(y) for y in input().split()]
            if len(rows_matrix) == dimensions_matrix[1]:
                matrix.append(rows_matrix)
            else:
                break
        scalar_num = float(input("Enter constant:"))
        multiplied_list = []
        final_result = []
        for i in range(len(matrix)):
            for j in range(dimensions_matrix[1]):
                multiplied = scalar_num * matrix[i][j]
                multiplied_list.append(multiplied)
            final_result.append(multiplied_list)
            multiplied_list = []
        print("The result is:")
        for r in final_result:
            print(*r)
        print()
    
    def Multiply_matrices():
        dimensions_matrix_1 = [int(x) for x in input("Enter size of first matrix:").split()]
        print("Enter first matrix:")
        matrix_1 = []
        for _i in range(1, dimensions_matrix_1[0] + 1):
            rows_matrix_1 = [float(y) for y in input().split()]
            if len(rows_matrix_1) == dimensions_matrix_1[1]:
                matrix_1.append(rows_matrix_1)
            else:
                break
        
        dimensions_matrix_2 = [int(a) for a in input("Enter size of second matrix:").split()]
        print("Enter second matrix:")
        matrix_2 = []
        for _o in range(1, dimensions_matrix_2[0] + 1):
            rows_matrix_2 = [float(b) for b in input().split()]
            if len(rows_matrix_2) == dimensions_matrix_2[1]:
                matrix_2.append(rows_matrix_2)
            else:
                break
        
        if dimensions_matrix_1[1] != dimensions_matrix_2[0]:
            print("The operation cannot be performed.")
        else:
            result = [[0 for x in range(dimensions_matrix_2[1])] for y in range(dimensions_matrix_1[0])]

            for c in range(len(matrix_1)):  # iterate through rows of matrix_1
                for k in range(len(matrix_2[0])):  # iterate through columns of matrix_2
                    for m in range(len(matrix_2)):  # iterate through rows of matrix_2
                        result[c][k] += matrix_1[c][m] * matrix_2[m][k]
            print("The result is:")            
            for f in result:
                print(*f)        
            print()

    def transpose():
        print()
        print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        transpose_selection = str(input("Your choice:"))
        dimensions_matrix = [int(x) for x in input("Enter matrix size:").split()]
        matrix = []
        print("Enter matrix:")
        for i in range(1, dimensions_matrix[0] + 1):
            rows_matrix = [float(y) for y in input().split()]
            if len(rows_matrix) == dimensions_matrix[1]:
                matrix.append(rows_matrix)
            else:
                break

        result = [[0 for x in range(dimensions_matrix[0])] for y in range(dimensions_matrix[1])]
        if transpose_selection == "1":  # transpose around main diagonal.            
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    result[j][i] = matrix[i][j]
            print("The result is:")
            for f in result:
                print(*f)
            print()
        
        elif transpose_selection == "2":  # transpose around side diagonal.
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    result[j][i] = matrix[i][j]
            side_diagonal_transpose = []
            for i in result:
                i.reverse()
                side_diagonal_transpose.append(i)
            side_diagonal_transpose.reverse()
            print("The result is:")
            for f in side_diagonal_transpose:
                print(*f)
            print()
        
        elif transpose_selection == "3":
            vertical_line_transpose = []
            for i in matrix:
                i.reverse()
                vertical_line_transpose.append(i)
            print("The result is:")
            for f in matrix:
                print(*f)
            print()
        
        elif transpose_selection == "4":
            matrix.reverse()
            print("The result is:")
            for f in matrix:
                print(*f)
            print()

    def determined():
        dimensions_matrix = [int(x) for x in input("Enter matrix size:").split()]
        print("Enter matrix:")
        matrix = []
        for _i in range(1, dimensions_matrix[0] + 1):
            rows_matrix = [float(y) for y in input().split()]
            if len(rows_matrix) == dimensions_matrix[1]:
                matrix.append(rows_matrix)
            else:
                break

        def recursive_cofactor(matrix, mul=1):
            width = len(matrix)
            if width == 1:
                return mul * matrix[0][0]
            else:
                sign = -1
                sum_ = 0
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(matrix[j][k])
                    m.append(buff)
                sign *= -1
                sum_ += mul * recursive_cofactor(m, sign * matrix[0][i])
            return sum_
        result = recursive_cofactor(matrix)
        print("The result is:")
        print(result)
        print()
        
    def Inverse_matrix():
        dimensions_matrix = [int(x) for x in input("Enter matrix size:").split()]
        print("Enter matrix:")
        matrix = []
        for _i in range(1, dimensions_matrix[0] + 1):
            rows_matrix = [float(y) for y in input().split()]
            if len(rows_matrix) == dimensions_matrix[1]:
                matrix.append(rows_matrix)
            else:
                break
        def getting_det(matrix, mul=1):
            width = len(matrix)
            if width == 1:
                return mul * matrix[0][0]
            else:
                sign = -1
                sum_ = 0
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(matrix[j][k])
                    m.append(buff)
                sign *= -1
                sum_ += mul * getting_det(m, sign * matrix[0][i])
            return sum_
        
        def transposeMatrix(matrix):
            width = len(matrix)
            result = [[0 for x in range(width)] for y in range(width)]           
            for i in range(width):
                for j in range(len(matrix[0])):
                    result[j][i] = matrix[i][j]
            return result

        def getMatrixMinor(matrix, i, j):
            return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
        def getMatrixInverse(matrix):
            det_matrix = getting_det(matrix)
            
            #special case for 2x2 matrix:
            if len(matrix) == 2:
                return [[matrix[1][1]/det_matrix, -1*matrix[0][1]/det_matrix],
                        [-1*matrix[1][0]/det_matrix, matrix[0][0]/det_matrix]]

            #find matrix of cofactors
            cofactors = []
            for r in range(len(matrix)):
                cofactorRow = []
                for c in range(len(matrix)):
                    minor = getMatrixMinor(matrix, r, c)
                    cofactorRow.append(((-1)**(r+c)) * getting_det(minor))
                cofactors.append(cofactorRow)
            cofactors = transposeMatrix(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r][c] = cofactors[r][c] * 100 / (det_matrix * 100)
            for f in cofactors:
                print(*f)
            print()
        getMatrixInverse(matrix)
    if user_selection == "1":
        adding_matrices()
    elif user_selection == "2":
        multiply_constant()
    elif user_selection == "3":
        Multiply_matrices()
    elif user_selection == "4":
        transpose()
    elif user_selection == "5":
        determined()
    elif user_selection == "6":
        Inverse_matrix()
    if user_selection == "0":
        break