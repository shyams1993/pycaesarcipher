from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'pycaesarcipher',
  packages = ['pycaesarcipher'],
  version = '1.0',
  license='MIT',
  description = "Python library to encipher & decipher a string using one of the simplest Substitution ciphers - 'Caesar's Cipher'",
  author = 'SHYAM SALIL',
  author_email = 'shyamsalil1993@gmail.com',
  url = 'https://github.com/shyams1993/pycaesarcipher',
  download_url = 'https://github.com/shyams1993/pycaesarcipher/archive/v1.0.tar.gz',
  keywords = ['SIMPLE', 'ELEGANT', 'YET CRYPTIC'],
  install_requires=['None'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',  
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
  ],
)