class School:
    school_name = 'Ostad School'

    @staticmethod
    def calculate_grade(marks):
        if marks >= 90:
            return 'A+'
        else:
            return 'Fail'
print(School.calculate_grade(89))
print(School().calculate_grade(89))
# Even though static methods are designed to be called on the class, you can still call them on an instance.
