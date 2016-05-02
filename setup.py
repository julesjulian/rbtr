from setuptools import setup, find_packages

setup(
    name='rbtr',
    version='0.0.1',
    description='Solution to a test exercise.',
    maintainer='Julian Kuhlmann',
    maintainer_email='jlnkuhlmann@gmail.com',
    packages=find_packages(exclude=['tests*']),
    platforms='any',
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'rbtr=rbtr.main:run_from_command_line'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering'
    ]
)
