class Singleton(object):
    __instance = None

    def __new__(cls):
        print('calling new')
        if cls.__instance == None:
            cls.__instance = "New Connection"
        return cls.__instance


def main():
    s1 = Singleton()
    s2 = Singleton()
    print(s1 == s2)
    print (s1)

main()