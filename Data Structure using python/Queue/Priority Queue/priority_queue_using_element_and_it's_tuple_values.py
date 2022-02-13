#Highest value as highest priority
q=[]
q.append((1,"alexa"))
q.append((4,"alex"))
q.append((2,"al"))
print(q)
q.sort(reverse=True)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))