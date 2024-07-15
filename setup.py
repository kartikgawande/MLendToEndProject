from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(path:str)->List[str]:
    requirement_list = []
    with open(path) as file_obj:
        requirement_list=file_obj.readlines()
        requirement_list = [req.replace('\n',"") for req in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(name='mle2e',
      version='0.0.7',
      author='Kartik',
      author_email='kartikgawandeonline@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
    )

    