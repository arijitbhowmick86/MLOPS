from square import square_num

# file name test_<file to be tested>.py
# function name test_<function to be tested>
# pytest - executes all files starting with test_
def test_square_num():
    a = 4
    result = square_num(a)
    assert result == 16,"Result mismatch"
