import easyyaml as eyaml

def main():
    yaml_file = "./example.yaml"
    yd = eyaml.load(yaml_file)
    print(yd)
    eyaml.save("./temp.yaml", yd)

if __name__ == '__main__':
    main()
    
