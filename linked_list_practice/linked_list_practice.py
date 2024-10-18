from linked_list import LinkedList


ll = LinkedList()

ll.add(20)
ll.add(25)
ll.add(30)
ll.add(35)
ll.add(40)

print(ll.size())
print("searching 35: ", ll.search(35))
print(ll.remove(35))
print("searching 35 again:", ll.search(35))
