from setuptools import setup
from m2_kernel import __version__


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='passagemath-macaulay2-jupyterkernel',
    version=__version__,
    packages=['m2_kernel'],
    description='Jupyter kernel for Macaulay2 (passagemath fork)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Radoslav Zlatev',
    author_email='radoslav@math.cornell.edu',
    maintainer='Matthias Koeppe and passagemath contributors',
    url='https://github.com/passagemath/passagemath-macaulay2-jupyterkernel',
    # packages=find_packages(),
    install_requires=['ipykernel', 'notebook', 'pexpect', 'passagemath-macaulay2'],
    include_package_data=True,
    package_data={'m2_kernel': [
        'assets/m2-mode/*', 'assets/m2-code/*', 'assets/m2-spec/*']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License'
    ]
)
