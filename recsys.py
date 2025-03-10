import math

"""
This module contains functions for building 
recommendation systems.
"""

def similarity(vector1, vector2):
    """
    Returns the cosine similarity between two vectors.  The vectors 
    must have the same length.  If either vector is all zeros, then the 
    similarity is defined to be zero.  Vectors are assumed to be lists that
    contain numbers (ints and floats).
    """
    
    if len(vector1) != len(vector2):
        raise ValueError("vectors must be same length")
    
    x=0
    y=0
    z=0
    i=0
    while i<(len(vector1)):
       #calculating each individual part of the cosine similarity equation separately
        x = (vector1[i]*vector2[i]) + x
        y = ((vector1[i])**2) + y
        z = ((vector2[i])**2) + z
        i=i+1
    #checking if one of the vectors is full of zeros 
    if x == 0:
        return(0)
    else:
        sim_score = x/(math.sqrt(y)*math.sqrt(z))
        return(sim_score)


    





