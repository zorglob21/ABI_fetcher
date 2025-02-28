from setuptools import setup, find_packages

setup(
    name="abi-fetcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "abi-fetch=abi_fetcher.client:main",  # Optional CLI
        ],
    },
    author="Yann Neve",
    author_email="neve.yann@gmail.com",
    description="A Python package to fetch smart contract ABIs from all EVM compatible blockchains",
    long_description=open("README.MD").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zorglob21/ABI_fetcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

