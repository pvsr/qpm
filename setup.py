from setuptools import setup, find_packages

setup(
    name="qbpm",
    version="0.3",
    url="https://git.sr.ht/~pvsr/qpm",
    packages=find_packages(),
    entry_points={"console_scripts": ["qbpm = qpm.main:main"]},
    install_requires=["pyxdg"],
    author="Peter Rice",
    author_email="peter@peterrice.xyz",
    description="qutebrowser profile manager",
)
