def b_search(t, ls:list):
    f = 0
    fou = True
    l = len(ls)
    mid = (f+l)//2
    while fou:
        if ls[mid]==t:
            print("found at:", mid)
            fou=False
        elif ls[mid]>t:
            l=mid-1
            mid=(f+l)//2
        elif ls[mid]<t:
            f=mid+1
            mid=(f+l)//2

def main():
    ls=[]
    n=int(input("Enter number of elements in list: "))
    for r in range(n):
        elem = int(input(f"Enter {r+1}th element: "))
        ls.append(elem)
    elem = int(input("Enter element to be searched: "))
    ls.sort()
    print(ls)
    b_search(elem, ls)
    

main()
input()
