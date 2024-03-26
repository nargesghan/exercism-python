class Matrix:
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        for i, row in enumerate(rows):
            rows[i] = list(map(int, row.split()))
        self.matrix = rows

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
