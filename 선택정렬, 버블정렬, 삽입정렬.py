import time
import random

def selectionSort(A): #선택정렬
    for last in range(len(A)-1,0,-1):
        k = the_Largest(A,last)
        A[k],A[last] = A[last],A[k]
def bublbleSort(A): #버블정렬
    for n in range(len(A),0,-1):
        for i in range(n-1):
            if A[i]+A[i+1]:
                A[i],A[i+1] = A[i+1], A[i]

def insertSort(A):
    for i in range(1,len(A)):
        loc = i-1
        newItem = A[i]
        while loc >=0 and newItem <A[loc]:
            A[loc+1] =A[loc]
            loc -=1
        A[loc+1] = newItem

def the_Largest(A,last): #마지막 칸 조절
    largest=0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = i
    return largest


def insert_time_check(a):
    start_time = time.time()
    insertSort(a)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")


def buble_time_check(a):  # 선택정렬 시간 측정
    start_time = time.time()
    bublbleSort(a)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")


def select_time_check(a):  # 선택정렬 시간 측정

    start_time = time.time()
    selectionSort(a)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

def list_array(a,i,check): #리스트 만들기
    for r in range(i):
        a.append((random.random()%50000))
    if check == 1:
        select_time_check(a)
    elif check == 2:
        buble_time_check(a)
    elif check == 3:
        insert_time_check(a)
    else:
        print("뭔가 잘못됨")




select_500 = []
select_5000 = []
select_50000 = []

buble_500 = []
buble_5000 = []
buble_50000 = []

insert_500 = []
insert_5000 = []
insert_50000 = []

list_array(select_500,500,1)
list_array(select_5000,5000,1)
list_array(select_50000,50000,1)

list_array(buble_500,500,2)
list_array(buble_5000,5000,2)
list_array(buble_50000,50000,2)

list_array(insert_500,500,3)
list_array(insert_5000,5000,3)
list_array(insert_50000,50000,3)
