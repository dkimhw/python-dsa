class Node:
  """A node of a linked list"""

  def __init__(self, node_data):
    self._data = node_data
    self._next = None

  def get_data(self):
    """Get node data"""
    return self._data

  def set_data(self, node_data):
    """Set node data"""
    self._data = node_data

  data = property(get_data, set_data)

  def get_next(self):
    """Get next node"""
    return self._next

  def set_next(self, node_next):
    """Set next node"""
    self._next = node_next

  next = property(get_next, set_next)

  def __str__(self):
    """String"""
    return str(self._data)

class LinkedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  # adds to the front
  def add(self, item):
    new_node = Node(item)

    if self.is_empty():
      self.head = new_node
    else:
      new_node.set_next(self.head)
      self.head = new_node

  def size(self):
    current = self.head
    count = 0
    while current is not None:
      current = current.get_next()
      count += 1

    return count

  def search(self, item):
    current = self.head
    while current is not None:
      if current.data == item:
        return True
      current = current.get_next()

    return False

  def remove(self, item):
    current = self.head
    previous = None

    while current is not None:
      if current.get_data() == item:
          break
      previous = current
      current = current.next

    if current is None:
      raise ValueError("{} is not in the list".format(item))
    if previous is None:
      self.head = current.get_next()
    else:
      previous.next = current.get_next()
