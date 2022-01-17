
class Dogs:
    '''My dog class'''
    def __init__(self):
        self.breed = 'Chihuahua'
        self.color = 'Brown'
        self.nickname = self
        self._age = self
        self.fav_snack = self

    def jon(self):
        self.nickname = 'Bubba'
        self.fav_snack = 'Smoked Salmon'
        return self

    def francis(self):
        self.nickname = 'Curly Fry'
        self.fav_snack = 'Chicken'
        return self

    def get_age(self):
        return self._age

    def set_age(self, num):
        self._age = num

    age = property(get_age, set_age)


mydogs = Dogs()


print(f'I have two {mydogs.breed}s, they go by {mydogs.jon().nickname} \
and {mydogs.francis().nickname}.')
