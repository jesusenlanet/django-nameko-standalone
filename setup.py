import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_nameko_standalone",
    version="0.0.1",
    author="Jesus Gutierrez Almazan",
    author_email="jesus.pedro.gutierrez.almazan@gmail.com",
    description="Use django standalone into nameko services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/projectsforfun/django-nameko-standalone",
    packages=['django_nameko_standalone'],
    install_requires=[
        "Django==2.1.4",
        "nameko==2.11.0"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 2.1",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Distributed Computing"
    ],
)
