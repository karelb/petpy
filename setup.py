from setuptools import setup

setup( name ='petpy',
       version='0.1',
       description="Petrophysics utilities",
       url='https://example.com',
       author='Karel Bokhorst',
       author_email='karelbokhorst@shell.com',
       license='Apache 2',
       packages=['petpy'],
       install_requires=['numpy'],
       tests_require=['pytest', 'pytest-cov'],
       entry_points ={
           'console_scripts': [
               'gardner=petpy.__main__:main'
           ]
       },
    )