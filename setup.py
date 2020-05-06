import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fmp API wrapper", 
    version="0.0.1",
    author="razorhash",
    author_email="hashim.mazhar@gmail.com",
    license="MIT",
    description="A python-based wrapper for the Financial Models Prep pro API (fmpcloud.io) for financial data of public companies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/razorhash/fmp/",
    download_url = "https://github.com/razorhash/fmp/archive/v0.0.1.tar.gz",
    packages=setuptools.find_packages(),
    keywords=["Financial Models Prep", "python", "wrapper", "API", "fmpcloud.io", "fmpcloud"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent"
        "Target Audience :: Traders, Programmers, Finance and Risk Professionals",
    ],
    python_requires='>=3.6',
)