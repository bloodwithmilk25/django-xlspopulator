import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_xlspopulator",
    version="1.1",
    author="Nikita Tonkoshkur",
    author_email="humapen@gmail.com",
    description="Populate your Django model from .xls file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bloodwithmilk25/django-xlspopulator",
    packages=setuptools.find_packages(),
    install_requires=['xlrd'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
