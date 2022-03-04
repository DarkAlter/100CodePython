class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        self.followers += 1
        user.following += 1
        
test1 = User("001", "stephen")
test2 = User("002","Angel")
test1.follow(test2)

print(test1.followers)
print(test1.following)
print(test2.followers)
print(test2.following)