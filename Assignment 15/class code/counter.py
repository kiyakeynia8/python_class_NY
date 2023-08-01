class Counter:
    def __init__(self, x):
        self.x = x

    def up(self, r):
        # for i in range(r):
        self.x += r

    def down(self):
        self.x -= 1

counter_object = Counter(0)
print(counter_object.x)

counter_object.up(10)
# counter_object.up()
# counter_object.up()
# counter_object.up()

print(counter_object.x)

counter_object.down()

print(counter_object.x)