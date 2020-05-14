import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()


def read_version():
    filename = os.path.join(os.path.dirname(__file__), "kulturweb", "__init__.py")
    with open(filename, mode="r", encoding="utf-8") as fin:
        for line in fin:
            if line and line.strip() and line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"')

    return "0.0.0.0"


requires = [
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_chameleon",
    "pyramid_debugtoolbar",
    "waitress",
    "SQLAlchemy",
    "arrow",
    "sqlalchemy_utils",
]

tests_require = [
    "WebTest >= 1.3.1",  # py3 compat
    "pytest >= 3.7.4",
]

setup(
    name="kulturweb",
    version=read_version(),
    description="a website with a selection of Bremen's cultural offerings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="Niek Stortenbeker",
    author_email="niek@kulturbremen.de",
    url="https://github.com/niekstortenbeker/kulturweb",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require},
    install_requires=requires,
    entry_points={"paste.app_factory": ["main = kulturweb:main"]},
)
