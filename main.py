def show_menu():
    print('1.Citire date')
    print('2.Cea mai lunga subsecventa cu prorpietatea ca toate numerele sunt pare')
    print('3.Cea mai lunga subsecventa cu prorpietatea ca toate numerele au acelasi numar de divizori')
    print ('4.Cea mai lunga subsecventa cu proprietatea ca toate numerele sunt prime')
    print('5.Iesire')
def read_list():
    lst=[]
    lst_str=input('Dati numerele separate prin spatiu: ')
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst
def get_longest_all_even(lst:list[int]):
    '''
    Determina cea mai lunga subsecventa cu toate numerele pare
    :param lst:lista in care se cauta subsecventa
    :return:subsecventa gasita
    '''
    n=len(lst)
    result=[]
    for st in range(n):
        for dr in range(st,n):
            all_even=True
            for num in lst[st:dr+1]:
                if num % 2 != 0:
                    all_even=False
                    break
            if all_even:
                if dr-st+1>len(result):
                    result=lst[st:dr+1]
    return result
def test_get_longest_all_even():
    assert get_longest_all_even([1,2,3,4,6,8,5])==[4, 6, 8]
    assert get_longest_all_even([1, 5, 3, 2, 6, 9, 5]) == [2, 6]
    assert get_longest_all_even([1, 2, 3, 4, 6, 8, 5, 2, 4, 12, 20, 22]) == [2, 4, 12, 20, 22]
    assert get_longest_all_even([1, 2, 4, 8, 3, 5, 7, 8, 5]) == [2, 4, 8]
def get_div_count(n):
    '''
    calculeaza numarul de divizori ai unui numar
    :param n:numarul caruia vrem sa ii aflam divizorii
    :return:numarul de divizori ai numarului n
    '''
    count=0
    for i in range(1,n+1):
        if n % i == 0:
            count=count+1
    return count
def get_longest_same_div_count(lst:list[int]):
    '''
    Determina cea mai lunga subsecventa cu acelasi numar de divizori
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa ceruta
    '''
    n = len(lst)
    result = []
    div_count=get_div_count(lst[0])
    for st in range(n):
        for dr in range(st, n):
            ok=True
            for num in lst[st:dr + 1]:
                if get_div_count(num)!=div_count:
                    div_count=get_div_count(num)
                    ok=False
                    break
            if ok:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result
def test_get_longest_same_div_count():
    assert get_longest_same_div_count([1, 2, 3, 5, 7, 8, 9])==[2, 3, 5, 7]
    assert get_longest_same_div_count([1, 7, 4, 9]) == [4, 9]
    assert get_longest_same_div_count([12, 4, 9, 1]) != [12]
    assert get_longest_same_div_count([10, 2, 4, 9, 16, 1]) != [1]
def is_prime(n):
    '''
    Verifica daca un numar este prim
    :param n: numarul care trebuie verificat
    :return: True daca este prim si False in caz contrar
    '''
    if n<2:
        return False
    for i in range (2,n):
        if n % i == 0:
            return False
    return True
def get_longest_all_prime(lst:list[int]):
    '''
    Determina cea mai lunga subsecventa cu toate numerele prime
    :param lst: lista in care se cauta subsecventele
    :return: cea mai lunga subsecventa cu proprietatea ceruta
    '''
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_prime = True
            for num in lst[st:dr + 1]:
                if is_prime(num)==False:
                    all_prime = False
                    break
            if all_prime:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result

def test_get_longest_all_prime():
    assert get_longest_all_prime([1, 2, 3, 5, 6, 9]) == [2, 3, 5]
    assert get_longest_all_prime([10, 12, 23, 5, 7, 9]) == [23, 5, 7]
    assert get_longest_all_prime([14, 22, 34, 5, 13, 90]) == [5, 13]
    assert get_longest_all_prime([25, 2, 6, 55, 6, 9, 2, 3, 5]) == [2, 3, 5]

def main():
    lst=[]
    while True:
        show_menu()
        opt=input('Optiunea: ')
        if opt=='1':
            lst=read_list()
        elif opt=='2':
            print(get_longest_all_even(lst))
        elif opt=='3':
           print(get_longest_same_div_count(lst))
        elif opt=='4':
            print(get_longest_all_prime(lst))
        elif opt=='5':
            break
        else:
         print('Optiune invalida')

if __name__ == '__main__':
    test_get_longest_all_even()
    test_get_longest_same_div_count()
    test_get_longest_all_prime()
    main()


