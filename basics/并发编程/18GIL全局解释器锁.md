### GIL全局解释器锁

Ps：博客园密码：xiaoyuanqujing@666

```python
"""
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple 
native threads from executing Python bytecodes at once. This lock is necessary mainly 
because CPython’s memory management is not thread-safe. (However, since the GIL 
exists, other features have grown to depend on the guarantees that it enforces.)
"""
"""
python解释器其实有多个版本
	Cpython
	Jpython
	Pypypython
但是普遍使用的都是CPython解释器

在CPython解释器中GIL是一把互斥锁，用来阻止同一个进程下的多个线程的同时执行
	同一个进程下的多个线程无法利用多核优势！！！
	疑问:python的多线程是不是一点用都没有？？？无法利用多核优势
	
因为cpython中的内存管理不是线程安全的
内存管理(垃圾回收机制)
	1.应用计数
	2.标记清楚
	3.分代回收
	
"""

"""
重点:
	1.GIL不是python的特点而是CPython解释器的特点
	2.GIL是保证解释器级别的数据的安全
	3.GIL会导致同一个进程下的多个线程的无法同时执行即无法利用多核优势(******)
	4.针对不同的数据还是需要加不同的锁处理 
	5.解释型语言的通病:同一个进程下多个线程无法利用多核优势
"""
```
