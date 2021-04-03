def binary_serach(lll, keyyy):
    if len(lll) == 0:
        return False
    else:
        mid = len(lll) // 2
        if lll[mid] == keyyy:
            return True
        elif keyyy < lll[mid]:
            return binary_serach(lll[:mid], keyyy)
        else:
            return binary_serach(lll[mid+1:], keyyy)

# print(__name__) #defautl nya name moduel bernama main
if __name__ =='__main__':
    lll =[100,200,300,400,500,600,700,800]
    keyyy = 100
    r = binary_serach(lll, keyyy)
    print(r)
