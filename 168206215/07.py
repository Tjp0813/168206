#ʹ��ѭ��������������
def topoSort(G):
    #��ʼ�����㱻ָ��ڵ���ֵ�
    cnt=dict((u,0) for u in G.keys())
    #��ĳ�ڵ㱻�����ڵ�ָ�򣬸ýڵ������+1
    for u in G:
        for v in G[u]:
            cnt[v]+=1
    #�ռ���ָ����Ϊ0�Ľڵ�,��ʱQֻ��һ���ڵ㣬����ʼ�ڵ�a
    Q=[u for u in cnt.keys() if cnt[u]==0]
    #��¼���
    seq=[]
    while Q:
        s=Q.pop()
        seq.append(s)
        for u in G[s]:
            cnt[u]-=1
            if cnt[u]==0:
                Q.append(u)
    return seq

#�����޻�ͼ���ڽ��ֵ�
G={
    'a':{'b','f'},
    'b':{'c','d','f'},
    'c':{'d'},
    'd':{'e','f'},
    'e':{'f'},
    'f':{}
}

res=topoSort(G)
print(res)