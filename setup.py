import setuptools

# Read long description from README
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

# Project metadata
REPO_NAME = "end-to-end-ml-multi-model"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "akashbhandari0309@gmail.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for ML applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},                      # Tells setuptools where to find packages
    packages=setuptools.find_packages(where="src"),  # Finds all packages inside 'src'
    classifiers=[                                 # Optional but good for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',                    # Optional, specifies Python version
)
