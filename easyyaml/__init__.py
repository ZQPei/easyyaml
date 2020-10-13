import os
import yaml
from easydict import EasyDict as edict

__version__ = '0.0.1'

_yaml_ext = ('.yml', '.yaml')

class EasyYaml(edict, list):
    def __init__(self, config=None):
        assert isinstance(config, (str, dict)), "Value Type Error"

        if isinstance(config, str):
            assert os.path.isfile(config) and os.path.splitext(config)[-1] in _yaml_ext
            with open(config, 'r') as foo:
                _dict = yaml.load(foo)
                if 

        elif isinstance(config, edict):
            _dict = config
        else:
            _dict = config

    


def load(): ...


def dump(): ...


def update(): ...


def pop(): ...


if __name__ == '__main__':
    ...
    