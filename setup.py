from setuptools import setup

current_dir = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(current_dir, 'README.rst')).read()

setup(
    name='blitz',
    version='1.0',
    long_description= README,
    packages=['blitz'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Fabric'],
)
