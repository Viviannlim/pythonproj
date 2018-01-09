import transactions as jennytrans

def processTransaction():
    try:
        t_file = open('file/jennyposb.txt', 'r')
        lines = []
        for trans in t_file:
            list = trans.split(',')
            e = jennytrans.transactions(list[0],list[1],int(list[2]))
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


