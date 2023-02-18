# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        total_elements = m*n

        startingRow = 0
        endingCol = n-1
        endingRow = m-1
        startingCol = 0

        count = 0
        while count < total_elements:
            #  print startingRow
            for i in range(startingCol, endingCol+1):
                if count < total_elements:
                    ans.append(matrix[startingRow][i])
                    count += 1
            startingRow += 1

            #  print endingCol
            for i in range(startingRow, endingRow+1):
                if count < total_elements:
                    ans.append(matrix[i][endingCol])
                    count += 1
            endingCol -= 1

            #  print endingRow
            for i in range(endingCol, startingCol-1, -1):
                if count < total_elements:
                    ans.append(matrix[endingRow][i])
                    count += 1
            endingRow -= 1

            #  print startingRow
            for i in range(endingRow, startingRow-1, -1):
                if count < total_elements:
                    ans.append(matrix[i][startingCol])
                    count += 1
            startingCol += 1

        return ans

        # res = []
        # left, right = 0, len(matrix[0])
        # top, bottom = 0, len(matrix)

        # while left < right and top < bottom:
        #     # get every i in the top row
        #     for i in range(left, right):
        #         res.append(matrix[top][i])
        #     top += 1
        #     # get every i in the right col
        #     for i in range(top, bottom):
        #         res.append(matrix[i][right - 1])
        #     right -= 1
        #     if not (left < right and top < bottom):
        #         break
        #     # get every i in the bottom row
        #     for i in range(right - 1, left - 1, -1):
        #         res.append(matrix[bottom - 1][i])
        #     bottom -= 1
        #     # get every i in the left col
        #     for i in range(bottom - 1, top - 1, -1):
        #         res.append(matrix[i][left])
        #     left += 1

        # return res