from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Remove newline chars

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject1',
    version='0.0.1',
    author='Aniket',
    author_email='aniketsah2019@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # ✅ correct spelling
)
