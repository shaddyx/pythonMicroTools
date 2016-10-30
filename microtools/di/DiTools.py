import new
import os
import sys
def getSimpleNameFromString(obj):
    return obj.split(".")[-1]

def getSimpleClassNameFromObject(obj):
    # type: (object) -> str
    tp = type(obj)
    if tp is new.classobj or tp is type:
        return getSimpleNameFromString(obj.__name__)
    elif tp is str:
        return obj
    elif tp is new.instance:
        return getSimpleNameFromString(obj.__class__.__name__)
    raise Exception("Cannot get className for object:" + str(type(obj)))


def getObjectPackage(obj):
    if type(obj) is str:
        return obj
    mod = sys.modules[obj.__module__]
    dir = os.path.dirname(mod.__file__)
    return ".".join(dir.split(os.pathsep))

def getFullyQualifiedName(obj):
    result = []
    package = getObjectPackage(obj)
    if package:
        result.append(package)
    result.append(getSimpleClassNameFromObject(obj))
    return ".".join(result)

def getScope(scopeHolder):
    if hasattr(scopeHolder, "__scope"):
        return scopeHolder.__scope
    raise Exception("Error, object is not scopeHolder:" + scopeHolder)
