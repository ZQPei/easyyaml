# EasyYaml

## Introduction

This is an easy library for loading, editing and saving yaml objects.

## Installation

You can install this project by a simple command.
```bash
    pip install easyyaml
```

## QuickStart

It is quite simple to manipulate the yaml object.
```python
>>> yd = eyaml.load(eyaml.__test_yaml_file__)
>>> for _ in range(4):
        yd.list.pop()
>>> yd.name = "this_is_a_simple_example_of_eyaml"
>>> eyaml.save(eyaml.__temp_yaml_file__, yd)
```

