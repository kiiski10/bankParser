SELECTED_BANK = "nordea"
payments = loadCSV("tilitiedot.csv")
receiverName = "tampereen kaupunki"

class Date:
    def __init__(self, dateStr):
        try:
            self.day = dateStr.split(".")[0]
            self.month = dateStr.split(".")[1]
            self.year = dateStr.split(".")[2]
        except IndexError as e:
            self.day = "00"
            self.month = "00"
            self.year = "00"

    def __str__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)


class Payment:
    def __init__(self, date, amount, receiver, title):
        self.date = date
        self.amount = amount
        self.receiver = receiver
        self.title = title


def loadCSV(fileName):
    paymnts = []
    with open(fileName, "r") as csv:
        rows = csv.readlines()
    for row in rows[1:]:                # Ignore first row as it is for column labels
        if SELECTED_BANK == "nordea":
            paymnts.append(nordeaRowToPayment(row))
        else:
            print("Sorry, your bank is not supported")
    return paymnts

def nordeaRowToPayment(row):
    row = row.split(";")
    date = Date(row[0])
    amount = row[1]
    receiver = row[5]
    title = row[4]
    print(row)
    return(Payment(date, amount, receiver, title))

def paymentsByReceiver(receiverName):
    fltrObj = filter(lambda x: receiverName.upper() in x.receiver.upper(), payments)
    return list(fltrObj)

def paymentsByMonth(month):
    fltrObj = filter(lambda x: month == x.date.month.lstrip("0"), payments)
    return list(fltrObj)

for p in paymentsByReceiver(receiverName):
    print("{} {} {} {}€".format(p.date, p.receiver, p.title, p.amount))

"""
for p in paymentsByMonth("2"):
    print("{} {} {}€".format(p.date, p.receiver, p.amount))
"""
