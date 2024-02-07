#div of two numbers

a=int(input("enter first number here:"))
b=int(input("enter second number here:"))
if type((a)==int or float):
	if(type(b)==int or float):
		div=(float(a)/float(b))
		print("div=",div)
else:
	print("error")
	





#FIND THE DOT PRODUCT OF TWO VECTORS

l=[]
m=[]
s=0
n=int(input("enter the length of the vector"))
for i in range(n):
	a=int(input("enter a number"))
	b=int(input("enter the number"))
	l.append(a)
	m.append(b)
print("list l=",l)
print("list m=",m)
for i in range(len(l)):
	s=s+l[i]*m[i]
print(s)


'''a=[1,2,3]
b=[3,4,5]
dot_product=sum(x*y for x,y in zip(a,b))
print("dot_product",dot_product)'''




#DET OF THE MATRIX.....CHECK WWTHER IT IS A SQUARE MATRIX.
r=int(input("enter the number"))
c=int(input("enter the number"))
matrix=[]
print("entre the row here:")
for i in range(r):
	a=[]
	for j in range(r):
		a.append(int(input())
	matrix.append(a)
for i in range(r):
	for j in range(c):
		print(matrix[i][j],end="")
	print()
det=matrix[0][0]*matrix[1][2]-matrix[1][0]*matrix[0][1]
print("det of the matrix is:",det)


'''matrix=[[1,2],[3,5]]
det=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
print(det)'''





















