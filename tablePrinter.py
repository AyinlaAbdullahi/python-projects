def printTable(tableData):
    # Step 1: find the maximum width for each column
    colWidths = [max(len(item) for item in col) for col in tableData]

    # Step 2: print row by row (transpose the list of lists)
    numRows = len(tableData[0])
    for row in range(numRows):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colWidths[col]), end=" ")
        print()  # new line at the end of each row


# Example usage
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)