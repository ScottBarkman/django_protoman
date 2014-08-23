from distutils.core import setup
setup(
  name = 'protoman',
  packages = ['protoman'], # this must be the same as the name above
  version = '0.1',
  description = 'Simple django app to help with prototyping',
  author = 'Scott Barkman',
  author_email = 'scottbarkman@gmail.com',
  url = 'https://github.com/ScottBarkman/django-protoman', # use the URL to the github repo
  download_url = 'https://github.com/ScottBarkman/django-protoman/tarball/{tag}', # I'll explain this in a second
  keywords = ['prototyping', 'prototype', 'helper'], # arbitrary keywords
  classifiers = [],
)
