# IRTools
IRTools is a computational toolset for detection and analysis of intron retention from RNA-Seq libraries.

## Installation



#### PIP

To install directly from PyPI:

```
pip install IRTools
```

If this fails, please install all dependencies first:

```
pip install HTSeq
pip install pysam
pip install pandas
pip install networkx
pip install bx-python==0.7.3
```


#### From source

To install from source:

1\. Install the dependencies with your favorite tools (`pip`, `conda`, etc.).

2\. Run:

```
python setup.py install
```


## Usage

```
IRTools [-h] [-v] {annotation,quant,diff} ...
```

There are three major functions available in IRTools serving as sub-commands.

| Command | Description |
| --- | --- |
| git status | List all new or modified files |
| git diff | Show file differences that haven't been staged |
