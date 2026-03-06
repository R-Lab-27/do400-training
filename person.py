class person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

usuario = person("Eduardo")
print(usuario)
