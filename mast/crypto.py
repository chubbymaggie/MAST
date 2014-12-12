from hashlib import sha256

class hashable:
    def __init__(self, data):
        self.data = data
        self.h = hash(str(data))
    def __str__(self):
        return "{data:%s\n,hash:%s}"%(self.data, self.h)
    def hash(self):
        return self.h
class ishash:
    def __init__(self, data):
        self.data = data
    def hash(self):
        return self.data
    def __str__(self):
        return "{hash:%s}"%(self.data)
def hash(s):
    return sha256(s).hexdigest()

def hashArr(arr):
    return hash("".join(map(str, arr)))

def verify(c, h):
    return hash(c) == h
def ripemd160(s):
    h = hashlib.new('ripemd160')
    h.update(s)
    return h.hexdigest()
def sha1(s):
    return sha1(s).hexdigest()
