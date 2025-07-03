from setuptools import find_packages, setup


def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        requirements = [req for req in requirements if req and req != '-e .']
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='MeetInCode',
    author_email='mehtameet115@gmail.com',
    packages=find_packages(), # it will find all the packages in the mlproject directory
    install_requires=get_requirements('requirements.txt') # it will install all the dependencies in the requirements.txt file
)