import time


def palindrom(string):


    #make list valiable to restore string as 'list'
    check=""

    #make valiable for check the number of string
    n=len(string)

    #for length of string, append to list while up to 0 as minus
    for i in range(len(string)):
        n-=1
        check+=string[n]
        
    return string == check



if __name__ == "__main__":


    start_time=time.time()

    print(palindrom('hello'))
    print(palindrom('eye'))
    print(palindrom('nisioisin'))

    end_time=time.time()

    print(end_time-start_time)
#test
