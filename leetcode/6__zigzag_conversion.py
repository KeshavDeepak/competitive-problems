def convert(s: str, numRows: int) -> str:
        # handle edge case where number of rows is 1
        if numRows == 1:
            return s
        
        output = [[] for _ in range(numRows)]
        current_row = 0
        direction = 1
        
        for char in s:
            output[current_row].append(char)
            
            # update direction if needed
            if current_row == len(output) - 1:
                direction = -1
            
            if current_row == 0:
                direction = 1
                
            # update current row
            current_row += direction
        
        return ''.join([''.join(row) for row in output])


# print(convert("zigzagconversion", 3))
# print(convert("PAYPALISHIRING", 3))
print(convert("AB", 1))