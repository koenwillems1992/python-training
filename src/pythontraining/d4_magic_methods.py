class Person:

    def __init__(self, name, height):
        self.height = height
        self.name = name

    def __str__(self):
        return f"Person is {self.name}"

    def __repr__(self):
        return 'Person(name = ' + self.name + ', height in cm = ' + str(self.height) + ')'

    def __gt__(self, other):
        return self.height > other.height


p1 = Person('John', 180)
p2 = Person('Jane', 170)
print(p1 > p2)
print(p2 > p1)

print(p1)