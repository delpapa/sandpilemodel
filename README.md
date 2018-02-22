# Sand pile model
A basic python implementation of the classic [Bak–Tang–Wiesenfeld model](https://en.wikipedia.org/wiki/Abelian_sandpile_model), including the avalanche distribution plots, written as an example for my phd thesis. The power-law distributions of avalanche durations and sizes result from the [self-organized criticality (SOC)](https://en.wikipedia.org/wiki/Self-organized_criticality) behavior.

## Usage

To run the model, choose the simulation parameters and run the script `src/run_single.py`. Important parameters are the lattice size, the number of grains to be dropped and the type of model. At this moment only the classic sandpile model is implemented, but a few variations are already implemented, such as grains of sand dropping on random sites and/or toppling to random neighbors.  

The main model methods can be found at `src/sandpile.py`.

Plot parameters can be modified in the `src/plot_avalanches.py` script as necessary.

To save simulation time, the avalanche durations and sizes are stored in the folder `results`.

The avalanche plots and power-law fits are done using the [powerlaw](https://pypi.python.org/pypi/powerlaw) package.

### Example

A single simulation of the classic sandpile model on a lattice of size (100, 100) and 100000 grains of sand yields the following avalanche distributions:


The lattice also looks reasonably pretty, even for such small parameters.
\begin{center} <br>
\includegraphics[width=8in]{src/sandpile.pdf} <br>
\end{center}
