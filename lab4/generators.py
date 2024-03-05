# #1
# import generators
# def zhul(n):
#     idx = 0
#     while idx <= n:
#         yield idx 
#         idx += 1
# def dyz(m):
#     for i in m:
#         yield i**2
# a = zhul(int(input()))
# b = dyz(a)
# for i in b:
#     print(i)

# #2
# def gen(n):
#     idx = 0
#     while idx <= n:
#         yield idx
#         idx += 1
# def even(m):
#     for i in m:
#         if i%2 == 0:
#             yield i
# a = gen(int(input()))
# b = even(a)
# for i in b:
#     print(i)



# #3
# def gen(n):
#     idx=0
#     while idx<=n:
#         yield idx
#         idx +=1

# def num(m):
#     for i in m:
#         if i %3==0:
#             if i%4 ==0:
#                 yield i

# a = gen(int(input()))
# b= num(a)
# for i in b:
#     print(i)

# #4
# def square(a,b):
#     for i in range(a,b):
#         yield i**2

# square1 = square(a = int(input()) , b = int(input()))
# for i in square1:
#     print(i)

#5
def num(n):
        i=0
        while n>=0:
             yield n
             n-=1
numb = num(n= int(input()))
for i in numb:
    print(i)

