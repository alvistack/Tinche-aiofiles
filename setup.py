# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aiofiles', 'aiofiles.tempfile', 'aiofiles.threadpool']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiofiles',
    'version': '23.1.0',
    'description': 'File support for asyncio.',
    'author': 'Tin Tvrtkovic',
    'author_email': 'tinchester@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Tinche/aiofiles',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
