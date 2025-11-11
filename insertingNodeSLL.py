class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("Null")

def insertNodePosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode
  
  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before insertion:")
traverseAndPrint(node1)

newNode = Node(25)
node1 = insertNodePosition(node1, newNode, 3)

print("After insertion:")
traverseAndPrint(node1)

