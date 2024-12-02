from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="yappa",
    version="0.4.30",
    url="https://github.com/turokg/yappa",
    description="Easy serverless deploy of python web applications",
    long_description_content_type="text/markdown",
    long_description=README,
    author="Egor Korovin",
    author_email="kbkor@yandex.ru",
    packages=find_packages(),
    install_requires=[
        "boto3>=1.10",
        "click>=8.0",
        "httpx==0.18",
        "yandexcloud>=0.102.1",
        "boltons>=21.0",
        "idna<3,>=2.5",
        "PyYAML>=5.0",
        "furl>=2.0",
        "pytz>=2021",
    ],
    python_requires=">=3.8.0",
    entry_points={"console_scripts": ["yappa = yappa.cli:cli"]},
    license="MIT",
    package_data={"yappa": ["*.yaml"]},
    include_package_data=True,
)
