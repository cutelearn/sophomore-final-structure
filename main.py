class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ 在鏈表末尾添加一個新的節點 """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            while next_node.next:
                next_node = next_node.next
            next_node.next = new_node

    def update(self, old_data, new_data):
        """ 修改鏈表中的節點數據 """
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                return True
            current = current.next
        return False

    def remove(self, data):
        """ 刪除鏈表中的節點 """
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return True

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return False

        prev.next = current.next
        current = None
        return True

    def find(self, data):
        """ 查詢鏈表中的節點是否存在 """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def peek(self):
        """ 返回鏈表的第一個節點數據，不刪除它 """
        if self.head:
            return self.head.data
        return None

    def print_list(self):
        """ 打印鏈表的所有節點 """
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")


if __name__ == "__main__":
    llist = LinkedList()
    while True:
        print("1. 添加節點")
        print("2. 修改節點")
        print("3. 刪除節點")
        print("4. 查詢節點")
        print("5. 查詢第一個節點")
        print("6. 打印鏈表")
        print("7. 退出")
        try:
            choice = int(input("請輸入你的選擇: "))
        except ValueError:
            print("請輸入一個有效的數字")
            continue

        if choice == 1:
            try:
                data = int(input("請輸入節點數據: "))
                llist.append(data)
            except ValueError:
                print("請輸入一個有效的數字")
                continue
        elif choice == 2:
            try:
                old_data = int(input("請輸入要修改的節點數據: "))
                new_data = int(input("請輸入新的節點數據: "))
                llist.update(old_data, new_data)
            except ValueError:
                print("請輸入一個有效的數字")
                continue
        elif choice == 3:
            try:
                data = int(input("請輸入要刪除的節點數據: "))
                llist.remove(data)
            except ValueError:
                print("請輸入一個有效的數字")
                continue
        elif choice == 4:
            try:
                data = int(input("請輸入要查詢的節點數據: "))
                print("找到了" if llist.find(data) else "有找到")
            except ValueError:
                print("請輸入一個有效的數字")
                continue
        elif choice == 5:
            print("第一個節點數據為:", llist.peek())
        elif choice == 6:
            llist.print_list()
        elif choice == 7:
            break
        else:
            print("輸入錯誤，請重新輸入")
