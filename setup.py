import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfmpcloud", 
    version="0.1.3",
    author="razorhash",
    author_email="hashim.mazhar@gmail.com",
    license="MIT",
    description="A python-based wrapper for the Financial Models Prep pro API (fmpcloud.io) for financial data of public companies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/razorhash/fmp/",
    download_url = "https://github.com/razorhash/fmp/archive/v0.1.3.tar.gz",
    packages=setuptools.find_packages(),
    data_files=[('config',['pyfmpcloud/config.ini'])],
    keywords=["Financial Models Prep", "python", "wrapper", "API", "fmpcloud.io", "fmpcloud"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    python_requires='>=3.6',
)