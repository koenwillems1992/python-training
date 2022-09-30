class Person:
    count = 0
    population = []

    def __init__(self, name):
        self.name = name
        Person.count += 1
        Person.population.append(self.name)


john = Person("John")
jane = Person("Jane")


class Date:

    def __init__(self, year: int, month: int, day: int):
        try:
            year = int(year)
        except ValueError:
            ""
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = date_string.split('-')
        return cls(year, month, day)

    @classmethod
    def from_dict(cls, date_dict):
        year = date_dict['year']
        month = date_dict['month']
        day = date_dict['day']
        return cls(year, month, day)

    def __repr__(self):
        return f"Date(year={self.year}, month={self.month}, day={self.day})"


d1 = Date(2015, 7, 15)
d2 = Date.from_string("2020-10-23")
d3 = Date.from_dict({"year": 2009, "month": 4, "day": 1})

print(d1)
print(d2)
print(d3)
