# Test1
def date_function(date1,date2):
    if date1 > date2:
        return ">"
    elif date1 == date2:
        return "=="
    else:
        return "<"

def test_date_function1():
    assert date_function(10,3) == '>'

# Test 2
def test_date_function2():
    assert date_function(3,3) == '=='

# Test 3
def test_date_function3():
    assert date_function(3,10) == '<'

# Test 4

# Test 5

# Test 6

# Test 7

# Test 8

# Test 9

# Test 10