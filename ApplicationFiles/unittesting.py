# Must install pytest
# This tests if the date selection menu works in the application

import pandas as pd

def date_function(date1,date2):
    if date1 > date2:
        return "ERR"
    elif date1 == date2:
        return "=="
    else:
        return "<"

def keyword_function(keyword):
    crash_data = pd.read_csv('data.csv')
    refined_crash_data = crash_data[crash_data['ACCIDENT_TYPE'].str.contains(keyword)]
    data = refined_crash_data['ACCIDENT_TYPE']
    if data.empty:
        keywordIn = False
    else:
        for a in data:
            keywordIn = True
            if keyword not in a:
                keywordIn=False
                break
    return keywordIn

print(keyword_function("Pedestrian"))

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

# Test 11
def test_keyword_function1():
    assert keyword_function("Pedestrian") == True


# Test 12
def test_keyword_function2():
    assert keyword_function("Collision") == True


# Test 13
def test_keyword_function3():
    assert keyword_function("Struck Pedestrian") == True

# Test 14
def test_keyword_function4():
    assert keyword_function("Collision with vehicle") == True

# Test 15
def test_keyword_function5():
    assert keyword_function("Banana") == False

# Test 16
def test_keyword_function6():
    assert keyword_function("America") == False

# Test 17
def test_keyword_function7():
    assert keyword_function("Boat") == False

# Test 18
def test_keyword_function8():
    assert keyword_function("") == True
