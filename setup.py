import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fmp API wrapper", 
    version="0.0.1",
    author="razorhash",
    author_email="hashim.mazhar@gmail.com",
    description="A python-based wrapper for the Financial Markets Prep API for financial data of public companies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/razorhash/fmp/",
    packages=setuptools.find_packages(),
    keywords=["Financial Markets Prep", "python", "wrapper", "API"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
        "Target Audience :: Traders, Programmers, Finance and Risk Professionals",
    ],
    python_requires='>=3.6',
)