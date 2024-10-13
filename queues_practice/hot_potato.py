from queue import Queue


def hot_potato(name_list, num):
  sim_queue = Queue()
  for name in name_list:
    sim_queue.enqueue(name)

  while sim_queue.size() > 1:
    for _ in range(num):
      curr_val = sim_queue.dequeue()
      sim_queue.enqueue(curr_val)

    # the child with the hot potato after `num` passes removed
    sim_queue.dequeue()

  return sim_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
