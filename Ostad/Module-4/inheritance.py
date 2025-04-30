# 1. Single inheritance
# class GrandFather:
#     def __init__(self, color, first_name):
#         self.color = color
#         self.first_name = first_name

# class Father(GrandFather):
#     def __init__(self, hobby, color, first_name):
#          super().__init__(color, first_name)
#          self.hobby = hobby

# gf1 = GrandFather('Red', "Chowdhury")
# f1 = Father("Footbal", 'Blue', "Hamza")
# print(f"Favorite color:{f1.color}; Favorite Name:{f1.first_name}; Hobby: {f1.hobby}")


# 2. Multiple inheritance
# class GrandFather:
#     def __init__(self, color, first_name):
#         self.color = color
#         self.first_name = first_name
#     def gf_method(self):
#         print('I am from Grand Father')

# class Father(GrandFather):
#     def __init__(self, hobby):
#          self.hobby = hobby
#     def f_method(self):
#         print('I am from Father')

# class Children(Father, GrandFather):
#     def __init__(self, fashion, hobby, color, first_name):
#         Father.__init__(self,hobby)
#         GrandFather.__init__(self, color, first_name)
#         self.fashion = fashion

# c1 = Children("Test Fashion", "Badminton", "Orange", "Chowdhury")
# c1.gf_method()
# print(c1.color, c1.fashion, c1.hobby)

# 3. Multi level inheritance
class GrandFather:
    def __init__(self, color, first_name):
        self.color = color
        self.first_name = first_name
    def gf_method(self):
        print('I am from Grand Father')

class Father(GrandFather):
    def __init__(self, hobby, color, first_name):
         super().__init__(color, first_name)
         self.hobby = hobby
    def f_method(self):
        print('I am from Father')

class Children(Father, GrandFather):
    def __init__(self, fashion, hobby, color, first_name):
        super().__init__( hobby, color, first_name)
        self.fashion = fashion

c1 = Children("Test Fashion", "Badminton", "Orange", "Chowdhury")
c1.gf_method()
print(c1.color, c1.fashion, c1.hobby)
