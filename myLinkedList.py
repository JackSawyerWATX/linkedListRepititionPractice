class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)

    if not self.head:
      self.head = new_node
      return
    
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def delete(self, data):
    if not self.head:
      return
      
    if self.head.data == data:
      self.head = self.head.next
      return
      
    current = self.head
    while current.next:
      if current.next.data == data:
        current.next = current.next.next
        return
      current = current.next

  def find(self, data):
    current = self.head
    while current:
      if current.data == data:
        return True
      current = current.next
    return False
      
  def get_size(self):
    count = 0
    current= self.head
    while current:
      count += 1
      current = current.next
    return count
      
  def display(self):
    if not self.head:
      print("List is empty.")
      return

    elements = []
    current = self.head

    while current:
      elements.append(str(current.data))
      current = current.next

    print(elements)

  def insert_at_position(self, position, data):
    if position == 0:
      self.prepend(data)
      return
    new_node = Node(data)
    current = self.head

    for i in range(position - 1):
      if current is None:
        print(f"Position {position} is out of bounds.")
        return
      current = current.next

    if current is None:
      print(f"Position {position} is out of bounds.")
      return

    new_node.next = current.next
    current.next = new_node

  def reverse(self):
    previous = None
    current = self.head

    while current:
      next_node = current.next
      current.next = previous
      previous = current
      current = next_node
    
    self.head = previous

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.display()
    my_list.append(1)
    my_list.display()
    my_list.append(2)
    my_list.display()
    my_list.append(3)
    my_list.display()
    my_list.append(0)
    my_list.display()

    print(my_list.get_size())
    print(my_list.find(2))
    print(my_list.find(5))
    my_list.insert_at_position(2, 1.5)
    my_list.display()
    my_list.delete(1.5)
    my_list.display()
    my_list.reverse()
    my_list.display()