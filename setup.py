from setuptools import setup

setup(
    name='easyyaml',
    version='0.0.4.1',
    author='ZQPei',
    author_email='dfzspzq@163.com',
    packages=['easyyaml'],
    install_requires=[
        "pyyaml",
        ],
    url='https://github.com/ZQPei/easyyaml',
    include_package_data=True,
    description='Easy yaml parser and editer',
    long_description=open('./README.md', 'r').read(), 
    long_description_content_type="text/markdown",
    platforms=["all"],
    license='MIT',
)