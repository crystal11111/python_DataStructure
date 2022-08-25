# isEmpty() : Front == Rear
# isFull() : Rear == Front 앞자리

class Queue:
    def __init__(self):
        self.front = 0  # 빨간 화살표
        self.rear = 0   # 파란 화살표
        self.size = 5   # 큐의 크기
        self.queue = [None] * self.size

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    # rear가 front보다 한 칸 전에 있으면: rear == front - 1
    # front가 rear보다 한 칸 뒤에 있으면: front == rear + 1
    def isFull(self):
        if self.front == (self.rear+ 1) % self.size:
            return True
        else:
            return False

    # item을 rear(파란 화살표 자리)에 넣어 주는 거
    def enqueue(self, item):
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size         # rear가 한 칸 전진

    # front(빨간 화살표 자리)값을 제거하는 거
    def dequeue(self):
        self.queue[self.front] = [None]
        self.front = (self.front + 1) % self.size      # front가 한 칸 전진

    def display(self):  # front ~ rear -1
        index = self.front
        while index <= self.rear - 1:
            print(self.queue[index], end = " ")
            index += 1
        #print(self.queue[self.front:self.rear])
        print()

q = Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.enqueue(1)
q.display()

q.dequeue()
q.dequeue()
q.dequeue()
q.display()

print(q.isFull())
q.dequeue()
print(q.isEmpty())

"""
다른 언어에서는,
None이라는 용어 자체가 없다
= 변수 안에 값을 제거하는 거 자체가 없다

그래서 자료구조를 표현(= 값이 제거됐다)
저료구조의 범위(ex. front ~ rear -1)

"""
