from setuptools import setup

setup(
    name='easyyaml',
    version='0.0.1',
    author='ZQPei',
    author_email='dfzspzq@163.com',
    packages=['easyyaml'],
    install_requires=[
        "pyyaml",
        ],
    # scripts=['utils/build_server_scripts'],
    url='https://github.com/ZQPei/easyyaml',
    description='Easy yaml parser and editer',
    long_description=open('./README.md', 'r').read(), 
    long_description_content_type="text/markdown",
    platforms=["all"],
    license='MIT',
)