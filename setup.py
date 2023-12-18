from setuptools import find_packages,setup
from typing import List
packages=find_packages()
Hyphen_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will returns the requirements
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hyphen_dot in requirements:
            requirements.remove(Hyphen_dot)
    return requirements


setup(
name ='mlproject',
author= 'Jay Shankar',
version='0.0.1',
author_email = 'jassshankar79@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
) 