from setuptools import setup, find_packages

setup(
    name="zos-ml-demo",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask>=3.0.0",
        "scikit-learn>=1.4.0",
        "pandas>=2.2.0",
        "numpy>=1.26.0",
        "python-dateutil>=2.8.2",
        "requests>=2.31.0",
        "pyyaml>=6.0.1",
        "typing-extensions>=4.9.0",
    ],
    python_requires=">=3.9",
)
