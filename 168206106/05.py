def recur_fibo(n):
   """�ݹ麯��
   ���쳲���������"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
 
# ��ȡ�û�����
nterms = int(input("��Ҫ�������? "))
 
# �������������Ƿ���ȷ
if nterms <= 0:
   print("����������")
else:
   print("쳲���������:")
   for i in range(nterms):
       print(recur_fibo(i))