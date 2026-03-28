from setuptools import find_packages,setup
from typing import List

def get_requiremnts()->List[str]:
    """
    This function will return list of requirements
    """
    requiremnt_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requiremnt = line.strip()
                if requiremnt and requiremnt!='-e .':
                    requiremnt_lst.append(requiremnt)
    
    except FileNotFoundError:
        print("requiremnts.txt file not found")
    
    return requiremnt_lst

setup(
    name="NETWORK SECURITY",
    version="0.0.1",
    author="ADITYA GUPTA",
    author_email="guptaaditya0506@gmail.com",
    packages=find_packages(),
    install_requires = get_requiremnts()
)