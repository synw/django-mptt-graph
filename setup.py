from setuptools import setup, find_packages


version = __import__('mptt_graph').__version__

setup(
  name = 'django-mptt-graph',
  packages=find_packages(),
  include_package_data=True,
  version = version,
  description = 'Graphical representation of mptt models',
  author = 'synw',
  author_email = 'synwe@yahoo.com',
  url = 'https://github.com/synw/django-mptt-graph', 
  download_url = 'https://github.com/synw/django-mptt-graph/releases/tag/'+version, 
  keywords = ['django', 'mptt'], 
  classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
  zip_safe=False
)
