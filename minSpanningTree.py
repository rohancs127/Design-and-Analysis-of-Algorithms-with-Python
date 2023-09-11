n = int(input("Enter the number of nodes: "))
max = 99999
selected = [False for i in range(n)]
parent=[0 for i in range(n)]

def find(i):
  while(parent[i]!= i):
    i = parent[i]

  return i

def uni(i,j):
  x = find(i)
  y = find(j)
  parent[x] = y

def prims(n, cost):
  nEdge = 0
  selected[0] = True
  while nEdge<n-1:
    min =max
    x=y=0
    for i in range(n):
      if selected[i]:
        for j in range(n):
          if not selected[j]  and cost[i][j]:
            if cost[i][j]<min:
              min = cost[i][j]
              x=i
              y=j

    print(x,"->",y,":",cost[x][y])
    selected[y] =True
    nEdge += 1


def kruskals(n,cost):
  minCost = 0
  eCtr =0
  for i in range(n):
    parent[i] =i
  while eCtr<n-1:
    min = max
    x=y=0
    for i in range(n):
      for j in range(n):
        if cost[i][j]<min and find(i)!=find(j):
          min = cost[i][j]
          x=i
          y=j
    uni(x,y)
    print("Edge (",x+1,",",y+1,"): ",cost[x][y])
    minCost+= min
    eCtr+=1

  print("Minimum Cost: ", minCost)


print("Enter the weighted matrix: ")
cost =[[0 for j in range(n)] for i in range(n)]
for i in range(n):
  row=list(map(int,input().split()))
  for j in range(n):
    cost[i][j]=row[j]
    if cost[i][j]==0:
      cost[i][j]=max

print("Minimum spanning tree using Prim's algorithm:")
prims(n,cost)
print("Minimum spanning tree using Kruskal's algorithm: ")
kruskals(n,cost)

print(cost)
    