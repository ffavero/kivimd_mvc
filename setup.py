from setuptools import setup

from minuta_ui import __version__

VERSION = __version__.VERSION
DATE = __version__.DATE
AUTHOR = __version__.AUTHOR
MAIL = __version__.MAIL
WEBSITE = __version__.WEBSITE


install_requires = []
with open("requirements.txt", "rt") as requirements:
    for line in requirements:
        install_requires.append(line.strip())

try:
    __import__("argparse")
except ImportError:
    install_requires.append("argparse")


def list_lines(comment):
    for line in comment.strip().split("\n"):
        yield line.strip()


classifier_text = """
    Development Status :: 5 - Production/Stable
    Intended Audience :: Developers
    Intended Audience :: Science/Research
    Intended Audience :: Information Technology
    Operating System :: OS Independent
    License :: OSI Approved :: GNU General Public License v3 (GPLv3)
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Topic :: Software Development :: Libraries :: Application Frameworks
    Topic :: Utilities
"""

setup(
    name="minuta_ui",
    python_requires=">3.4.0",
    version=VERSION,
    description=("A strategy optimization framework"),
    long_description=open("README.rst").read(),
    author=AUTHOR,
    author_email=MAIL,
    url=WEBSITE,
    license="GPLv3",
    include_package_data=True,
    packages=[
        "minuta_ui",
        "minuta_ui.model",
        "minuta_ui.view",
        "minuta_ui.control",
    ],
    test_suite="test",
    entry_points={"console_scripts": ["minuta = minuta_ui.start:main"]},
    install_requires=install_requires,
    classifiers=list(list_lines(classifier_text)),
    keywords="finance",
)
