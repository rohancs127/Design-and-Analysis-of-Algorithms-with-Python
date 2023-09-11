def isSafe(board,row,col,n):
  for i in range(row):
    if board[i][col]==1:
      return False

  for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
    if board[i][j]==1:
      return False

  for i,j in zip(range(row,-1,-1),range(col,n)):
    if board[i][j]==1:
      return False

  return True

def nQueensSolutionsUtil(board,row,n,solutions):
  if row==n:
    solutions.append([row[:] for row in board])
    return
  for col in range(n):
    if isSafe(board,row,col,n):
      board[row][col]=1
      nQueensSolutionsUtil(board,row+1,n,solutions)
      board[row][col]=0

def nQueensSolutions(n):
  board =[[0 for i in range(n)] for j in range(n)]
  solutions = []
  row =0
  nQueensSolutionsUtil(board,row,n,solutions)
  return solutions

def printSolutions(solutions):
  if not solutions:
    print("There in no possible solution.")
  else:
    for sol in solutions:
      for row in sol:
        print(' '.join(map(str,row)))
      print()

n= int(input("Enter the size of the board(N): "))
solutions = nQueensSolutions(n)
printSolutions(solutions)