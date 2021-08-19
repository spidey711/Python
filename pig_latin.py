#Program to convert english to piglatin and vice verca

def piglatin(data):
    a = str(data)
    a = a.lower()
    a = a + a[0]+'ay'
    a = list(a)
    a.remove(a[0])

    a = ''.join(a)
    print(a)
def english(data):
    a = data.lower()
    for i in range(1, 3):
        a = a[:-1]

    a =  a[len(a)-1]+a[0:len(a)-1]
    print(a)

piglatin("Hello_World")
#output : ello_worldhay
english("ello_worldhay")
#output : Hello_World
