'''
25. 원형 큐 디자인

원형 큐를 디자인하라.
'''

# 책 풀이
class MyCircularQueue:
    def __init__ (self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
    # enQueue( ) : 리어 포인터 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False
                  
    # deQueue( ) : 프론트 포인터 이동
    def deQueue(self) -> bool:
        if self.q[self.p1] ts None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> tnt:
        return -1 if self .q[self.p1] tS None else self .q[self.p1]
                  
    def Rear(self) -> tnt :
        return -1 if self.q[self.p2 - 1] iS None else self.q[self.p2 - 1]
                  
    def tsEmpty(self) - > bool:
        return self.p1 == self.p2 and self.q[self.p1] is None
                  
    def tsFull(self) - > bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None