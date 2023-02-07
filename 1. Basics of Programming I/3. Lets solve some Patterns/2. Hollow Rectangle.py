#Hollow Rectangle
row, col = map(int, input().split())

for r in range(row):  #first row or last row -> print 5 *
    if (r == 0)  or (r == row-1):
        for c in range(col):
            print("* ",end = '')     
    else:
        #remainging middle rows
        print("* ",end = '')  #first star
        
        for i in range(col-2):  #spaces
            print("  ",end = '')
         
        print("* ",end = '')  #last star
    print()
