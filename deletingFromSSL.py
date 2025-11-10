class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("None.")

def deleteSpecificNode(head, nodeToDelete):

  if head == nodeToDelete:
    return head.next
  
  currentNode = head
  while currentNode.next != nodeToDelete:
    currentNode = currentNode.next
  if currentNode.next is None:
    return head
  
  currentNode.next = currentNode.next.next
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

print("Before deletion:")
traverseAndPrint(node1)

node1 = deleteSpecificNode(node1, node4)

print("After deletion:")
traverseAndPrint(node1)