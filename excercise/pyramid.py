def number_pyramid(rows):
   for i in range(rows):
        
        print(' ' * (rows - i - 1), end='')
        
        for j in range(i + 1):
            print(j + 1, end=' ')
        
        print()


num_rows = 5
number_pyramid(num_rows)
