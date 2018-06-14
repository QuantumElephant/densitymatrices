# var2DM

Python package for optimising density matrices.

## Getting Started

Download the github repository:

```
$ git clone https://github.com/QuantumElephant/densitymatrices.git
```

Using a conda environment is recommended for managing project dependencies. Download miniconda here:

https://conda.io/miniconda.html

Once you have miniconda installed, create a new virtual environment for the project:

```
$ conda create -n var2dm python=3
```

To switch on the environment, use:

```
$ source activate var2dm
```

To deactivate the environment, use:

```
(var2dm) $ source deactivate
```

### Prerequisites

Requirements right now are python 3.6, numpy, iodata, and gbasis. The last two requirements are part of the Horton package from theochem.

There are also some requirements for the semi-definite programming portion of this package: six, cvxopt, and picos.

### Installing Prerequisites

Activate the conda environment and enter the following commands:

```
(var2dm) $ conda install six
(var2dm) $ conda install -c conda-forge cvxopt
(var2dm) $ conda install -c theochem gbasis
(var2dm) $ conda install -c theochem iodata
```

Note: cvxopt requires numpy to be installed, and so conda should install that package automatically.

For installing picos, download the source tarball from here: 

http://picos.zib.de/download.html

Then, go to where the package was saved, and extract the files. You may need to change the version number depending on what file you downloaded.

```
(var2dm) $ tar -xzvf PICOS-1.1.2.tar.gz
(var2dm) $ cd PICOS-1.1.2
(var2dm) $ pip install -e ./
```

### Installing var2DM

With the virtual environment activated, install the package locally:

```
(var2dm) $ pip install -e /path/to/densitymatrices
```

Now the package can be imported in python:

```
(var2dm) $ python
Python 3.6.5 |Anaconda, Inc.| (date-time stripped)
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import var2DM
>>>
```

## Running the tests

Install nosetests and specify the package name:
```
(var2dm) $ conda install nose
(var2dm) $ nosetests -v var2DM
```

## Pipenv Notes

Jen is experimenting with pipenv. Feel free to install it on your machine. This installation method won't work until the project dependencies are available via pip install.

```
$ pip3 install --user pipenv
$ cd densitymatrices
$ pipenv --python 3.6
$ pipenv shell
(var2dm_env) $ pipenv install package=version
(var2dm_env) $ pipenv install --dev package=version
$ exit
```

With your environment switched on (pipenv shell):

```
(var2dm_env) $ pipenv install
```

## Authors

Ali, Xiao, Fanwang, Jen, maybe David, maybe Derrick

## License

No license yet. Don't use this code; it's broken.

## Acknowledgments

* Paul
* Tea

