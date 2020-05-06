from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'CaesarCipher-shyams_1993',
  packages = ['CaesarCipher'],
  version = '1.0',
  license='MIT',
  description = "Python library to encipher & decipher a string using one of the simplest Substitution ciphers - 'Caesar's Cipher'",
  author = 'SHYAM SALIL',
  author_email = 'shyamsalil1993@gmail.com',
  url = 'https://github.com/shyams1993/CaesarCipher',
  download_url = 'https://github.com/shyams1993/CaesarCipher/archive/v1.0.tar.gz',
  keywords = ['SIMPLE', 'ELEGANT', 'YET CRYPTIC'],
  install_requires=['None'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3+',      #Specify which pyhton versions that you want to support
  ],
)