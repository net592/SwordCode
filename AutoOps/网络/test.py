def foo(*args,**kwargs):
    print('args is',args)
    print('kwargs is',kwargs)
    
foo(1,2,3, {"name": 111}, name=1)