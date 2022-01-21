#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    numb = []
    for i in str(n):
        numb.append(int(i))
    numb.reverse()
    return numb
