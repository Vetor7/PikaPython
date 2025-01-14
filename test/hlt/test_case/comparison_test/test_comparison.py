def test_number_equality(num1):
    assert num1 == 10, "Expected %d to be equal to 10" % num1

def test_number_greater_than(num1, num2):
    assert num2 > num1, "Expected %d to be greater than %d" % (num2, num1)

def test_number_less_than(num1, num2):
    assert num1 < num2, "Expected %d to be less than %d" % (num1, num2)

def test_number_greater_than_or_equal(num1, num2):
    assert num1 >= 10, "Expected %d to be greater than or equal to 10" % num1
    assert num2 >= num1, "Expected %d to be greater than or equal to %d" % (num2, num1)

def test_number_less_than_or_equal(num1, num2):
    assert num1 <= 10, "Expected %d to be less than or equal to 10" % num1
    assert num1 <= num2, "Expected %d to be less than or equal to %d" % (num1, num2)

def test_list_membership(list1):
    assert 3 in list1, "Expected 3 to be in the list"
    assert 6 not in list1, "Expected 6 to not be in the list"

def test_dict_membership(dict1):
    assert 'a' in dict1, "Expected 'a' to be in the dictionary keys"
    assert 'z' not in dict1, "Expected 'z' to not be in the dictionary keys"

def test_identity(num1, num3, list1, dict1):
    assert num1 is num1, "Expected num1 to be identical to itself"
    assert num1 is not num3, "Expected num1 to not be identical to num3"
    assert list1 is list1, "Expected list1 to be identical to itself"
    assert list1 is not [1, 2, 3, 4, 5], "Expected list1 to not be identical to a new list"
    assert dict1 is dict1, "Expected dict1 to be identical to itself"
    assert dict1 is not {'a': 1, 'b': 2, 'c': 3}, "Expected dict1 to not be identical to a new dictionary"

def run_tests():
    num1 = 10
    num2 = 20
    num3 = 15
    list1 = [1, 2, 3, 4, 5]
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    test_number_equality(num1)
    test_number_greater_than(num1, num2)
    test_number_less_than(num1, num2)
    test_number_greater_than_or_equal(num1, num2)
    test_number_less_than_or_equal(num1, num2)
    test_list_membership(list1)
    test_dict_membership(dict1)
    test_identity(num1, num3, list1, dict1)
    print("Comparison operations tests passed!")

run_tests()