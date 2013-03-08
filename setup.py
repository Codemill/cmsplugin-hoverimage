from setuptools import setup, find_packages

version = __import__('cmsplugin_hoverimage').__version__

setup(
    name = 'cmsplugin-hoverimage',
    version = version,
    description = 'Plugin for Django CMS that displays a image that changes on hover.',
    author = 'Ludvig Widman, CodeMill AB',
    author_email = 'opensource@codemill.se',
    url = 'http://github.com/codemill/cmsplugin-hoverimage',
    packages = find_packages(),
    include_package_data=True,
    install_requires = [
        'django-cms>=2.1',
    ],
)
