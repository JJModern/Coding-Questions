class Assignment(object):
    def __init__(self, aid, name, points):
        self.aid = aid
        self.name = name
        self.points = points
        self.__students_submitted = []

    def add_student_submission(self, student_id):
        if student_id in self.__students_submitted:
            raise Exception(student_id, "has already submitted!")
        else:
            self.__students_submitted.append(student_id)

    def num_submissions(self):
        return len(self.__students_submitted)


class Course(object):
    def __init__(self, code, name, num_students):
        self.code = code
        self.name = name
        self.num_students = num_students
        self.__assignments = {}

    def add_assignment(self, assignment):
        self.__assignments[assignment.aid] = assignment

    def get_assignment_by_id(self, aid):
        return self.__assignments.get(aid, None)

    def total_points(self):
        total_points = 0
        for assignment in self.__assignments.values():
            total_points += assignment.points
        return total_points

    def percent_submitted(self, aid):
        assignment = self.__assignments.get(aid, None)
        if not assignment:
            return None
        return assignment.num_submissions() / self.num_students * 100


a1 = Assignment("pa1", "Programming Assignment 1", 50)
a2 = Assignment("pa2", "Programming Assignment 2", 100)
a3 = Assignment("pa3", "Programming Assignment 3", 100)
print(a1.num_submissions())
print(a2.num_submissions())
print(a3.num_submissions())
a1.add_student_submission(10000001)
a1.add_student_submission(20000002)
a1.add_student_submission(30000003)
print(a1.num_submissions())
a2.add_student_submission(10000001)
a2.add_student_submission(20000002)
print(a2.num_submissions())
print(a3.num_submissions())
c = Course("BAGL 10100", "Introductory Bagelology", 4)
c.add_assignment(a1)
c.add_assignment(a2)
c.add_assignment(a3)
a = c.get_assignment_by_id("pa1")
print(a.name)
a = c.get_assignment_by_id("pa2")
print(a.name)
a = c.get_assignment_by_id("pa3")
print(a.name)
print(c.total_points())
print(c.percent_submitted("pa1"))  # 75
print(c.percent_submitted("pa2"))  # 50.0
print(c.percent_submitted("pa3"))  # 0.0
