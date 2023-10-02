# Must install pytest
# This tests if the date selection menu works in the application

def date_function(date1,date2):
    if date1 > date2:
        return "ERR"
    elif date1 == date2:
        return "=="
    else:
        return "<"

# Test1
def test_date_function1():
    assert date_function(2013,2016) == '<'

# Test 2
def test_date_function2():
    assert date_function(2015,2014) == 'ERR'

# Test 3
def test_date_function3():
    assert date_function(2014,2014) == '=='

# Test 4
def test_date_function4():
    assert date_function(2014,2018) == '<'


# Test 5
def test_date_function5():
    assert date_function(2014,2015) == '<'

# Test 6
def test_date_function6():
    assert date_function(2019,2015) == 'ERR'

# Test 7
def test_date_function7():
    assert date_function(2014,2013) == 'ERR'

# Test 8
def test_date_function8():
    assert date_function(2019,2019) == '=='

# Test 9
def test_date_function9():
    assert date_function(2018,2018) == '=='

# Test 10
def test_date_function10():
    assert date_function(2015,2016) == '<'