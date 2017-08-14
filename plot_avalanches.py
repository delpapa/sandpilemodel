import numpy as np
import matplotlib.pylab as plt
import powerlaw as pl

def plot_avalanches(asm):

    aval_time = np.array(asm.aval_time)
    aval_size = np.array(asm.aval_size)

    # fit power-laws
    size = pl.Fit(aval_size, xmin=1)
    time = pl.Fit(aval_time, xmin=1)

    mean_t = np.unique(aval_time)
    mean_s = np.zeros_like(mean_t)
    for t, dur in enumerate(mean_t):
        mean_s[t] = aval_size[np.where(aval_time == dur)[0]].mean()

    plt.figure(1)
    x_range = np.arange(1, aval_time.max())
    plt.plot(x_range, x_range**(-time.alpha), 'k')
    pl.plot_pdf(aval_time)

    plt.figure(2)
    x_range = np.arange(1, aval_size.max())
    plt.plot(x_range, x_range**(-size.alpha), 'k')
    pl.plot_pdf(aval_size)

    plt.figure(3)
    plt.plot(mean_t, mean_s, '.')

    import ipdb; ipdb.set_trace()
