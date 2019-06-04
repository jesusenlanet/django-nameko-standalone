import setuptools

with open('README.txt') as file:
    long_description = file.read()

setuptools.setup(
    name="django-nameko-standalone",
    version="1.2.2",
    author="Jesus Gutierrez Almazan",
    author_email="jesus.pedro.gutierrez.almazan@gmail.com",
    description="Use django into a nameko service",
    long_description=long_description,
    url="https://github.com/jesusenlanet/django-nameko-standalone",
    packages=['django_nameko_standalone'],
    platforms=['Linux'],
    install_requires=[
        "Django>=1.11,<=2.2.2",
        "nameko==2.12.0"
    ],
    test_suite='pytest',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Framework :: Django :: 2.1",
        "Topic :: Software Development :: Libraries",
    ],
)
