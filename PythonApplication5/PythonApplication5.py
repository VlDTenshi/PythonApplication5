#3.    ������ 8 �����. ����� �� ������������ (������ �������������)

j=0
for i in range(1,7,1):
    A=float(input(f"sisesta A:"))
    if A>0:
        if int(A)==A: j+=A
print(round(j),)

#4.    ��������� ���������, ��������� �� ����� �������� ����� �� 10 �� 20

for i in range(9,21):
    print(i**2)

#6.    � ���������� �������� N �����.��������� ���������, ������� ���������� ���������� �������������,���������� ������������� � ���������� ����� ����� ��������� �����

j=0
for i in range(1,9,1):
    N=float(input(f"Sisesta arv:"))
    if N<0:
        if int(N)==N: j+=N 
print(round(j),)

#7.    ������� �� ����� �����, ������� � �� ���������� [�,�]

for i in range(135,1135,5):
    if i%10==0:
        print(i)

#8.    ��������� ���������, ������� �������� ������� �������� ���������� �� ������ � ���������� (1 ���� =2,5 ��) ��� �������� ���� �� 1 �� 20 ������.

for i in range(1,21):
	print(f"{i }*{2.5}={i * 2.5}")

#9.    � ���� �� �������������� ����� �������� S ����. ����� ������ ����� ������ ����� N ���?

n=float(input("aastate arv ="))
p=float(input("protsenti ? ="))
s=float(input("kui palju raha ="))

for i in range(int(n)):
    s+=s*(p/100)
print(f"peale {int(n)} aastat su on nii palju raha {s}")

#10.������ � ���������� 10 ���.�������� ����� � ������ ���� � ���������� ������� �� ���

for i in range(1,10):
    a,b=map(int,input().split())
    if a==0 and b==0: break
    else:
        if a>b:
            print(a)
        elif a<b:
            print(b)

#12.� �������, ���������� �� ������ ����, ������� N �����������

n=int(input("sisestage Niidukide kogus "))
m=int(input("sisestage kui palju tootas 1 Niiduk "))
tul=0
for i in range(n):
    tul+=1 
    m+=1/6
print(f"{tul} tundi kogu meeskond tootas",)

#17.Korrustustabel

n=int(input("sisesta n:"))
for i in range(1,10):
    print(f"{n} * {i} ={n * i}")

#24.� ��� �������� �� ������� ������ � ����� N �������� ������. ���������� ������� 
#���� �������� ������.

a=int(input("sisestage opilaste hulk:"))
print("pikkus iga opilaste:")
pikkus=[int(input())for i in range(a)] 
avg_p=sum(pikkus)/a 
print(avg_p," cm kesk")