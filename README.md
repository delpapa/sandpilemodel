# Sand pile model
A basic python implementation of the classic [Bak–Tang–Wiesenfeld model](https://en.wikipedia.org/wiki/Abelian_sandpile_model) with avalanche distribution plots, written as a test for my thesis. The power law distributions of avalanche durations and sizes result from the self-organized critical (SOC) behavior.

## Usage

To run the model, choose the simulation parameters and run the script `run_single.py`. Important parameters are the lattice size, the number of grains to be dropped and the model variations. A few variations from the original model are already implemented, such as grains of sand dropping on random sites and/ or toppling to random neighbors.  

The main model methods can be found at `sandpile.py`.

Plot parameters can be modified in the `plots.py` script as necessary.

To save simulation time, the avalanche durations and sizes are stored in the folder `results`.

The avalanche plots and power law fits are done using the [powerlaw](https://pypi.python.org/pypi/powerlaw) package.
