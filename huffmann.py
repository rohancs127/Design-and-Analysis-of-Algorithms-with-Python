import heapq


class HuffmannNode:
  def __init__(self,char,freq):
    self.char= char
    self.freq= freq
    self.left = None
    self.right = None

  def __lt__(self,other):
    return self.freq<other.freq

def buildHuffmannTree(characters, frequencies):
  heap =[]
  for i in range(len(characters)):
    node = HuffmannNode(characters[i], frequencies[i])
    heapq.heappush(heap, node)

  while len(heap)>1:
    leftNode = heapq.heappop(heap)
    rightNode = heapq.heappop(heap)
    combinedFreq = leftNode.freq + rightNode.freq
    combinedNode = HuffmannNode(None, combinedFreq)
    combinedNode.left = leftNode
    combinedNode.right = rightNode
    heapq.heappush(heap, combinedNode)

  return heapq.heappop(heap)

def buildHuffmannCode(root, currentCode, huffmannCodes):
  if root is None:
    return

  if root.char is not None:
    huffmannCodes[root.char]= currentCode
    return

  buildHuffmannCode(root.left, currentCode+'0', huffmannCodes)
  buildHuffmannCode(root.right, currentCode+'1', huffmannCodes)

def encodeString(string, huffmannCodes):
  encodedString = ''
  for char in string:
    encodedString += huffmannCodes[char]

  return encodedString

def decodeString(encodedString,root):
  decodedString =''
  currentNode = root
  for bit in encodedString:
    if bit == '0':
      currentNode= currentNode.left
    else:
      currentNode = currentNode.right
    if currentNode.char is not None:
      decodedString += currentNode.char
      currentNode=root

  return decodedString


n= int(input("Enter the number of characters"))
characters=[]
frequencies =[]

for _i in range (n):
  c= input("Enter the character:")
  f= float(input("Enter the frequency:"))
  characters.append(c)
  frequencies.append(f)

huffmannTree = buildHuffmannTree(characters, frequencies)

huffmannCodes = {}
buildHuffmannCode(huffmannTree,'',huffmannCodes)

string = input("Enter a string to encode:")
encodedString = encodeString(string, huffmannCodes)
print("Huffman Codes:")
for char, code in huffmannCodes.items():
  print(char,':',code)

print("Encoded string: ", encodedString)

ch = input("Do you want to decode the encoded string?(y/n): ")
if ch=='y':
  decodedString = decodeString(encodedString, huffmannTree)
  print("Decoded string: ", decodedString)

ch= input("Do you want to enter a new string to decode?(y/n): ")
if ch=='y':
  encodedString=input("Enter encoded string: ")
  decodedString= decodeString(encodedString, huffmannTree)
  print("Decoded String: ", decodedString)