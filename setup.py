from setuptools import setup, find_packages

setup(
    name='Pythonwebsample',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-Migrate',
        'Werkzeug',
    ],
    entry_points={
        'console_scripts': [
            'Pythonwebsample-main = loginpage:app',
        ],
    },
)