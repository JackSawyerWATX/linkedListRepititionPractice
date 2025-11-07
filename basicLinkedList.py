class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

# creates the nodes
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

# points present node to next node
node1.next = node2
node2.next = node3
node3.next = node4

# shows the node
currentNode = node1
while currentNode:
  print(currentNode.data, end = " -> ")
  currentNode = currentNode.next
print("None")