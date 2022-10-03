##Full Name: Kanika Gupta
##TEAM MEMBERS: KANIKA GUPTA, SHREYAS SWAROOP , YIRGA YAKOB
##ID: KXG5522@PSU.EDU
##Date: 09/30/2022
##Filename: A.1_Gupta_Kanika_KXG5522.py
##Purpose: to solve assignment 1



#PROBLEM 1
def countele(x,a):
    counter=0
    for i in range(0,len(a)):
        if x==a[i]:
            counter=counter+1
    return(counter)

def prob1(a):
    mini=len(a)
    maxi=0
    minno=a[0]
    maxino=a[0]
    li=[]
    for j in range(0,len(a)):
        n=countele(a[j],a)
        if mini>=n:
            mini=n
            minno=a[j]
        elif maxi<=n:
            maxi=n
            maxino=a[j]
        
    finallist=[maxino,minno]
    return(finallist)

#PROBLEM 2
def size(lst,w):
    fill = []
    blank = []
    for i in range(len(lst)-w+1):
        fill = lst[i]
        blank+=[another(w, lst, i, fill)]
    print(blank)

def another(w, lst, i, fill): 
    for j in range(1,w):
        if lst [i + j] > fill:
            fill = lst[i+j]
    return(fill)




    
#MAIN FUNCTION

def main():
    a= [ 10, 30, 60, 88, 10, 30, 10, 60, 3, 88 ]
    l=prob1(a)
    print(l)
    lst = [1, 3, 5, 1, 2, 4, 7, 8]
    w = 4
    size(lst,w)
    

main()
