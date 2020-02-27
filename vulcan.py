class vulan(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,value):
        if gender=='female'or'male':
            self.__gender=gender
        else:
            raise ValueError('error gender')

