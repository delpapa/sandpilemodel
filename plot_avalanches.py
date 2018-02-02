import os
import cPickle as pickle

import numpy as np
import matplotlib.pylab as plt
import powerlaw as pl

def plot_avalanches(aval_times, aval_sizes):
    """Plot avalanche events distrubutions
    Includes plots and power-law fits for duration, size, and average size
    """
    # figure main parameters
    FIG_SIZE = (6, 5)
    FONT_SIZE = 12

    # load variables
    aval_times = np.array(aval_times)
    aval_sizes = np.array(aval_sizes)

    # fit power-laws
    # xmax should be estimated based on the plot
    size = pl.Fit(aval_sizes, discrete=True, xmin=1, xmax=1000)
    time = pl.Fit(aval_times, discrete=True, xmin=1, xmax=100)

    unique_t = np.unique(aval_times)
    mean_s = np.zeros_like(unique_t)
    for t, dur in enumerate(unique_t):
        mean_s[t] = aval_sizes[np.where(aval_times == dur)[0]].mean()

    fig_dur = plt.figure(figsize=FIG_SIZE)
    x_range = np.arange(1, aval_times.max())
    plt.plot(x_range, x_range**(-time.alpha), 'r',
             label=r'$\alpha = %.2f$' % time.alpha)
    t_unique, t_counts = np.unique(aval_times, return_counts=True)
    plt.plot(t_unique, t_counts / float(t_counts.sum()), '.', color='gray',
             label=r'data')
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(r'$t$', fontsize=FONT_SIZE)
    plt.ylabel(r'$f(t)$', fontsize=FONT_SIZE)
    plt.title(r'Avalanche times', fontsize=FONT_SIZE)
    plt.legend(loc='best', frameon=False, fontsize=FONT_SIZE)

    fig_size = plt.figure(figsize=FIG_SIZE)
    x_range = np.arange(1, aval_sizes.max())
    plt.plot(x_range, x_range**(-size.alpha), 'r',
             label=r'$\alpha = %.2f$' % size.alpha)
    s_unique, s_counts = np.unique(aval_sizes, return_counts=True)
    plt.plot(s_unique, s_counts / float(s_counts.sum()), '.', color='gray',
             label=r'data')
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(r'$s$', fontsize=FONT_SIZE)
    plt.ylabel(r'$f(s)$', fontsize=FONT_SIZE)
    plt.title(r'Avalanche sizes', fontsize=FONT_SIZE)
    plt.legend(loc='best', frameon=False, fontsize=FONT_SIZE)

    fig_scale = plt.figure(figsize=FIG_SIZE)
    x_range = np.arange(1, unique_t.max())
    plt.plot(unique_t, mean_s, '.', color='gray',
             label = r'sim. data')
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(r'$t$', fontsize=FONT_SIZE)
    plt.ylabel(r'$\langle s \rangle$', fontsize=FONT_SIZE)
    plt.title(r'Average avalanche size', fontsize=FONT_SIZE)
    plt.legend(loc='best', frameon=False, fontsize=FONT_SIZE)

    # save figures
    if not os.path.exists('plots'):
        os.makedirs('plots')
    fig_dur.savefig('plots/avalanche_duration.pdf', dpi=200)
    fig_size.savefig('plots/avalanche_size.pdf', dpi=200)
    fig_scale.savefig('plots/avalanche_scaling.pdf', dpi=200)


def plot_pile(lattice):
    """Plot the final shape of the pile of sand."""

    fig = plt.figure(figsize=(5, 5))
    plt.imshow(lattice, interpolation='none', cmap='Blues')
    plt.xticks([], [])
    plt.yticks([], [])

    if not os.path.exists('plots'):
        os.makedirs('plots')
    fig.savefig('plots/sandpile.pdf', dpi=200)

if __name__ == "__main__":

    for n_sim in xrange(1, 1000):
        results_dir = 'results/ASM' + '_' + str(n_sim) + '/'
        if os.path.exists(results_dir):
            break

    aval_times = pickle.load(open(results_dir+'avalanche_times.p', 'rb'))
    aval_sizes = pickle.load(open(results_dir+'avalanche_sizes.p', 'rb'))

    plot_avalanches(aval_times, aval_sizes)
