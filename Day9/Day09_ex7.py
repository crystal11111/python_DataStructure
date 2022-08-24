# tree
class Tree:
    def __init__(self):      # 8자리칸 빈 리스트 생성
        self.size = 8
        self.tree = [None] * self.size

    def show_parents(self, position):
        print(self.tree[position // 2])

    def show_left_child(self, position):
        print(self.tree[position * 2])

    def show_right_child(self, position):
        print(self.tree[position * 2 + 1])

    def add(self):
        

    def delete(self):
