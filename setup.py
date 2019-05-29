from setuptools import setup
setup(
  name = 'redmed',
  packages = ['redmed'],
  version = '1.0',
  description = 'Lexicon and associated tools for identifying drug mentions in social media data',
  author = 'Adam Lavertu',
  author_email = 'adamlavertu@gmail.com',
  url = 'https://github.com/alavertu/redmed',
  download_url = 'https://github.com/alavertu/redmed.git',
  keywords = ['pharmacovigilance', 'lexicon', 'text analysis', 'drugs', 'social media data'],
  #package_data= { 'empath': ['data/lexicon.txt', "data/user/blank"]}, Update with path to lexicon once finalized
  classifiers = [],
  install_requires=[
          'requests'
  ]
)