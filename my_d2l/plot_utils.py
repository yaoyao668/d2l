from matplotlib import axes
import matplotlib.pyplot as plt

def set_figsize(figsize=(3.5, 2.5)):
    # 设置图表大小
    plt.rcParams['figure.figsize'] = figsize

def set_axes(axes, xlable, ylable, xlim, ylim, xscale, yscale, legend):
    # 设置图表的属性
    axes.set_xlabel(xlable)
    axes.set_ylabel(ylable)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    axes.set_xscale(xscale)
    axes.set_yscale(yscale)
    if legend:
        axes.legend(legend)
    axes.grid()

def plot(X, Y=None, xlable=None, ylable=None, legend=None, xlim=None, ylim=None, xscale='linear', yscale='linear', fmts=('-','m--','g-.','r:'), figsize=(3.5,2.5), axes=None):
    if legend is None:
        legend=[]
    set_figsize(figsize)
    axes = axes if axes else plt.gca()

    def has_one_axis(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list) and not hasattr(X[0], "__len__"))

    if has_one_axis(X):
        X = [X]

    if Y is None:
        X,Y = [[]]*len(X),X
    elif has_one_axis(Y):
        Y = [Y]

    if len(X) != len(Y):
        X = X * len(Y)
    axes.cla()

    for x,y,fmt in zip(X, Y, fmts):
        if len(x):
            axes.plot(x,y,fmt)
        else:
            axes.plot(y,fmt)

    set_axes(axes,xlable,ylable,xlim,ylim,xscale,yscale,legend)
    plt.show()

