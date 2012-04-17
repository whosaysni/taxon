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
    """Classifies object as a tuple of type, module, class, object itself.

    >>> classify(int)
    ('class', '__builtin__', 'int', 'int')
    >>> classify(int.__add__)
    ('methoddescriptor', '__builtin__', 'int', '__add__')
    >>> import json
    >>> classify(json)
    ('module', 'json', 'module', 'json')
    >>> classify(json.dumps)
    ('function', 'json', 'function', 'dumps')
    >>> classify(1)
    ('instance', '__builtin__', 'int', '0x...')

    """

    typename = None
    modulename = None
    classname = None
    objname = None

    if ismodule(obj):
        typename = 'module'
        modulename = obj.__name__
        classname = type(obj).__name__
        objname = modulename
    elif isclass(obj):
        typename = 'class'
        modulename = obj.__module__
        classname = obj.__name__
        objname = classname
    elif ismethod(obj):
        typename = 'method'
        cls = obj.im_class
        modulename = cls.__module__
        classname = cls.__name__
        objname = obj.__name__
    elif isfunction(obj):
        typename = 'function'
        modulename = obj.__module__
        classname = type(obj).__name__
        objname = obj.__name__
    elif isbuiltin(obj):
        typename = 'builtin'
        instance = getattr(obj, '__self__', None)
        if instance:
            cls = instance.__class__
            modulename = cls.__module__
            classname = cls.__name__
        else:
            modulename = obj.__module__
            classname = type(obj).__name__
        objname = obj.__name__
    elif ismethoddescriptor(obj):
        typename = 'methoddescriptor'
        cls = obj.__objclass__
        modulename = cls.__module__
        classname = cls.__name__
        objname = getattr(obj, '__name__', '')
    elif isdatadescriptor(obj):
        typename = 'datadescriptor'
        cls = obj.__objclass__
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
        # umm, I cannot figure how to treat this...
        typename = 'memberdescriptor'
        cls = getattr(obj, 'im_class')
        if cls:
            modulename = cls.__module__
            classname = cls.__name__
        else:
            classname = type(obj).__name__
        objname = getattr(obj, '__name__', '')
    else:
        # object can be an instance
        cls = getattr(obj, '__class__', None)
        if cls:
            typename = 'instance'
            classname = cls.__name__
            modulename = cls.__module__
        else:
            typename = 'undefined'
    # fallback stuff
    if objname is None:
        if obj is None:
            objname = 'None'
        elif obj is True:
            objname = 'True'
        elif obj is False:
            objname = 'False'
        else:
            objname = hex(id(obj))
    return (typename, modulename, classname, objname)
            
    
if __name__=='__main__':
    from doctest import *
    testmod(optionflags=ELLIPSIS)
