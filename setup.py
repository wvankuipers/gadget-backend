import io

from setuptools import find_packages
from setuptools import setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="gadget",
    version="1.0.0",
    url="https://github.com/wvankuipers/gadget-backend",
    license="MIT",
    maintainer="W. van Kuipers",
    maintainer_email="gadget@pwnd.nl",
    description="The REST backend for the Gadget project.",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=["flask"],
    extras_require={"test": ["pytest", "coveralls"]},
    python_requires='>=3.6',
)
