from collections import deque
q = deque()
print(q)

q.append(5)
q.append(6)
q.append(3)
print(q)

q.popleft()
print(q)
print(q[0], q[-1])
