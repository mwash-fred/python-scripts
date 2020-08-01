#This script finds a target wors from a 2D array of characters
# The search is either left tp right or top to down in the matrix
# For this script the target word is FOAM 

def word_search(matrix, word):
    #Left to right search happens on the same row
    target = ''
    r = 0
    c = 0
    for row in matrix[r]:
        if( r < len(matrix) and c < len(matrix[0])):
            for row in matrix[r]:
                char = matrix[r][c]
                target += char
                c += 1
        else:
            break
        if (target == word):
            print(f"{word} found \nTrue")
            target = ''
            r = 0
            c = 0 
            break
        else:
            target = ''
            r += 1
            c = 0
    
    # Top down search happens on the same column
    r = 0
    for row in matrix[r]:
        if( r < len(matrix) and c < len(matrix[0])):
            for column in matrix[r]:
                char = matrix[r][c]
                target += char
                r += 1
        else:
            break
        if (target == word):
            print(f"{word} found \nTrue")
            target = ''
            r = 0
            c = 0
            break
        else:
            target = ''
            r = 0
            c += 1

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]

word_search(matrix, "CQOS")