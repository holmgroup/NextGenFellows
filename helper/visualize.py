import matplotlib.pyplot as plt
import numpy as np
import skimage.io

from . import classification_tools as ct


def pano_image(x, y, paths, patch_size=(3, 3), ax0=None):
    """
    overlays images on t-sne plot
    :param x: array of x coords
    :param y: array y coords
    :param paths: list of image paths
    :param patch_size: image pach size
    :param ax0: axis object
    :return: axis object if one is passed to ax0
    """
    if ax0 is None:
        fig, ax = plt.subplots(figsize=(7, 7), dpi=150)
    else:
        ax = ax0
    px, py = patch_size
    ax.scatter(x, y, color=(0, 0, 0, 0))
    for xi, yi, pi in zip(x, y, paths):
        im = skimage.io.imread(pi)
        ax.imshow(im, extent=(xi - px, xi + px, yi - py, yi + py), cmap='gray')

    if ax0 is None:
        plt.show()
    else:
        return ax

def pretty_cm(cm=None, labelnames=ct.label_list, cscale=0.6, ax0=None, fs=12):
    """
    generates a pretty-formated confusion matrix
    :param cm: confusion matrix, nxn numpy array
    :param labelnames: list of labels corresponding to each row/column in cm, for labeling purposes
    :param cscale : parameter adjusts the color intensity (useful for good models with few mistakes)
    :param ax0: matplotlib axis object on which to compute confusion matrix. If none is provided, plot will be shown, but can not be manipulated further (ie is not returned)
    :param fs: font size for axis labels and annotations on confusion matrix
    """
    acc = cm.trace() / cm.sum()
    if ax0 is None:
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7), dpi=300)
        fig.set_facecolor('w')
    else:
        ax = ax0

    n = len(labelnames)
    ax.imshow(np.power(cm, cscale), cmap='magma', extent=(0, n, 0, n))
    labelticks = np.arange(n) + 0.5
    ax.set_xticks(labelticks, minor=True)
    ax.set_yticks(labelticks, minor=True)
    ax.set_xticklabels(['' for i in range(n)], minor=False, fontsize=fs)
    ax.set_yticklabels(['' for i in range(n)], minor=False, fontsize=fs)

    ax.set_xticklabels(labels=labelnames, minor=True, fontsize=fs)
    ax.set_yticklabels(labels=reversed(labelnames), minor=True, fontsize=fs)

    ax.set_xlabel('Predicted Labels', fontsize=fs)
    ax.set_ylabel('Actual Labels', fontsize=fs)
    for (i, j), z in np.ndenumerate(cm):
        ax.text(j + 0.5, n - i - 0.5, '{:^5}'.format(z), ha='center', va='center', fontsize=fs,
                bbox=dict(boxstyle='round', facecolor='white', edgecolor='0.3'))
    ax.grid(which='major', color=np.ones(3) * 0.33, linewidth=1.5)

    if ax0 is None:
        ax.set_title('Accuracy: {:.3f}'.format(cm.trace() / cm.sum()))
        plt.show()
        return
    else:
        return ax
