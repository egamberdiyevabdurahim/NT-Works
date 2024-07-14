

class Member:
    member_count = 0

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        Member.member_count += 1

    def display_info(self):
        print(f"Username: {self.username}\nEmail: {self.email}\nAge: {self.age}\n")

    @classmethod
    def get_member_count(cls):
        return cls.member_count


class Student(Member):
    def __init__(self, username, email, age, student_id):
        super().__init__(username, email, age)
        self.student_id = student_id
        self.courses = {}
        print(f"{username} - Studentga Qo'shildi!")

    def display_info(self):
        super().display_info()
        print(f"Student ID-si: {self.student_id}\nKurslar va baholar: {self.courses}")

    def enroll_in_course(self, course):
        if course not in self.courses:
            self.courses[course] = 0
            print(f"{self.username} - Kursga yozildi: {course}")
        else:
            print(f"{self.username} - Allaqachon Bu Kursga Yozilgan: {course}")

    def set_grade(self, course, grade):
        if course in self.courses:
            self.courses[course] = grade
            print(f"{self.username} - {course} uchun Baho Qo'yildi: {grade}")
        else:
            print(f"{self.username} - Bunday Kurs Mavjud Emas: {course}")

    def get_average_grade(self):
        grades = [grade for grade in self.courses.values() if grade != 0]
        if grades:
            average_grade = sum(grades) / len(grades)
            return average_grade
        return None


class Teacher(Member):
    def __init__(self, username, email, age, teacher_id):
        super().__init__(username, email, age)
        self.teacher_id = teacher_id
        self.subjects = []
        print(f"{username} - Teacherga Qo'shildi!")

    def display_info(self):
        super().display_info()
        print(f"Teacher ID-si: {self.teacher_id}\nFanlar: {self.subjects}")

    def assign_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"{self.username} - Belgilangan Mavzu: {subject}")
        else:
            print(f"{self.username} - Allaqachon Bunday Mavzu Mavjud: {subject}")


class AdminStaff(Member):
    def __init__(self, username, email, age, staff_id, department):
        super().__init__(username, email, age)
        self.staff_id = staff_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Xodim ID-si: {self.staff_id}\nBo'limi: {self.department}")


student1 = Student("Abdurahim", "abdurahim@gmail.com", 16, "S1")
student1.enroll_in_course("Math")
student1.set_grade("Math", 97)
student1.enroll_in_course("Physics")
student1.set_grade("Physics", 70)
student1.enroll_in_course("Biology")
student1.set_grade("Biology", 50)
student1.display_info()
print(f"O'rtacha baho: {student1.get_average_grade()}")

student2 = Student("Muhammad", "muhammad@gmail.com", 16, "S2")
student2.enroll_in_course("Physics")
student2.set_grade("Physics", 80)
student2.enroll_in_course("Math")
student2.set_grade("Math", 60)
student2.enroll_in_course("Biology")
student2.set_grade("Biology", 96)
student2.display_info()
print(f"O'rtacha baho: {student2.get_average_grade()}")

print("#############################################")
print(f"Memberlar Soni: {student2.get_member_count()}")
print("#############################################")


teacher1 = Teacher("Rustam", "rustam@mail.ru", 40, "T1")
teacher1.assign_subject("Math")
teacher1.assign_subject("Physics")
teacher1.assign_subject("Biology")
teacher1.display_info()

teacher2 = Teacher("Ali", "ali@mail.ru", 35, "T2")
teacher2.assign_subject("Biology")
teacher2.assign_subject("Physics")
teacher2.display_info()


admin1 = AdminStaff("Admin", "admin@icloud.com", 35, "A1", "IT")
admin1.display_info()

admin2 = AdminStaff("Admin2", "admin2@icloud.com", 30, "A2", "English Language")
admin2.display_info()
