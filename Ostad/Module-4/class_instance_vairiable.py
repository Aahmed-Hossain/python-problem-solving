class School:
    school_name = 'ABC School & College' #class variable

    def __init__(self, name):
        self.std_name = name #instance variable

school1 = School('Karim')
print(school1.std_name)
