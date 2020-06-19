import numpy as np


class CustomLabelEncoder:
    """
    Creates a mapping between string labels and integer class clabels for working with categorical data.
    
    
    Attributes
    ----------
    mapper:None dict
        None if mapper is not supplied or model is not fit.
        keys are unique string labels, values are integer class labels.
    """
    def __init__(self, mapper=None):
        """
        Initializes class instance.
        
        If the mapper dictionary is supplied here, then the model can be used without calling .fit().
        
        Parameters
        -----------
        mapper (optional): dict or None
            if mapper is None encoder will need to be fit to data before it can be used.
            If it is a dictionary mapping string labels to integer class labels, then this will be stored
            and the model can be used to transform data.
        """
        self.mapper = mapper
    
    def fit(self, str_labels, sorter=None):
        """
        Fits string labels to intiger indices with optional sorting.
        
        np.unique() is used to extract the unique values form labels. If 
        
        Parameters
        ----------
        str_labels: list-like
            list or array containing string labels
        
        sorter (optional): None or function
            key for calling sorted() on data to determine ordering of the numeric indices for each label.
            
        Attributes
        -----------
        mapper: dict
            dictionary mapping string labels to the sorted integer indices is stored after fitting.
        
        """
        sorted_unique = sorted(np.unique(str_labels), key=sorter)
        mapper = {label: i for i, label in enumerate(sorted_unique)}
        self.mapper = mapper    

    def transform(self, str_labels):
        """
        Maps string labels to integer labels.
        
        Parameters
        ----------
        str_labels: list-like
            list of string labels whose elements are in self.mapper
        
        Returns
        --------
        int_labels: array
            array of integer labels  corresponding to the string labels
        """
        assert self.mapper is not None, 'Encoder not fit yet!'
        
        int_labels = np.asarray([self.mapper[x] for x in str_labels], np.int)
        
        return int_labels
        
    def inverse_transform(self, int_labels):
        """
        Maps integer labels to original string labels.
        
        Parameters
        -----------
        int_labels: list-like
            list or array of integer class indices
        
        Returns
        ----------
        str_labels: array(str)
            array of string labels corresponding to intiger indices
        
        """
        assert self.mapper is not None, 'Encoder not fit yet!'
        
        reverse_mapper = {y:x for x,y in self.mapper.items()}
        
        str_labels = np.asarray([reverse_mapper[x] for x in int_labels])
        
        return str_labels


def label_matcher(y_cluster, labels, return_mapper=False):
    """
    maps cluster centers to true labels based on the most common filename for each cluster. 

    Parameters
    ----------
    y_cluster: ndarray
        n-element array of labels obtained from clusters
        
    labels: ndarray
        n-element array of ground truth labels for which y_cluster will be mapped to
        
    return_mapper:bool
        if True, dictionary mapping values in y_cluster to values in labels will be returned


    Returns
    -----------
    y_pred: ndarray
        n-element array of values in y_cluster mapped to labels
    
    mapper (optional): dict
        dictonary whose keys are elements of y_cluster and values are the corresponding
        elements of labels.

    """
        
    y_cluster = np.asarray(y_cluster)
    labels = np.asarray(labels)
    
    y_cluster_unique = np.unique(y_cluster)

    
    mapper = {}  # keys will be cluster ID's, values will be corresponding label
    
    for x in y_cluster_unique:
        unique, counts = np.unique(labels[y_cluster==x], return_counts=True)  # get frequency of each gt label in cluster x
        mapper[x] = unique[counts.argmax()]  # set mapper[x] to the most frequent label in the cluster

    y_pred = np.asarray([mapper[x] for x in y_cluster])  # map cluster id's to labels

    if return_mapper:
        return y_pred, mapper
    else:
        return y_pred

