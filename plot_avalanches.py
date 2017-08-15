import os
import cPickle as pickle

import numpy as np
import matplotlib.pylab as plt
import powerlaw as pl

def plot_avalanches(aval_times, aval_sizes):

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

    plt.figure(1)
    x_range = np.arange(1, aval_times.max())
    plt.plot(x_range, x_range**(-time.alpha), 'r',
             label=r'$\alpha = %.2f$' % time.alpha)
    t_unique, t_counts = np.unique(aval_times, return_counts=True)
    plt.plot(t_unique, t_counts / float(t_counts.sum()), '.',
             label=r'data')
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(r'$t$')
    plt.ylabel(r'$f(t)$')
    plt.title(r'Avalanche times')
    plt.legend(loc='best')

    plt.figure(2)
    x_range = np.arange(1, aval_sizes.max())
    plt.plot(x_range, x_range**(-size.alpha), 'r',
             label=r'$\alpha = %.2f$' % size.alpha)
    s_unique, s_counts = np.unique(aval_sizes, return_counts=True)
    plt.plot(s_unique, s_counts / float(s_counts.sum()), '.',
             label=r'data')
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(r'$s$')
    plt.ylabel(r'$f(s)$')
    plt.title(r'Avalanche sizes')
    plt.legend(loc='best')

    plt.figure(3)
    x_range = np.arange(1, unique_t.max())
    plt.plot(unique_t, mean_s, '.',
             label = r'sim. data')
    plt.xscale('log')
    plt.yscale('log')

    plt.xlabel(r'$t$')
    plt.ylabel(r'$\langle s \rangle$')
    plt.title(r'Average avalanche size')
    plt.legend(loc='best')

if __name__ == "__main__":

    for n_sim in xrange(1, 1000):
        results_dir = 'results/ASM' + '_' + str(n_sim) + '/'
        if os.path.exists(results_dir):
            break

    aval_times = pickle.load(open(results_dir+'avalanche_times.p', 'rb'))
    aval_sizes = pickle.load(open(results_dir+'avalanche_sizes.p', 'rb'))

    plot_avalanches(aval_times, aval_sizes)
    plt.show()
