from chinese_zodiac import calculate


# Simple test case at the start of the current cycle
def test_cycle_start():
    assert calculate(1984) == ('Wood', 'Rat', 'yang', 1)


# Randomly chosen year later in the cycle with different values
def test_different_date():
    assert calculate(1993) == ('Water', 'Rooster', 'yin', 10)


# Test another year in same cycle with same animal
# Element should cycle forward but yin/yang association should be same
def test_second_rat_year():
    assert calculate(1996) == ('Fire', 'Rat', 'yang', 13)


# Test a negative value to make sure it can handle BCE years
# Technically not a valid cycle since the fist cycle starts at 4
# Should be calculated as if there were though
def test_negative_value():
    assert calculate(-1) == ('Earth', 'Goat', 'yin', 56)


# Test maxint to make sure it works on ridiculous numbers
# Value is written rather than sys.maxsize incase run on 32-bit system
def test_max_int():
    assert calculate(9223372036854775807) == ('Fire', 'Rabbit', 'yin', 4)
