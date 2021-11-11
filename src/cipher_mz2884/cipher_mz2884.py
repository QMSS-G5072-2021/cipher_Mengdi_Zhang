def cipher(text, shift, encrypt=True):

    """
    This function takes string and shifts each letter by the number of positions specified in the alphabet to either left(-) or right(+). 
    Parameters
    ----------
    text: str
        Input string that you want to shift
    shift: int
        Number of positions in the alphabet to shift in the right direction
    encrypt: boolean
        True/False indicator defining whether or not the string is to be encrypted by this function
    Returns
    ----------
    new_text: str
        The changed text
        
    Example
    ----------
    >>>cipher("test", 4)
    xiwx
    """""

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text


