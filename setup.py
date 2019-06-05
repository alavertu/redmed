from setuptools import setup
setup(
  name = 'redmed',
  packages = ['redmed'],
  version = '0.1.3',
  description = 'Lexicon and associated tools for identifying drug mentions in social media data',
  author = 'Adam Lavertu',
  author_email = 'adamlavertu@gmail.com',
  url = 'https://github.com/alavertu/redmed',
  download_url = 'https://github.com/alavertu/redmed.git',
  keywords = ['pharmacovigilance', 'lexicon', 'text analysis', 'drugs', 'social media data'],
  package_data= { 'redmed': ['data/redmed_drug_lexicon.tsv', "data/redmed_phrases.txt"]},
  classifiers = [],
  include_package_data=True,
)
