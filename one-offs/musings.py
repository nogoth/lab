from typing import Self # 3.11  or higher

class LinkNode():
    def __init__(self,input=None,ptr=None):
        self.value=input
        self.next=ptr
    def add(self, ptr=None) -> Self:
        if not ptr is None:
            self.next = ptr
        return self

h = LinkNode(1)
n1 = LinkNode(2,h)
n2 = LinkNode(3,n1).add(LinkNode(14))


print(h)
assert n1.next == h
print(n2.next)
