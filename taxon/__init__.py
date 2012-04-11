# coding: utf-8
"""Taxon: simple object taxonomy.
"""

from inspect import (
    getmodulename, 
    ismodule, isclass, ismethod, isfunction, istraceback,
    isframe, iscode, isbuiltin, isroutine,
    ismethoddescriptor, isdatadescriptor, isgetsetdescriptor,
    ismemberdescriptor)

try:
    from inspect import (
        isgeneratorfunction, isgenerator, isabstract)
except ImportError:
    _never = lambda o: False
    isgeneratorfunction = _never
    isgenerator = _never
    isabstract = _never
    del _never


def classify(obj):
    """Classifies returns a tuple of names of type, module, class, and the object. 

    >>> classify(int)
    ('class', '__builtin__', 'int', None)
    >>> classify(int.__add__)
    ('routine', '__builtin__', 'int', '__add__')
    >>> import os
    >>> classify(os)
    ('module', 'os', None, None)
    >>> classify(os.path)
    ('module', ..., None, None)
    >>> classify(os.path.isdir)
    ('function', ..., None, 'isdir')

    """

    typename = None
    modulename = None
    classname = None
    objname = None

    if ismodule(obj):
        typename = 'module'
        modulename = obj.__name__
    elif isclass(obj):
        typename = 'class'
        modulename = obj.__module__
        classname = obj.__name__
    elif isabstract(obj):
        typename = 'abstract'
        modulename = obj.__module__
        classname = obj.__name__
    elif ismethod(obj):
        typename = 'method'
        cls = obj.im_class
        modulename = cls.__module__
        classname = cls.__name__
        objname = obj.__name__
    elif isfunction(obj):
        typename = 'function'
        modulename = obj.__module__
        objname = obj.__name__
    elif isgeneratorfunction(obj):
        typename = 'generatorfunction'
        modulename = obj.__module__
        objname = obj.__name__
    elif isgenerator(obj):
        typename = 'generatorfunction'
        code = obj.gi_code
        objname = code.co_name
    elif istraceback(obj):
        typename = 'traceback'
        frame = obj.tb_frame
        code = frame.f_code
        objname = code.co_name
    elif isframe(obj):
        typename = 'frame'
        code = frame.f_code
        objname = code.co_name
    elif isbuiltin(obj):
        # should never reach here
        typename = 'builtin'
        modulename = obj.__module__
        instance = getattr(obj, '__self__', None)
        if instance:
            cls = instance.__class__
            modulename = cls.__module__
            classname = cls.__name__
        objname = obj.__name__
    elif isroutine(obj):
        # should never reach here
        typename = 'routine'
        instance = getattr(obj, '__self__', None)
        cls = None
        if instance:
            cls = instance.__class__
        else:
            cls = getattr(obj, '__objclass__', None)
        if cls:
            modulename = cls.__module__
            classname = cls.__name__
        objname = obj.__name__
    elif ismethoddescriptor(obj):
        typename = 'methoddescriptor'
        cls = obj.__get__.im_class
        modulename = cls.__module__
        classname = cls.__name__
        objname = getattr(obj, '__name__', '')
    elif isdatadescriptor(obj):
        typename = 'datadescriptor'
        cls = obj.__set__.im_class
        modulename = cls.__module__
        classname = cls.__name__
        objname = getattr(obj, '__name__', '')
    elif isgetsetdescriptor(obj):
        typename = 'getsetdescriptor'
        cls = obj.__set__.im_class
        modulename = cls.__module__
        classname = cls.__name__
        objname = getattr(obj, '__name__', '')
    elif ismemberdescriptor(obj):
        # umm, I don't figure how to treat this...
        typename = 'memberdescriptor'
        cls = getattr(obj, 'im_class')
        if cls:
            modulename = cls.__module__
            classname = cls.__name__
        objname = getattr(obj, '__name__', '')
    else:
        typename = 'undefined'
    return (typename, modulename, classname, objname)
            
    
if __name__=='__main__':
    from doctest import *
    testmod(optionflags=ELLIPSIS)
