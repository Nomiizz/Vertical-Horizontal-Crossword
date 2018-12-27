# Dynammic Programming Solution to Crossword Problem

The solution assumes that given a word and a square matrix of alphabets, the word can be found in the matrix by traversing only in the vertical or horizontal direction, and not diagonally. Once the program executes it accepts a word folowed by a blank line and then a square matrix. If the word is found in the matrix then the program prints the starting and ending coordinates of the alphabets in the matrix, else it prints '0'.

For example, if the input is  
HORSE  
  
AABCDE  
BAHOT9  
DhcRS4  
aQAAE6  
321458  
EFGHIJ  
  
the output should be  
2 3 4 5\n  