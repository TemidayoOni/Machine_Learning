from setuptools import setup, find_packages
from typing import List

hyphen_e = '.e'


# collect the requirements into the requirements.txt file

def get_requirements(path_to_file:str) -> List[:str]:

    requirements = []
    with open(path_to_file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("/n", "") for r in requirements]


        if hyphen_e in requirements:

            requirements.remove(hyphen_e)

    return requirements



setup(
    name = "Ml_project1",
    author= "Temidayo Oni",
    version= '0.0.1',
    author_email='onitemidayo@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)