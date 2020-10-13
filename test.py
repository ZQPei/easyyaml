import yaml
from easyyaml.easydict import EasyDict as edict

def main():
    f = "./test.yaml"
    with open(f, 'r') as foo:
        d = yaml.load(foo)

    import ipdb; ipdb.set_trace()

    ed = edict(d[0])

if __name__ == "__main__":
    main()

