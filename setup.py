try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Learning sorting algorithms through PyGame visualizations.',
    'author':'My name',
    'url':'URL to get it at',
    'download_url':'URL to download at',
    'author_email':'My email',
    'version':'0.1',
    'install_requires':['unittest'],
    'packages':['NAME'],
    'scripts':[],
    'name':'project name'
}

setup(**config)