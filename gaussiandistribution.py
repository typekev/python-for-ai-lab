import math
from generaldistribution import Distribution

class Gaussian(Distribution):
    """
    Gaussian distribution class for calculating and visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
    """
    def __init__(self):
        pass


    def calculate_mean(self):
        """
        Function to calculate the mean of the data set.
        
        Args: 
            None
        
        Returns: 
            float: Mean of the data set.
    
        """
        pass


    def calculate_stdev(self, sample=True):

        """
        Function to calculate the standard deviation of the data set.
        
        Args: 
            sample: bool. Whether the data represents a sample or population.
        
        Returns: 
            float: Standard deviation of the data set.
    
        """
        pass        


    def pdf(self, x):
        """
        Probability density function calculator for the gaussian distribution.
        
        Args:
            x: float. Point for calculating the probability density function.
            
        
        Returns:
            float: probability density function output.
        """
        pass


    def __add__(self, other):
        """
		Function to add together two Gaussian distributions.
        
        Args:
            other: Gaussian. Gaussian instance.
            
        Returns:
            Gaussian: Gaussian distribution.
        """
        pass