class MyClass:
    static_elem = 123

    def __init__(self):
        self.object_elem = 456

c1 = MyClass()
c2 = MyClass()

# print(c1.static_elem, c1.object_elem)
# print(c2.static_elem, c2.object_elem)


MyClass.static_elem = 999

# print(c1.static_elem, c1.object_elem)
# print(c2.static_elem, c2.object_elem)

c1.object_elem = 888


print(c1.static_elem, c1.object_elem)
print(c2.static_elem, c2.object_elem)