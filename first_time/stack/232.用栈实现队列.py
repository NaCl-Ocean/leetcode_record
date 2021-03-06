#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pushstack = list()
        self.popstack = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pushstack.append(x)



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
        return self.popstack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
        return self.popstack[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.pushstack and not self.popstack:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

