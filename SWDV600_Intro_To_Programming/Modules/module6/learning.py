class Course:
    "The course class"
    
    def __repr__(self):
        return 'Title: {}, Code: {}'.format(self._title, self._code)
    
    def __init__(self, title, code, creditHours):
        """
            Creates a new course instance
            e.g Course('Intro to Programming', 'BDAT 600', 3)
        """
        self._title = title
        self._code = code
        self._creditHours = creditHours
        
    def getTitle(self):
        return self._title
    
    def getCode(self):
        return self._code
    
    def getCreditHours(self):
        return self._creditHours
        

class Student:
    "The Student class"
    
    def __init__(self, name, major, coursesSeq):
        self.name = name
        self.major = major
        self.courses = coursesSeq
        
    def getName(self):
        return self.name
    
    def getCourses(self):
        return self.courses
    
    def getMajor(self):
        return self.major
    
    def addCourse(self, course):
        self.courses.append(course)
        
    def creditHoursCompleted(self):
        totalCredits = 0
        for course in self.getCourses():
            totalCredits = totalCredits + course.getCreditHours()
        return totalCredits
    
    def readyForGraduation(self):
        creditHoursCompleted = self.creditHoursCompleted()
        
        if creditHoursCompleted < 12:
            return False
        else:
            return True
    
        
def main():
    
    me = Student(
            'Colin Knebl',
            'M.S. in Software Development',
            [Course('Intro to Programming', 'BDAT 600', 3)]
        )

    print(me.getCourses())
    
if __name__ == '__main__':
    main()


