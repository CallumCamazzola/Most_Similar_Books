import math
from recsys import similarity

def test_similarity_no_ratings():
    """
    This test sends a vector with all zeros into recsys.similarity and
    verifies that the result is 0.0.  The test checks many different 
    lengths of vectors (typical vector lengths of 1 to 3).  The test is 
    careful to check both vectors being all zeros, and one vector 
    being all zeros with the other vector not being all zeros.  
    """
    vector1 = [0,0,0]
    vector2 = [0,0,0]
    result = similarity(vector1,vector2)
    expected = 0.0
    assert (result == expected)

    vector1 = [0,0]
    vector2 = [0,0]
    result = similarity(vector1,vector2)
    expected = 0.0
    assert (result == expected)
    
    vector1 = [0]
    vector2 = [0]
    result = similarity(vector1,vector2)
    expected = 0.0
    assert (result == expected)

    vector1 = [0,0,0]
    vector2 = [1,4,2]
    result = similarity(vector1,vector2)
    expected = 0.0
    assert (result == expected)



def test_similarity_identical_books():
    """
    This test sends two identical vectors to the recsys.similarity function
    and asserts that the similarity is reported to be 1.0 within a tolerance of
    0.0001.  The test checks many different vectors and lengths of vectors 
    (typical vector lengths of 1 to 3).  Note that an all zero vector has 
    a similarity of zero with itself and not similarity of 1.
    """
    vector1 = [1,4,2]
    vector2 = [1,4,2]
    result = similarity(vector1,vector2)
    expected = 1.0
    assert math.isclose(result, expected, abs_tol=0.0001)

    vector1 = [1,4]
    vector2 = [1,4]
    result = similarity(vector1,vector2)
    expected = 1.0
    assert math.isclose(result, expected, abs_tol=0.0001)

    vector1 = [1]
    vector2 = [1]
    result = similarity(vector1,vector2)
    expected = 1.0
    assert math.isclose(result, expected, abs_tol=0.0001)

    

def test_similarity_diff_books():
    """
    This test sends two different vectors to the recsys.similarity function
    and asserts that the similarity is reported to be within a tolerance of
    0.0001 of the hand computed cosine similarity.  The test checks many 
    different vector pairs and lengths of vectors (typical vector lengths of
    1 to 3). 
    """
    
    vector1 = [2,3,4]
    vector2 = [1,4,2]
    result = similarity(vector1,vector2)
    expected = 0.891485
    assert math.isclose(result, expected, abs_tol=0.0001)

    vector1 = [2,3]
    vector2 = [4,1]
    result = similarity(vector1,vector2)
    expected =  0.73994
    assert math.isclose(result, expected, abs_tol=0.0001)

    vector1 = [2]
    vector2 = [7]
    result = similarity(vector1,vector2)
    expected =  1.0
    assert math.isclose(result, expected, abs_tol=0.0001)

    
