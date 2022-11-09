#%%
from abc import ABC, abstractmethod

class School:
    def __init__(self, name: str, level: str, number_of_students: int):
        self.name = name
        self.level = level
        self.number_of_students = number_of_students
        
    # getters
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_number_of_students(self):
        return self.number_of_students
    
    # setters

    def set_number_of_students(self, number_of_students: int):
        self.number_of_students = number_of_students
        
    # representation
    def __repr__(self):
        return f"{self.name} is a {self.level} school with {self.number_of_students} students."
    

class PrimarySchool(School):
    def __init__(self, name, number_of_students,pick_up_policy,level='primary'):
        self.pick_up_policy = pick_up_policy
        super().__init__(name,level, number_of_students,)
        





def main():
    mayo = School(name="Mayo", level="High", number_of_students=1000)
    print(mayo.get_name())
    print(mayo.get_level())
    print(mayo.get_number_of_students())
    mayo.set_number_of_students(2000)
    print(mayo.get_number_of_students())
    print(mayo.__repr__())
    
# if __name__ == "__main__":
    # main()
# %%
