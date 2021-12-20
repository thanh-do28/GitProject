Ax = int(input())
Ay = int(input())
Bx = int(input())
By = int(input())
Cx = int(input())
Cy = int(input())
print('[', Ax,',' ,Ay,',' ,Bx,',' ,By,',' ,Cx,',' ,Cy,']')

#toa do
print("tọa độ A", "=", (Ax, Ay))
print("tọa độ B", "=", (Bx, By))
print("tọa độ C", "=", (Cx, Cy))

#vecter AB, BC, CA
ABx = (Bx - Ax)
ABy = (By - Ay)
BCx = (Cx - Bx)
BCy = (Cy - By)
CAx = (Ax - Cx)
CAy = (Ay - Cy)
print("vecto AB", '=', (ABx, ABy))
print('vecto BC', '=', (BCx, BCy))
print('vecto CA', '=', (CAx, CAy))

#chung minh tam giac
if (Bx - Ax)/(Cx - Bx) != (By - Ay)/(Cy - By):
	print('ABC là tam giác')
else:
	print('ABC không phải tam giác')

#tính độ dài các cạnh
import math
AB = math.sqrt((BCx - ABx)**2 + (BCy - ABy)**2)
BC = math.sqrt((CAx - BCx)**2 + (CAy - BCy)**2)
CA = math.sqrt((ABx - CAx)**2 + (ABx - CAy)**2)
print(('độ dài các cạnh AB BC CA'), round(AB, 2), round(BC, 2), round(CA,2))

#các góc
import math
A = (((ABx * CAx) + (ABy * CAy)) / (math.sqrt(ABx**2 + ABy**2) * math.sqrt(CAx**2 + CAy**2)))
B = (((ABx * BCx) + (ABy * BCy)) / (math.sqrt(ABx**2 + ABy**2) * math.sqrt(BCx**2 + BCy**2)))
C = (((CAx * BCx) + (CAy * BCy)) / (math.sqrt(CAx**2 + CAy**2) * math.sqrt(BCx**2 + BCy**2)))
print('goc A goc B goc C', round(A, 2), round(B, 2), round(C, 2))

#chứng minh tam giác
if AB**2 + CA*2 == BC**2 or BC**2 + AB**2 == CA**2 or CA**2 + BC**2 == AB**2:
	print('ABC la tam giac vuong')
elif AB == CA or BC == AB or BC== CA:
	print('ABC la tam giac can')
elif AB == BC == CA:
	print('ABC la tam giac deu')
elif A == 0.9 and CA == AB:
	if (B == 0.9 and AB == BC) or (C == 0.9 and CA == BC):
		print('ABC lad tam giac vuong can')
elif C < 0.9 and B < 0.9 and A < 0.9:
	print('ABC laf tam giac nhon')
elif A < 0.9 or B < 0.9 or C < 0.9:
	print('ABC la tam giac tu')
else:
	print('ABC la tam giac thuong')
