import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lucidsonicdreams", 
    version="0.4",
    author="Alain Mikael Alafriz",
    author_email="mikaelalafriz@gmail.com",
    description="Syncs GAN-generated visuals to music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.7',
    url="https://github.com/DeFi-Coder-News-Letter/lucid-sonic-dreams",
    download_url="https://github.com/DeFi-Coder-News-Letter/lucid-sonic-dreams/blob/main/lucid-sonic-dreams-v_04.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['tensorflow==1.15',
                      'librosa',
                      'numpy==1.16.0',
                      'moviepy',
                      'Pillow==6.2.1',
                      'tqdm',
                      'scipy==1.1.0',
                      'scikit-image',
                      'pygit2',
                      'gdown', 
                      'mega.py',
                      'requests==2.22.0',
                      'pandas',
                      'SoundFile']
)
