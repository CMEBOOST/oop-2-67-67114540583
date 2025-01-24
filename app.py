class Student(object):
  sutudent_count = 0

  def __new__(self):
    print('student.__new__')

  def __init__(self):
    print('self.__init__')
    self.gpa = 4.00

  def study_hard(self):
    print('Sir, yes sir.')
