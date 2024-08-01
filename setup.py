from setuptools import setup, find_packages

setup(
    name="journal-cli",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'colorama==0.4.6',
    ],
    entry_points={
        'console_scripts': [
            'journal-cli=journal.cli:main',
        ],
    },
    author="Taylor Hall",
    author_email="taylormichaelhall@gmail,com",
    description="A simple command-line journaling application",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/taylormichaelhall/journal-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)