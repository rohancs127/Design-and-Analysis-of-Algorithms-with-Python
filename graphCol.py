from collections import defaultdict

class Graph:
  def __init__(self,subjects):
    self.subjects = subjects
    self.graph = defaultdict(list)

  def addEdge(self, subject1, subject2):
    self.graph[subject1].append(subject2)
    self.graph[subject2].append(subject1)

  def graphColoring(self):
    colorMap = {}
    availableColors = set(range(1,len(self.subjects)+1))
    for subject in self.subjects:
      usedColors = set()
      for neighbor in self.graph[subject]:
        if neighbor in colorMap:
          usedColors.add(colorMap[neighbor])
        availableColor = availableColors-usedColors
        if availableColor:
          colorMap[subject] = min(availableColor)
        else:
          colorMap[subject] = len(availableColors)+1
          availableColors.add(colorMap[subject])
    return colorMap

  def getMinimumTimeSlot(self):
    colorMap = self.graphColoring()
    return max(colorMap.values())


if __name__ == '__main__':
  numSubjects = int(input("Enter the number of subjects: "))
  subjects=[]
  students ={}
  for i in range(numSubjects):
    sub=input(f"Enter the name of subject {i+1}: ")
    subjects.append(sub)
    numStudents = int(input(f"Enter the number of students for {sub}: "))
    studentList=[]
    for j in range(numStudents):
      stud = input(f"Enter the name of student {j+1} for {sub}: ")
      studentList.append(stud)

    students[sub]=(studentList)

  numEdge = int(input("Enter the number of edges: "))
  graph = Graph(subjects)

  for _ in range(numEdge):
    edge = input("Enter edge from (subject1,subject2): ").split()
    graph.addEdge(edge[0],edge[1])

  minTS = graph.getMinimumTimeSlot()
  print("Minimum Time slots required: ", minTS)
  
  