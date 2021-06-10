import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import skimage.io
import skimage.color

def pad_img(img, color, padwidth=5):
    if len(img.shape) == 2:
        img = skimage.color.gray2rgb(img)
        
    r,c = img.shape[:2]
    #print(r,c, img.shape, color, img.dtype, np.array(color).dtype)
    new_img = np.reshape(color, (1,1,3)) * np.ones((r+2*padwidth, c+2*padwidth, 3), img.dtype)
    new_img[padwidth:-padwidth,padwidth:-padwidth,:] = img
    return new_img


def pano_plot(x, y, paths, patch_size=(3, 3), ax0=None, labels=None):
    """
    Graphs y vs x with images on plot instead of points.

    Generates 'panoramic' image plots which are useful for visualizing how images 
    separate in feature space for clustering and classification challenges.
    
    Parameters
    ---------------
    x, y: ndarray
        n-element arrays of x and y coordinates for plot
        
    paths: list of strings or path objects
        n-element list of paths to images to be displaied at each point
        
    patch_size: tuple(int, int)
        size of the image patches displayed at each point
        
    ax0: None or matplotlib axis object
        if None, a new figure and axis will be created and the visualization will be displayed.
        if an axis is supplied, the panoramic visualization will be plotted on the axis in place.

    labels: None or list-like
        (optional) if not none, images will be padded in color corresponding to their labels
        
    Returns
    ----------
    None
    
    """
    if ax0 is None:
        fig, ax = plt.subplots(figsize=(7, 7), dpi=150)
    else:
        ax = ax0
    px, py = patch_size
    ax.scatter(x, y, color=(0, 0, 0, 0))
    if labels is None:
        for xi, yi, pi in zip(x, y, paths):
            im = skimage.io.imread(pi)
            ax.imshow(im, extent=(xi - px, xi + px, yi - py, yi + py), cmap='gray')
    else:
        unique = np.unique(labels)
        colors = np.array(sns.color_palette('bright')[:len(unique)])
        colors = skimage.exposure.rescale_intensity(colors, (0,1), (0,255)).astype(np.uint8)
        mapper = {u:c for u, c in zip(unique, colors)}
        
        for xi, yi, pi, li  in zip(x, y, paths, labels):
                im = skimage.io.imread(pi)
                im = pad_img(im, mapper[li])
                ax.imshow(im, extent=(xi - px, xi + px, yi - py, yi + py), cmap='gray')

    if ax0 is None:
        plt.show()


def pretty_cm(cm, labelnames, cscale=0.6, ax0=None, fs=12, cmap='magma'):
    """
    Generates a pretty-formated confusion matrix for convenient visualization.
    
    The true labels are displayed on the rows, and the predicted labels are displayed on the columns.
    
    Parameters
    ----------
    cm: ndarray 
        nxn array containing the data of the confusion matrix.
    
    labelnames: list(string)
        list of class names in order on which they appear in the confusion matrix. For example, the first
        element should contain the class corresponding to the first row and column of *cm*.

    cscale: float
        parameter that adjusts the color intensity. Allows color to be present for confusion matrices with few mistakes,
        and controlling the intensity for ones with many misclassifications.
    
    ax0: None or matplotlib axis object
        if None, a new figure and axis will be created and the visualization will be displayed.
        if an axis is supplied, the confusion matrix will be plotted on the axis in place.

    fs: int
        font size for text on confusion matrix.
        
    cmap: str
        matplotlib colormap to use
    
    Returns
    ---------
    None
    
    """
    
    acc = cm.trace() / cm.sum()
    if ax0 is None:
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 7), dpi=300)
        fig.set_facecolor('w')
    else:
        ax = ax0

    n = len(labelnames)
    ax.imshow(np.power(cm, cscale), cmap=cmap, extent=(0, n, 0, n))
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

