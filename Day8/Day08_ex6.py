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
        if self.front == self.size - 1:
            self.rear + 1:
            return True
        else:
            return False

    # item을 rear(파란 화살표 자리)에 넣어 주는 거
    def enqueue(self, item):
        self.queue[self.rear] = item
        self.rear += 1                  # rear가 한 칸 전진

    # front(빨간 화살표 자리)값을 제거하는 거
    def dequeue(self, item):
        self.queue[self.front] = [None]
        self.front += 1                 # front가 한 칸 전진


"""
다른 언어에서는,
None이라는 용어 자체가 없다
= 변수 안에 값을 제거하는 거 자체가 없다



"""