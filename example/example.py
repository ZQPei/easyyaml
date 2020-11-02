import easyyaml as eyaml


def main():
    yd = eyaml.load(eyaml.__test_yaml_file__)
    for _ in range(4):
        yd.list.pop()
    yd.name = "this_is_a_simple_example_of_eyaml"
    eyaml.save(eyaml.__temp_yaml_file__, yd)
    eyaml.show(yd)


if __name__ == '__main__':
    main()
    
