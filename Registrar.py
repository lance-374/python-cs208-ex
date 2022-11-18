class Student:
    def __init__(self, name, grad_year, grad_term, major=None):
        self.name = name
        self.grad_year=grad_year
        self.grad_term=grad_term
        self.advisor=None
        self.passed=set()
        self.enrolled=set()
        self.major=major

    def __repr__(self):
        return f"<Student: {self.name}, {self.grad_term} {self.grad_year}>"
    
    def enroll(self, clas): # enrolls student in class, returns True if successful and False otherwise
        if clas.course in self.passed:
            return False
        # check if clas meet times overlap with any enrolled classes' meet times
        # for i in self.enrolled:
        #     if not i.meet_times.isdisjoint(clas.meet_times):
        #         return False
        if clas.course.any==True:
            if not clas.course.prereq.isdisjoint(self.passed):
                self.enrolled.add(clas)
                return True
        else:
            if clas.course.prereq.issubset(self.passed):
                self.enrolled.add(clas)
                return True
        return False
    
    def drop(self, clas): # drops a class, returns False if student is not enrolled in class, true otherwise
        if (not clas in self.enrolled):
            return False
        self.enrolled.discard(clas)
        return True

    def req_courses(self):
        return self.major.courses.difference(self.passed)
    
    def pass_class(self, clas):
        self.passed.add(clas.course)
        self.drop(clas)

    def pass_course(self, course):
        self.passed.add(course)
    
    def set_advisor(self, professor):
        if self.advisor != None:
            self.advisor.advisees.discard(self)
        self.advisor = professor
        professor.advisees.add(self)

class Professor:
    def __init__(self, name, dept, courses):
        self.name=name
        self.dept=dept
        self.courses=courses
        self.advisees=set()
    
    def __repr__(self):
        return f"<Professor: {self.name}, {self.dept}>"

    def teaches_course(self, course):
        return course in self.courses

class Time: # represents class period and day
    def __init__(self, day, period):
        self.day=day
        self.period=period
    
    def __repr__(self):
        return f"<{self.day}, Period {self.period}>"

class Course:
    def __init__(self, code, name, prereq=set(), any=False):
        self.code=code # course code (e.g. CS208)
        self.name=name # "Programming Languages"
        self.prereq=prereq
        self.any=any # set this to True if only one prereq is required, leave blank otherwise

    def __repr__(self):
        return f"{self.code}"

class Class:
    def __init__(self, course, term, year, meet_times, prof, section):
        self.course=course
        self.term=term
        self.year=year
        self.meet_times=meet_times
        self.prof=prof
        self.section=section
        prof.courses.add(course)
    
    def __repr__(self):
        return f"<{self.course.code}, {self.term} {self.year}, Section {self.section}>"

class Major:
    def __init__(self, name, courses):
        self.name=name
        self.courses=courses
    
    def __repr__(self):
        return f"<{self.name}, {self.courses}>"



def test():
    math175 = Course("CS175", "Discrete Mathematics")
    cs141 = Course("CS141", "Introduction to Computer Science")
    cs142 = Course("CS142", "Program Design and Methodology", {cs141})
    cs205 = Course("CS205", "Algorithm Design and Analysis", {cs142, math175})
    cs208 = Course("CS208", "Programming Languages", {cs142})
    cs214 = Course("CS214", "Introduction to Computing Systems", {cs142})
    cs220 = Course("CS220", "Applied Data Structures", {cs142})
    cs292 = Course("CS292", "Software Developemnt and Professional Practice", {cs205, cs208, cs214, cs220}, True)
    cs322 = Course("CS322", "Software Engineering")
    cs303 = Course("CS303", "Computer Graphics", {cs205, cs208, cs214, cs220, cs292}, True)
    cs305 = Course("CS305", "Operating Systems", {cs205, cs208, cs214, cs220, cs292}, True)
    cs_ba = Major("Computer Science BA", {cs141, cs142, cs205, cs208, cs214, cs220, cs292, math175, cs322, cs303, cs305})
    psyc100 = Course("PSYC100", "Introduction to Psychology")
    psyc201 = Course("PSYC201", "Cognitive Psychology", {psyc100})
    foo100 = Course("FOO100", "Introduction to Foo")
    rb = Professor("R B", "Computer Science", {cs208, cs205, cs220, cs322, cs141, cs292})
    db = Professor("D B", "Computer Science", {cs142, cs205})
    ag = Professor("A G", "Psychology", {psyc100})
    px = Professor("P X", "PSYC", {psyc201}) # normally the name slots should contain full names, real names are just being omitted from this model and replaced with initials
    blaze = Professor("Blaze", "FOO", {foo100})
    ls = Student("L S", 2025, "Winter", cs_ba)
    ls.pass_course(cs141)
    ls.pass_course(cs142)
    ls.pass_course(cs220)
    ls.pass_course(psyc100)
    ls.pass_course(math175)
    print(ls.req_courses())
    cs208_1 = Class(cs208, "Fall", 2022, {Time("Monday", 2), Time("Tuesday", 2), Time("Wednesday", 2), Time("Friday", 2)}, rb,1 )
    # cs292_1 = Class(cs292, "Winter", 2023, {Time("Monday", 5), Time("Monday", 6), Time("Wednesday", 5), Time("Wednesday", 6)}, rb, 1)
    cs205_1 = Class(cs205, "Fall", 2022, {Time("Monday", 5), Time("Wednesday", 5), Time("Thursday", 5), Time("Friday", 5)}, db, 1)
    # psyc100_1 = Class(psyc100, "Winter", 2022, {Time("Monday", 4), Time("Wednesday", 4), Time("Friday", 4)}, ag, 1)
    psyc201_1 = Class(psyc201, "Fall", 2022, {Time("Monday", 3), Time("Wednesday", 3), Time("Friday", 3)}, px, 1)
    foo100_1 = Class(foo100, "Fall", 2022, {Time("Monday", 3), Time("Wednesday", 3), Time("Friday", 3)}, blaze, 1)
    ls.set_advisor(db)
    print(cs205_1.meet_times.isdisjoint(cs208_1.meet_times))
    print(foo100_1.meet_times.isdisjoint(psyc201_1.meet_times))
    print(ls)
    print(ls.advisor)
    print(rb)
    print(rb.teaches_course(cs208))
    print(rb.teaches_course(psyc201))
    print(cs208)
    ls.enroll(cs208_1)
    ls.enroll(cs205_1)
    ls.enroll(psyc201_1)
    print("foo100 meet times")
    print(foo100_1.meet_times)
    print("psyc201 meet times")
    print(psyc201_1.meet_times)
    print(ls.passed)
    ls.enroll(foo100_1)
    print(ls.enrolled)
    print(ls.drop(foo100_1))
    print(ls.enrolled)
    print(ls.drop(foo100_1))
    ls.pass_class(psyc201_1)
    ls.pass_course(cs292)
    print(ls.passed)
    print(Time("Monday",3)==Time("Monday",3))

test()