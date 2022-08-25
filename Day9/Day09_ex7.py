# tree
class Tree:
    def __init__(self):      # 8자리칸 빈 리스트 생성
        self.cursor = 1
        self.size = 8
        self.tree = [None] * self.size

    def show_parents(self, position):
        # 루트노드
        # position이 범위 안에 들어오는지
        print("{}의 부모 노드 값은 {}".format(position, self.tree[position // 2]))

    def show_left_child(self, position):
        # position * 2가 트리 범위 안에 들어오는지
        print(self.tree[position * 2])

    def show_right_child(self, position):
        # position * 2 + 1가 범위 안에 들어오는지
        print(self.tree[position * 2 + 1])

    def add(self, item):
        if not self.isFull():   # self.isFull() == False:
            self.tree[self.cursor] = item
            self.cursor += 1

    def delete(self):
        if self.isEmpty() == False:
            self.tree[self.cursor - 1] = [None]     # 다른 언어는 이 코드가 없다
            self.cursor -= 1

    def isEmpty(self):
        if self.cursor == 1:
            return True
        else:
            return False

    def isFull(self):
        if self.cursor == self.size:
            return True
        else:
            return False

    def display(self):
        index = 1
        while index < self.cursor:
            print(self.tree[index], end="")
            index += 1
        print()
        # print(self.tree[1:self.cursor])

tree = Tree()
tree.add('a')
tree.add('b')
tree.add('c')
tree.add('d')
tree.add('e')
tree.add('f')
tree.add('g')
print(tree.tree)

tree.show_parents(3)    # a
tree.show_parents(7)    # c

tree.show_left_child(2)     # 4번자리 = d
tree.show_right_child(2)    # 5번자리 = e

tree.delete()
tree.delete()
tree.delete()
tree.display()

# 동아리, 과목, 기숙사, 인턴