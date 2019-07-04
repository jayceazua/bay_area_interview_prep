class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.replace('\n', 'n')
        print(self.matrix_string)

    def row(self, index):
        rows = []

        current = []

        for val in self.matrix_string:
            print(val)

            if val.isdigit():
                current.append(val)
                print("CURRENT", current, val)

            elif val.isspace():
                print("just skip", current, val)

            elif val == 'n':
                print("not covered", val)
                rows.append(current) # new row, add current one
                current = [] # empty current row list
                print("CURRENT", current, val)

        return rows[index-1]

    def column(self, index):
        cols = []
        current = []

        counter = 0
        for val in self.matrix_string:
            if val != 'n':
                current.append(val)
                cols.append(current)
                current = []
            
            if counter < len(cols):
                cols[counter].append(val)
                counter += 1
            else: 
                counter = 0 

if __name__ == "__main__":
    matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
    print(matrix.row(3), [7, 8, 9])
