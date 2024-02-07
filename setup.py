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
    'version': '0.8.0',
    'description': 'File support for asyncio.',
    'long_description': 'aiofiles: file support for asyncio\n==================================\n\n.. image:: https://img.shields.io/pypi/v/aiofiles.svg\n        :target: https://pypi.python.org/pypi/aiofiles\n\n.. image:: https://travis-ci.org/Tinche/aiofiles.svg?branch=master\n        :target: https://travis-ci.org/Tinche/aiofiles\n\n.. image:: https://codecov.io/gh/Tinche/aiofiles/branch/master/graph/badge.svg\n        :target: https://codecov.io/gh/Tinche/aiofiles\n\n.. image:: https://img.shields.io/pypi/pyversions/aiofiles.svg\n        :target: https://github.com/Tinche/aiofiles\n        :alt: Supported Python versions\n\n**aiofiles** is an Apache2 licensed library, written in Python, for handling local\ndisk files in asyncio applications.\n\nOrdinary local file IO is blocking, and cannot easily and portably made\nasynchronous. This means doing file IO may interfere with asyncio applications,\nwhich shouldn\'t block the executing thread. aiofiles helps with this by\nintroducing asynchronous versions of files that support delegating operations to\na separate thread pool.\n\n.. code-block:: python\n\n    async with aiofiles.open(\'filename\', mode=\'r\') as f:\n        contents = await f.read()\n    print(contents)\n    \'My file contents\'\n\nAsynchronous iteration is also supported.\n\n.. code-block:: python\n\n    async with aiofiles.open(\'filename\') as f:\n        async for line in f:\n            ...\n\nAsynchronous interface to tempfile module.\n\n.. code-block:: python\n\n    async with aiofiles.tempfile.TemporaryFile(\'wb\') as f:\n        await f.write(b\'Hello, World!\')\n\n\nFeatures\n--------\n\n- a file API very similar to Python\'s standard, blocking API\n- support for buffered and unbuffered binary files, and buffered text files\n- support for ``async``/``await`` (:PEP:`492`) constructs\n- async interface to tempfile module\n\n\nInstallation\n------------\n\nTo install aiofiles, simply:\n\n.. code-block:: bash\n\n    $ pip install aiofiles\n\nUsage\n-----\n\nFiles are opened using the ``aiofiles.open()`` coroutine, which in addition to\nmirroring the builtin ``open`` accepts optional ``loop`` and ``executor``\narguments. If ``loop`` is absent, the default loop will be used, as per the\nset asyncio policy. If ``executor`` is not specified, the default event loop\nexecutor will be used.\n\nIn case of success, an asynchronous file object is returned with an\nAPI identical to an ordinary file, except the following methods are coroutines\nand delegate to an executor:\n\n* ``close``\n* ``flush``\n* ``isatty``\n* ``read``\n* ``readall``\n* ``read1``\n* ``readinto``\n* ``readline``\n* ``readlines``\n* ``seek``\n* ``seekable``\n* ``tell``\n* ``truncate``\n* ``writable``\n* ``write``\n* ``writelines``\n\nIn case of failure, one of the usual exceptions will be raised.\n\nThe ``aiofiles.os`` module contains executor-enabled coroutine versions of\nseveral useful ``os`` functions that deal with files:\n\n* ``stat``\n* ``sendfile``\n* ``rename``\n* ``replace``\n* ``remove``\n* ``mkdir``\n* ``makedirs``\n* ``rmdir``\n* ``removedirs``\n* ``path.exists``\n* ``path.isfile``\n* ``path.isdir``\n* ``path.getsize``\n* ``path.getatime``\n* ``path.getctime``\n* ``path.samefile``\n* ``path.sameopenfile``\n\nTempfile\n~~~~~~~~\n\n**aiofiles.tempfile** implements the following interfaces:\n\n- TemporaryFile\n- NamedTemporaryFile\n- SpooledTemporaryFile\n- TemporaryDirectory\n\nResults return wrapped with a context manager allowing use with async with and async for.\n\n.. code-block:: python\n\n    async with aiofiles.tempfile.NamedTemporaryFile(\'wb+\') as f:\n        await f.write(b\'Line1\\n Line2\')\n        await f.seek(0)\n        async for line in f:\n            print(line)\n\n    async with aiofiles.tempfile.TemporaryDirectory() as d:\n        filename = os.path.join(d, "file.ext")\n\n\nWriting tests for aiofiles\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nReal file IO can be mocked by patching ``aiofiles.threadpool.sync_open``\nas desired. The return type also needs to be registered with the\n``aiofiles.threadpool.wrap`` dispatcher:\n\n.. code-block:: python\n\n    aiofiles.threadpool.wrap.register(mock.MagicMock)(\n        lambda *args, **kwargs: threadpool.AsyncBufferedIOBase(*args, **kwargs))\n\n    async def test_stuff():\n        data = \'data\'\n        mock_file = mock.MagicMock()\n\n        with mock.patch(\'aiofiles.threadpool.sync_open\', return_value=mock_file) as mock_open:\n            async with aiofiles.open(\'filename\', \'w\') as f:\n                await f.write(data)\n\n            mock_file.write.assert_called_once_with(data)\n\nHistory\n~~~~~~~\n0.8.0 (2021-11-27)\n``````````````````\n* aiofiles is now tested on Python 3.10.\n* Added ``aiofiles.os.replace``.\n  `#107 <https://github.com/Tinche/aiofiles/pull/107>`_\n* Added ``aiofiles.os.{makedirs, removedirs}``.\n* Added ``aiofiles.os.path.{exists, isfile, isdir, getsize, getatime, getctime, samefile, sameopenfile}``.\n  `#63 <https://github.com/Tinche/aiofiles/pull/63>`_\n* Added `suffix`, `prefix`, `dir` args to ``aiofiles.tempfile.TemporaryDirectory``.\n  `#116 <https://github.com/Tinche/aiofiles/pull/116>`_\n\n0.7.0 (2021-05-17)\n``````````````````\n- Added the ``aiofiles.tempfile`` module for async temporary files.\n  `#56 <https://github.com/Tinche/aiofiles/pull/56>`_\n- Switched to Poetry and GitHub actions.\n- Dropped 3.5 support.\n\n0.6.0 (2020-10-27)\n``````````````````\n- `aiofiles` is now tested on ppc64le.\n- Added `name` and `mode` properties to async file objects.\n  `#82 <https://github.com/Tinche/aiofiles/pull/82>`_\n- Fixed a DeprecationWarning internally.\n  `#75 <https://github.com/Tinche/aiofiles/pull/75>`_\n- Python 3.9 support and tests.\n\n0.5.0 (2020-04-12)\n``````````````````\n- Python 3.8 support. Code base modernization (using ``async/await`` instead of ``asyncio.coroutine``/``yield from``).\n- Added ``aiofiles.os.remove``, ``aiofiles.os.rename``, ``aiofiles.os.mkdir``, ``aiofiles.os.rmdir``.\n  `#62 <https://github.com/Tinche/aiofiles/pull/62>`_\n\n\n0.4.0 (2018-08-11)\n``````````````````\n- Python 3.7 support.\n- Removed Python 3.3/3.4 support. If you use these versions, stick to aiofiles 0.3.x.\n\n0.3.2 (2017-09-23)\n``````````````````\n- The LICENSE is now included in the sdist.\n  `#31 <https://github.com/Tinche/aiofiles/pull/31>`_\n\n0.3.1 (2017-03-10)\n``````````````````\n\n- Introduced a changelog.\n- ``aiofiles.os.sendfile`` will now work if the standard ``os`` module contains a ``sendfile`` function.\n\nContributing\n~~~~~~~~~~~~\nContributions are very welcome. Tests can be run with ``tox``, please ensure\nthe coverage at least stays the same before you submit a pull request.\n',
    'author': 'Tin Tvrtkovic',
    'author_email': 'tinchester@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
