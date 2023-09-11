graph = [[0 for j in range(100)] for i in range(100)]
start = 1
vis = [0 for i in range(100)]
n =-1

def tsp(cur):
  minCost = 99999
  bestVertex =-1
  bestPath = ""
  vis[cur]  =1

  for i in range(1,n+1):
    if vis[i]:
      continue
    cost, path = tsp(i)
    if cost+graph[cur][i] < minCost:
      minCost = cost + graph[cur][i]
      bestVertex = i
      bestPath = path
  vis[cur] = 0

  if bestVertex == -1:
    bestPath = str(cur)+"->"+str(start)
    return graph[cur][start], bestPath

  bestPath = str(cur)+"->"+bestPath
  return minCost, bestPath




n =int(input("Enter the number of cities: "))
graph = [[0 for j in range(n+1)] for i in range(n+1)]
print("Enter the cost matrix: ")
for i in range(1,n+1):
  row = list(map(int,input().split()))
  for j in range(1,n+1):
    graph[i][j] = row[j-1]

print("The weighted matrix is: ")
for i in range(1,n+1):
  for j in range(1,n+1):
    print(graph[i][j], end="\t")
  print()

cost, path = tsp(start)
print("The path is:")
print(path)
print("The minimum cost: ", cost)