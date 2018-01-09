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

def processTransaction():
    try:
        t_file = open('file/jennyposb.txt', 'r')
        lines = []
        for trans in t_file:
            list = trans.split(',')
            e = transactions(list[0],list[1],int(list[2]))
            lines.append(e)
            return lines
    except IOError:
        print('File cannot be found')
    except ValueError:
        print('Invalid integer')
    except ZeroDivisionError:
        print('Second number cannot be 0')
    except:
        print('An unknown error occured')

