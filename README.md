# var2DM

Python package for optimising density matrices.

## Getting Started

Install this package with pip. Jen recommends a conda environment.

https://conda.io/miniconda.html

Once you have miniconda installed:
```
$ conda create -n var2dm python=2 numpy
```

To switch on the environment, use:

```
$ source activate var2dm
```

Then install the horton dependency and the package:

```
$ conda install -c theochem horton
$ pip install -e /path/to/densitymatrices
```

Jen is experimenting with pipenv. Feel free to install it on your machine.

```
$ pip3 install --user pipenv
$ cd densitymatrices
$ pipenv --python 3.6
$ pipenv shell
$ pipenv install package=version
$ pipenv install --dev package=version
$ exit
```

### Prerequisites

Requirements right now are numpy and python 3.6.

### Installing

With your environment switched on (pipenv shell):

```
pipenv install
```

## Running the tests

Not implemented yet...

## Authors

Ali, Xiao, Fanwang, Jen, maybe David, maybe Derrick

## License

No license yet. Don't use this code; it's broken.

## Acknowledgments

* Paul
* Tea

