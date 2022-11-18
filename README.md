# Simple Registrar model 
Contains classes Student, Professor, Course, Class, Major, and Time
## Getting Started
1. Start by creating Courses. Create them using syntax "Course("code", "name", {set of prereqs, optional}, any*) 
* \* pass True here if only one course from prereqs set is required, leave blank otherwise
2. The next step is to create Majors. Create them using syntax Major("name of major", {set of required courses})
3. Then create Professors using syntax Professor("name", "department", {set of courses optional}, {set of classes optional**}, {set of advisees})
* \*\* A Class is a particular instance of a course such as CS 208 Fall Term 2022 Section 1
4. Now create Students using syntax Student("name", "grad year", "grad term***", major)
* \*\*\* can be "fall", "winter", "spring", or "summer"
5. Finally, create Classes using syntax Class(Course, Term, Year, {set of meet times}, professor, section number. Each item in the set of meet times should be of class Time(Day of the week*\*\*\*, period 1-6****)
* \*\*\*\* Day of the week should be strings "Monday", "Tuesday", "Wednesday", "Thursday", "Friday". If courses meet for two periods together, simply use two Times for that such as {Time("Monday", 2), Time("Monday", 3)}

# Methods:
## Student
* student.enroll(class) enrolls student in class if possible, meaning that all prereqs are met and the course has not already been passed by the student
* student.pass_course(course) adds the course to the student's set of passed courses. Only use this if transferring credits.
* student.pass_class(class) add the classes course to the students set of passed courses, than drops the class. Only works if student is currently enrolled in the class
* student.set_advisor(professor) assigns the given professor as the student's advisor, and adds the student to the professor's set of advisees
* student.req_courses() returns the set of courses still needed to complete the student's major
* student.drop(class) remove the given class from the student's set of enrolled classes if the student is enrolled in the class, returns True if class was dropped and False if the student was never enrolled in the class
## Professor
* professor.teaches_course(course) returns True if professor teaches given course, false otherwise

# Properties that can be safely edited directly
## Student
* name
* grad_year
* grad_term
* major
## Professor
* name
* dept
* courses
## Course
* code
* name
* prereq
* any
## Class
* course
* term
* year
* meet_times
* prof (professor)
* section
## Major
* name
* courses (set of required courses to complete major)

# Properties that can be read but not edited directly without breaking
## Student
* advisor
* passed (set of passed courses)
* enrolled (set of currently enrolled courses)

### There is a test function at the end of the file

# Known issues
* it is possible to enroll in two courses that overlap, the isdisjoint method doesn't work on Times
* isdisjoint always returns true when comparing two sets of class Time
* comparing two identical Times returns False 
* Time("Monday",3)==Time("Monday",3) -> False
* when attempting to define \_\_eq\_\_ function, unhashable type error is thrown
