def knapsack(v,w,cap,n):
  f = [[0 for j in range(cap+1)] for i in range(n+1)]
  selected = [0]*(n+1)

  for i in range(n+1):
    for j in range(cap+1):
      if j<w[i]:
        f[i][j]= f[i-1][j]
      else:
        f[i][j]= max(f[i-1][j], v[i]+f[i-1][j-w[i]])

  print("The optimal solution is: ", f[n][cap])

  i,j = n,cap
  while i>0 and j>0:
    if f[i][j]!= f[i-1][j]:
      selected[i]=1
      j -= w[i]
    i -= 1
  print("Selected items: ")
  for i in range(n+1):
    if selected[i]!=0:
      print(i, end=" ")


n = int(input("Enter the number of items: "))
v = [0]*(n+1)
w = [0]*(n+1)
print("Enter the weights (Seperated by spaces): ")
wInput = input().split()
for i in range(1,n+1):
  w[i] = int(wInput[i-1])

print("Enter the values (Seperated by spaces): ")
vInput = input().split()
for i in range(1,n+1):
  v[i] = int(vInput[i-1])

cap = int(input("Enter the maximum capacity: "))

knapsack(v,w,cap,n)