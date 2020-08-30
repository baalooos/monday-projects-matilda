from errbot import BotPlugin, botcmd
import datetime

def load_file(tab):
    f = open("files/matilda/Total.txt", "r")
    line = f.readline()
    while line:
        tab.append(line.strip('\n'))

        line = f.readline()

    f.close()
    tab.reverse()

    return(tab)

def sum_week(tab):
    sum = 0
    #day of the week, from 0 (monday) to 6 (sunday)
    day = datetime.datetime.today().weekday()
    
    for i in range(day,-1,-1):
        sum += int(tab[i])

    return sum

def sum_month(tab):
    sum = 0
    #jour
    #print(datetime.datetime.now().strftime("%d"))
    #mois
    #print(datetime.datetime.now().strftime("%m"))
    
    for i in range(int(datetime.datetime.now().strftime("%d")),-1,-1):
        sum += int(tab[i])

    return(sum)

def sum_year(tab):
    sum = 0
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    for i in range(day_of_year,-1,-1):
        sum += int(tab[i])
    return sum

class matilda(BotPlugin):
    """Monday project - Plugin for Matilda"""

    @botcmd
    def matilda_week(self, msg, args):

        total = []
        total = load_file(total)

        return 'the expanse for this week so far is ' + str(sum_week(total))

    @botcmd
    def matilda_month(self, msg, args):

        total = []
        total = load_file(total)

        return 'the expanse for this month so far is ' + str(sum_month(total))

    @botcmd
    def matilda_year(self, msg, args):

        total = []
        total = load_file(total)

        return 'the expanse for this year so far is ' + str(sum_year(total))
