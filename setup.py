#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="project",
    version="0.0.1",
    description="Describe Your Cool Project",
    author="Logan D. Graham",
    author_email="Logan.Graham@StonyBrook.edu",
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url="https://github.com/LoganDGraham",
    packages=find_packages(),
    install_requires=[
        "pytorch-lightning",
        "torch@https://download.pytorch.org/whl/cu113/torch-1.10.1%2Bcu113-cp39-cp39-linux_x86_64.whl",
        "torchvision@https://download.pytorch.org/whl/cu113/torchvision-0.11.2%2Bcu113-cp39-cp39-linux_x86_64.whl",
        "torchaudio@https://download.pytorch.org/whl/cu113/torchaudio-0.10.1%2Bcu113-cp39-cp39-linux_x86_64.whl",
    ],
    setup_requires=["black"],
)
