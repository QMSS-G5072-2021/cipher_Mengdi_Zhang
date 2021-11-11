from cipher_mz2884 import cipher_mz2884

def test_cipher_encrypt(): 
    example = ['test', 4]
    expected = 'xiwx'
    actual = cipher_mz2884.cipher(example[0],example[1])
    assert actual == expected
