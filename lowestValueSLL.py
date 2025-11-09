class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def fildLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(37)
node2 = Node(13)
node3 = Node(49)
node4 = Node(58)
node5 = Node(25)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(fildLowestValue(node1))