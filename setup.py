from setuptools import setup, find_packages

setup(
  name = 'django-jssor',
  packages=find_packages(),
  version = '0.1.2',
  description = 'Jssor slideshow for Django',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-jssor', # use the URL to the github repo
  download_url = 'https://github.com/synw/django-jssor/releases/tag/0.1', # I'll explain this in a second
  keywords = ['django', 'slideshow', 'jssor'], # arbitrary keywords
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  install_requires=[
        "Django >= 1.8.0",
        'Pillow'
    ],
  zip_safe=False
)
