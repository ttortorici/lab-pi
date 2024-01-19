class Dog:
    HAIR = True

    def __init__(self):
        self.hair = self.__class__.HAIR


class HairlessDog(Dog):
    HAIR = False


if __name__ == "__main__":
    finn = HairlessDog()
    print(finn.HAIR)
    print(finn.hair)
