from setuptools import setup, find_packages

setup(
    name="xpectranet-sdk",
    version="0.1.0",
    description="SDK for building symbolic agents with memory, remix logic, and Circle governance using the XpectraNet protocol.",
    author="Xpectra Data Technologies Ltd.",
    author_email="dev@xpectradata.com",
    url="https://github.com/XpectraData/xpectranet-sdk",
    packages=find_packages(exclude=["tests*", "examples*"]),
    install_requires=[
        "requests>=2.28",
        "pydantic>=1.10",
        "gql>=3.4",
        "emoji>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Business Source License 1.1",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
