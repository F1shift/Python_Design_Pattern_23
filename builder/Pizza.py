class Pizza:
    def __init__(self):
        self.materials = []

    def check(self):
        print("Pizza:")
        print(*list(map(lambda m: m.check(), self.materials)))
