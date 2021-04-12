def quicksort(array):
    """
    

    Parameters
    ----------
    array : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if(len(array) <= 1):
        return array
    else:
        sortElem = array[0]
        maxElem = []
        minElem = []
        centerElem = []
        for i in range(len(array)):
            if (array[i] > sortElem):
                maxElem.append(array[i])
            else:
                if (array[i] < sortElem):
                    minElem.append(array[i])
                else:
                    centerElem.append(array[i])
    return quicksort(minElem) + centerElem + quicksort(maxElem)
                    
def search_elem(elem, array):
    """
    

    Parameters
    ----------
    elem : TYPE
        DESCRIPTION.
    array : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    for i in range(len(array)):
        if (array[i] == elem):
            return i
    return False

def arrayInArray(firstArray,secondArray): 
    """
    

    Parameters
    ----------
    firstArray : TYPE
        DESCRIPTION.
    secondArray : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    for i in range(len(secondArray)):
        array = []
        if len(firstArray) <= len(secondArray) - i:
            for j in range(len(firstArray)):
                if firstArray[j] == secondArray[i+j]:
                    array.append(firstArray[j])
                else:
                    break               
            if array == firstArray:
                return i    
    return False

def search_maxElements(amount, array):
    """
    

    Parameters
    ----------
    amount : TYPE
        DESCRIPTION.
    array : TYPE
        DESCRIPTION.

    Returns
    -------
    maxElem : TYPE
        DESCRIPTION.

    """
    array = quicksort(array)
    maxElem = []
    for i in range(amount):
        maxElem.append(array[len(array)-i-1])
    return maxElem

def search_minElements(amount, array):
    """
    What does it do...
    

    Parameters
    ----------
    amount : int
    array : list

    Returns
    -------
    minElem : list

    """
    array = quicksort(array)
    minElem = []
    for i in range(amount):
        minElem.append(array[i])
    return minElem
    


def sered(array):
    """
    

    Parameters
    ----------
    array : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if(len(array) > 0):
        sered = sum(array)/len(array)
        return sered
    else:
        return 0

def returns(array):
    """
    Removes duplicate numbers in the list. 

    Parameters
    ----------
    array : list.

    Returns
    -------
    array : list.

    """
    array.reverse() # перевернули масив
    for i in array:
        number = i
        while( array.count(number) > 1):
            array.remove(number)
    array.reverse()
    return array
       
    
cout=[34,3,5,23,23,2,3,4,67,3,12,5]
print( " max elem = "+str(returns(cout)))