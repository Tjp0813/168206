
def binSearch(lst, item):
  mid = len(lst) //2
  found = False
  if lst[mid] ==
item:
 found = True
 return found
  if mid == 0:
#mid����0�����ҵ����һ��Ԫ���ˡ�
 found = False
 return found
  else:
 if item > lst[mid]: #�Һ�벿��
   #print(lst[mid:])
   return
binSearch(lst[mid:], item)
 else:
   return
binSearch(lst[:mid], item) #��ǰ�벿��