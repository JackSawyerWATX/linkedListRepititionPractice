class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class My_linkedlist:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def print_list(self):
    current_node = self.head
    while current_node:
      print(f"* {current_node.data}")
      current_node = current_node.next

linked_list = My_linkedlist()
linked_list.append("Starbucks")
linked_list.append("Dunkin Donuts")
linked_list.append("Peet's Coffee")
linked_list.append("Tim Hortons")
linked_list.append("Mercury")
linked_list.print_list()