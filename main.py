class SpiralMatrix:
    def create(self, n):
        mas = [[0] * n for i in range(n)]

        i = 1 # The number to write to the array
        x = 0 # Row position
        y = -1 # Columns position
        d_row = 0 # -1 0 1
        d_column = 1 # -1 0 1
        length = len(str(n**2))

        while i <= n**2:
            if 0 <= x + d_row < n and 0 <= y + d_column < n and mas[x + d_row][y + d_column] == 0:
                x += d_row
                y+= d_column
                mas[x][y] = i
                i+= 1
            else:
                if d_column == 1:
                    d_column = 0
                    d_row = 1
                elif d_row == 1:
                    d_row = 0
                    d_column = -1
                elif d_column == -1:
                    d_column = 0
                    d_row = -1
                elif d_row == -1:
                    d_row = 0
                    d_column = 1

        for row in mas:
            for elem in row:
                print(str(elem).rjust(length), end = ' ')
            print()

s = SpiralMatrix()
s.create(11)
