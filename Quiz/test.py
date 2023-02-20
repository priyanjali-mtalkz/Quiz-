def opc(x):
    if x['answer']=='C':
        return True
    else :
        return False

        
def afterDate(x):
    if str(x['date']) >= '2023-02-01 00:00:00':
        return True
    else:
        return False

def beforeDate(x):
    if str(x['date']) < '2023-02-01 00:00:00':
        return True
    else:
        return False


def onDate(x):
    if str(x['date']) == '2023-02-04 18:30:00':
        return True
    else:
        return False

def btwDate(x):
    if str(x['date']) > '2023-02-01 00:00:00' and str(x['date']) < '2023-02-10 00:00:00':
        return True
    else:
        return False 



