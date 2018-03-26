try:
    import cPickle as pickle
except ImportError:
    import pickle

d=dict(url='index.html',title='首页',content='首页')
'''
pickle.dumps(d)         #dumps方法，将任意对象序列化成一个str
f=open(r'E:\workspace\。。。.txt','wb')
pickle.dump(d,f)        #dump方法，将序列化后的对象直接写入文件
f.close()
'''
f=open(r'E:\workspace\。。。.txt','rb')
d=pickle.load(f)
f.close()
d

