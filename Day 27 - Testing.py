def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

##################################################################
##################################################################
#####BELOW CODE ONLY IS WRITTEN BY ME#############################
##################################################################
##################################################################

import random

class TestDataEmptyArray:
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues:
    size = random.randint(2,30)
    min_indx = random.randint(0,size - 1)
    min_value = random.randint(1,100)
    res = []
    i = 0
    while True:
        if i >= size:
            break
        numb = random.randint(min_value + 1,1000)
        if numb in res:
            continue
        elif i == min_indx:
            res.append(min_value)
            i = i + 1
        else:
            res.append(numb)
            i = i + 1
        if i == size:
            break
    @staticmethod
    def get_array():
        return TestDataUniqueValues.res 

    @staticmethod
    def get_expected_result():
        return TestDataUniqueValues.min_indx

class TestDataExactlyTwoDifferentMinimums:
    size = random.randint(3,30)
    min_indx1 = random.randint(0,size - 1)
    min_value = random.randint(1,100)
    res = []
    i = 0
    while True:
        min2 = random.randint(0, size - 1)
        if min2 == min_indx1:
            continue
        else:
            min_indx2 = min2
            break
    
    while True:
        if i >= size:
            break
        numb = random.randint(min_value + 1,1000)
        if numb in res:
            continue
        elif i == min_indx1 or i == min_indx2:
            res.append(min_value)
            i = i + 1
        else:
            res.append(numb)
            i = i + 1
    @staticmethod
    def get_array():
        return TestDataExactlyTwoDifferentMinimums.res

    @staticmethod
    def get_expected_result():
        if TestDataExactlyTwoDifferentMinimums.min_indx1 < TestDataExactlyTwoDifferentMinimums.min_indx2:
            res = TestDataExactlyTwoDifferentMinimums.min_indx1
        else:
            res = TestDataExactlyTwoDifferentMinimums.min_indx2
        return res


##################################################################
##################################################################
######################UP TO HERE #################################
##################################################################


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

