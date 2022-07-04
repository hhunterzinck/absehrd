import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'absehrd'
AUTHOR = 'Haley Hunter-Zinck'
AUTHOR_EMAIL = 'haley.s.hunter.zinck@census.gov'
URL = 'https://github.com/hhunterzinck/absehrd'

LICENSE = 'BSD License'
DESCRIPTION = 'Automated Brewing of Electronic Health Record Data'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'pyarrow',
      'matplotlib',
      'numpy',
      'scipy',
      'scikit-learn',
      'torch',
      'tqdm',
      'pandas'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      entry_points ={
            'console_scripts': [
                'absehrd = absehrd.__main__:main'
            ]
      }
      )

