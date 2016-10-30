import copy
import os
import sys
from threading import RLock

from microtools.di import DiTools

_services={}  # type: dict[str, classobj]
class ScopeContext(object):
    def __init__(self):
        self.__instances = {}
        self.scopeLock = RLock()
        self.services = {}

    def resolveClass(self, name):
        pkg = DiTools.getObjectPackage(name)
        if pkg not in _services:
            raise Exception("Error, no class with name {pkg} registered, available:{keys}".format(pkg=pkg, keys=_services.keys()))
        return _services[pkg]

    def makeInstance(self, cls):
        instance = cls()
        instance.contextScope = self
        if hasattr(instance, "_inject"):
            instance._inject()
        return instance

    def getInstance(self, name):
        name = DiTools.getFullyQualifiedName(name)
        if name in self.__instances:
            return self.__instances[name]
        self.scopeLock.acquire()
        cls = self.resolveClass(name)
        if name not in self.__instances:
            self.__instances[name] = self.makeInstance(cls)

        self.scopeLock.release()
        return self.__instances[name]

    @staticmethod
    def configure(params):
        appContext = ScopeContext()
        appContext._services = copy.copy(_services)
        appContext.params = params

def InjectClass(**kwargs_):
    def decorator(cls):
        def inject(self):
            for name in kwargs_:
                setattr(self, name, self.contextScope.getInstance(kwargs_[name]))
        cls._inject =inject
        return cls
    return decorator

def Service():
    def decorator(cls):
        _services[DiTools.getFullyQualifiedName(cls)] = cls
        return cls
    return decorator