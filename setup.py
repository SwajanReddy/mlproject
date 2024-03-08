# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [x.replace('\n',"") for x in req]
        
        if "-e." in req:
            req.remove("-e.")
            
    return req


setup(
      name='mlproject',
      version='0.0.1',
      author='Swajan',
      author_email='swajan.edu@gmail.com',
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')
      )

