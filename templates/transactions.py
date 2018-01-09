class transactions():
    def __init__(self,date,type,amount):
        self.__date = date
        self.__type = type
        self.__amount = amount

    def get_date(self):
        return self.__date
    def get_type(self):
        return self.__type
    def get_amount(self):
        return self.__amount

    def set_date(self,date):
        self.__date = date
    def set_type(self,type):
        self.__type = type
    def set_amount(self,amount):
        self.__amount = amount