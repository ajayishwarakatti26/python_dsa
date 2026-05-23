n=6
e=7
egdes=[(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]
# print(egdes)

#adjacency list:
adjList=[]
for i in range(n):
    adjList.append([])
for edge in egdes:
    x=edge[0]
    y=edge[1]
    
    adjList[x].append(y)
    adjList[y].append(x)

for i in range(n):
        print(i ,"->",adjList[i])


#ahjances matrix:
ajdmatrix=[]
for i in range(n):
     List1=[0]*n
     ajdmatrix.append(List1.copy())

for i in range(e):
     a=egdes[i][0]
     b=egdes[i][1]
     ajdmatrix[a][b]=1
     ajdmatrix[b][a]=1

for i in ajdmatrix:
     print(i)


