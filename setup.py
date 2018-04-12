from distutils.core import setup

setup(
    name='aiodisk',
    packages=['aiodisk'],  # this must be the same as the name above
    version='0.1.alpha3',
    description='Access all cloud services in one script',
    author='Oguz BAKIR',
    author_email='worms298@gmail.com',
    url='https://github.com/oguzbakir/AioDisk',  # use the URL to the github repo
    download_url='https://github.com/oguzbakir/aiodisk/archive/0.1.tar.gz',
    keywords=['drive', 'mega', 'cloud', 'cloudaio'],  # arbitrary keywords
    classifiers=['Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6'],
    install_requires=[
        'google-api-python-client',
    ],
)
