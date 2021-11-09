from setuptools import setup, find_packages

PACKAGES = find_packages()


def setup_package() -> None:
    setup(
        name="ThymeDrift",
        version="",
        description="",
        long_description="",
        author="PerfectThyme",
        author_email="marvin.buss@gmail.com",
        maintainer="PerfectThyme",
        maintainer_email="marvin.buss@gmail.com",
        url="https://github.com/PerfectThyme/ThymeDrift",
        download_url="https://github.com/PerfectThyme/ThymeDrift",
        packages=PACKAGES,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
        ],
        license="",
        requires=""
    )


if __name__ == "main":
    setup_package()
