from math import floor

def searchMatrix(matrix, target):
    def inner(cols):
        if not cols:
            return False

        mid = floor(len(cols) / 2)
        value = cols[mid]

        if target == value:
            return True
        elif target < value:
            return inner(cols[:mid]) # end = mid - 1
        elif target > value:
            return inner(cols[mid+1:]) # start = mid + 1

    def in_range(cols):
        if cols[0] <= target and target <= cols[-1]:
            return 0
        elif target < cols[0]:
            return -1
        elif target > cols[-1]:
            return 1

    def outer(rows):
        if not rows:
            return False

        mid = floor(len(rows) / 2)
        row = rows[mid]
        x = in_range(row)

        if x == 0:
            return inner(row)
        elif x < 0:
            return outer(rows[:mid]) # end = mid - 1
        elif x > 0:
            return outer(rows[mid + 1:]) # start = mid + 1

    return outer(matrix)


result = searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
print("Results: ", result, " - Expects: ", True)