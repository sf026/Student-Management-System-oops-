
class person:                       
    def __init__(self,name,age):     
        self.name=name   
        self.age=age
    def details(self):   
        return f"Name: {self.name}, Age: {self.age}"
    

class Student(person):              
    def __init__(self, name, age, student_id, marks):   
        super().__init__(name, age)     
        self.student_id=student_id
        self.marks=marks
    def grade(self):        
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return "B" 
        elif self.marks>=50:
            return "C"
        else:
            return "Fail"  
    def details(self):        
        base_details=super().details()
        return f"{base_details},student ID:{self.student_id},Marks:{self.marks},Grade:{self.grade()}"
    