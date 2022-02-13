#lowest element as highest priority
import queue
q=queue.PriorityQueue()
q.put(10)
q.put(20)
q.put(60)
q.put(40)
'''It will dequeue according to the order here as both values are same i.e 40'''
q.put(40)
print(q.queue)
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())