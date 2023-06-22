from setuptools import find_packages, setup
from typing import List

hyphen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''function to return requirements'''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements        

setup(
    name='mlproject',
    version='0.0.1',
    author='Makina',
    author_email='makinamulimbika0928@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')

)