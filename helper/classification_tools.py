import numpy as np

### constants/global variables
label_mapper = {'Cr' : 0, 'In' : 1, 'Pa' : 2, 'PS' : 3, 'RS' : 4, 'Sc' : 5}
label_list_pair = sorted([[x, y] for x,y in label_mapper.items()], key = lambda x : x[1])
label_list = [x[0] for x in label_list_pair]


def label_matcher(y_cluster, files, map_dict=label_mapper, return_map=False):
    """
    maps cluster centers to true y values based on the most common filename for each cluster. Useful for mapping
    multiple cluster centers onto a single class prediction (eg mapping separate cluster centers representing
    vertical and horizontal scratches to a classification of 'scratches')
    N: number of samples
    ncluster: number of cluster centers
    nclass: number of classes

    :param y_cluster: N*1 vector of clusters
    :param files: list of files corresponding to each element in y_clusters
    :param map_dict: maps filenames to y_true



    :return:y_pred
    """

    clusters = np.unique(y_cluster, return_counts=False)

    map1 = {x: None for x in clusters}
    for x in clusters:
        #temp: list of tags ('Sc' or 'RS' etc) for all images from one cluster center
        temp = [files[i] for i in range(len(files)) if y_cluster[i] == x]
        unique, count = np.unique(temp, return_counts=True)
        #temp
        map1[x] = unique[np.argmax(count)]

    y_pred = np.array([map_dict[map1[x]] for x in y_cluster],dtype=y_cluster.dtype)

    if return_map:
        return y_pred, map1
    else:
        return y_pred