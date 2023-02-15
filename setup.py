from setuptools import find_packages
from setuptools import setup

setup(
    name="EdgeGPT",
    version="0.0.40",
    license="GNU General Public License v2.0",
    author="Antonio Cheong",
    author_email="acheong@student.dalat.org",
    description="Reverse engineered Edge Chat API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/acheong08/EdgeGPT",
    install_requires=["asyncio", "tls-client", "websockets"],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["EdgeGPT"],
)
