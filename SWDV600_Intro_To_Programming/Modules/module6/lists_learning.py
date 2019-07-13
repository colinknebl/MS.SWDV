"""
All about Python Lists
\n
OPERATORS:
+ operator = list concatenation
* operator = list repition
[n] operator = list indexing
[:] operator = list sequencing
for <var> in <seq> = list iteration
len(<seq>) = returns length of list

METHODS:
append => add <item> to end of sequence :: <seq>.append(<item>)
del => removes <item> from sequence :: del <seq>[n]
in => searches the sequence :: <item> in <seq>
index => returns index of first occurence of <item> or ValueError if item is not in sequence :: <seq>.index(<item>)
count => returns the number the <item> appears in the sequence :: <seq>.count(<item>)
pop => removes <item> from sequence and returns the removed <item> :: <seq>.pop(2)
insert => insert an <item> to the <seq> at a specific index :: <seq>.insert( <index>, <item> )
sort => orders numeric and string values :: <seq>.sort()
\tCan provide a key param :: <seq>.sort(key=<key>)
reverse => reverse sorts a sequence :: <seq>.reverse()

"""

class MonthMgr:
    
    def __init__(self):
        self.months = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
        
    def getMonth(self, monthNum):
        return self.months[monthNum - 1]


def main():
    
    monthMgr = MonthMgr()
    
    print(monthMgr.getMonth(1))
    print(monthMgr.getMonth(8))
    

main()