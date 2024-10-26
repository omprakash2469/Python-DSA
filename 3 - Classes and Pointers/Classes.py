class Cookie:
    def __init__(self, color):
        self.color = color

    def get_cookie(self):
        return self.color
    
    def set_cookie(self, color):
        self.color = color


cookie_one = Cookie("Blue")
cookie_two = Cookie("Green")

print(f"Cookie one is {cookie_one.get_cookie()}")
print(f"Cookie two is {cookie_two.get_cookie()}")

# Update cookies
cookie_one.set_cookie("Red")
cookie_two.set_cookie("Yellow")

print(f"Cookie one is now {cookie_one.get_cookie()}")
print(f"Cookie two is now {cookie_two.get_cookie()}")

