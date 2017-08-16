def locked_method(method):
    """Method decorator. Requires a lock object at self._lock"""
    def newmethod(self, *args, **kwargs):
        with self._lock:
            return method(self, *args, **kwargs)
    return newmethod

class DecoratorLockedSet(set):
    def __init__(self, *args, **kwargs):
        self._lock = Lock()
        super(DecoratorLockedSet, self).__init__(*args, **kwargs)

    @locked_method
    def add(self, *args, **kwargs):
        return super(DecoratorLockedSet, self).add(elem)

    @locked_method
    def remove(self, *args, **kwargs):
        return super(DecoratorLockedSet, self).remove(elem)