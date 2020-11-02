from __future__ import absolute_import

import os
import yaml

__version__ = '0.0.2'

__yaml_ext__ = ('.yml', '.yaml')
__test_yaml_file__ = os.path.join(__path__[0], "test.yaml")
__temp_yaml_file__ = "./temp.yaml"


def _is_valid_key(key:str, invalid_key_list:list=None) -> None:
    if not (isinstance(key, str) and key and key.replace('_', '').isalnum() and not key[0].isdecimal()) \
        or (invalid_key_list and key in invalid_key_list):
        raise KeyError("Invalid Key: %s"%(key))

def _is_valid_value(value):
    if not isinstance(value, (type(None), str, int, float, tuple, list, dict)):
        raise TypeError("Invalid Value: %s"%(str(value)))

def _idx2key(idx):
    return "_%d"%(idx)

def _key2idx(key):
    return int(key[1:])

class YamlDict(dict):
    def __init__(self, d:dict=None, **kwargs):
        d = d or {}
        d.update(**kwargs)
        
        for k, v in d.items():
            setattr(self, k, v)
    
    def __setattr__(self, key:str, value):
        _is_valid_key(key, dict.__dict__.keys())
        _is_valid_value(value)
        if isinstance(value, (tuple, list)):
            value = YamlList(value)
            # value = YamlList([self.__class__(x) 
            #                     if isinstance(x, dict) else x for x in value])
        elif isinstance(value, dict):
            value = self.__class__(value)
        super(YamlDict, self).__setattr__(key, value)
        super(YamlDict, self).__setitem__(key, value)

    __setitem__ = __setattr__

    def update(self, d:dict=None, **kwargs):
        d = d or {}
        d.update(kwargs)
        for k, v in d.items():
            setattr(self, k, v)

    def pop(self, k:str, default=None):
        delattr(self, k)
        return super(YamlDict, self).pop(k, default)

    def clear(self):
        for k in self.keys():
            delattr(self, k)
        super(YamlDict, self).clear()

    def to_dict(self):
        d = {}
        for k, v in self.items():
            if isinstance(v, list):
                # v = [x.to_dict() if isinstance(x, dict) else x for x in v]
                v = v.to_list()
            elif isinstance(v, dict):
                v = v.to_dict()
            d[k] = v
        return d

class YamlList(list): 
    def __init__(self, it=None):
        it = it or []
        for idx, v in enumerate(it):
            self.append(v)

    def __setitem__(self, idx:int, value):
        _is_valid_value(value)
        key = _idx2key(idx)
        if isinstance(value, (tuple, list)):
            value = self.__class__(value)
        elif isinstance(value, dict):
            value = YamlDict(value)
        super(YamlList, self).__setattr__(key, value)
        super(YamlList, self).__setitem__(idx, value)

    def __setattr__(self, key:str, value):
        _is_valid_value(value)
        idx = _key2idx(key)
        if isinstance(value, (tuple, list)):
            value = self.__class__(value)
        elif isinstance(value, dict):
            value = YamlDict(value)
        super(YamlList, self).__setattr__(key, value)
        super(YamlList, self).__setitem__(idx, value)

    def append(self, v):
        super(YamlList, self).append(v)
        setattr(self, _idx2key(len(self)-1), v)

    def pop(self, index:int=None):
        idx = index or len(self)-1
        for i in range(idx, len(self)-1):
            self[i] = self[i+1]
        delattr(self, _idx2key(len(self)-1))
        super(YamlList, self).pop()

    def to_list(self):
        l = []
        for v in self:
            if isinstance(v, list):
                v = v.to_list()
            elif isinstance(v, dict):
                v = v.to_dict()
            l.append(v)
        return l


def load(yaml_file):
    assert isinstance(yaml_file, str) and os.path.isfile(yaml_file) and os.path.splitext(yaml_file)[-1] in __yaml_ext__, "invalid file: %s"%(yaml_file)
    with open(yaml_file, 'r') as foo:
        yaml_data = yaml.load(foo)

    if isinstance(yaml_data, list):
        return YamlList(yaml_data)
    elif isinstance(yaml_data, dict):
        return YamlDict(yaml_data)

def save(yaml_file, yaml_data): 
    assert isinstance(yaml_file, str)

    if isinstance(yaml_data, list):
        yaml_data = yaml_data.to_list()
    elif isinstance(yaml_data, dict):
        yaml_data = yaml_data.to_dict()

    with open(yaml_file, 'w') as foo:
        yaml.dump(yaml_data, foo)

def show(yaml_data):
    assert isinstance(yaml_data, (list, tuple, YamlList, YamlDict)), "invalid input"
    import shutil
    columns = shutil.get_terminal_size().columns
    print("YAML_DATA".center(columns, "="))

    if isinstance(yaml_data, (list, YamlList)):
        for x in yaml_data:
            print("%s"%(x))
    elif isinstance(yaml_data, (dict, YamlDict)):
        max_key_len = max([len(k) for k in yaml_data.keys()])
        for k, v in yaml_data.items():
            print("%s: %s"%(k.ljust(max_key_len), v))
    print()


def test(dst_file, src_file):
    yd = load(src_file)
    print(yd)
    save(dst_file, yd)
    show(yd)


if __name__ == '__main__':
    test("./temp.yaml", __test_yaml_file__)

    