class Person:
    name = "Wendell"

    def greeting(self):
        print("Hello, I'm %s" % self.name)

me = Person()
me.greeting()

wife = Person()
wife.name = "Juliana"
wife.greeting()