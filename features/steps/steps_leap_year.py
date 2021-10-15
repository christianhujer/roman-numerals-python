from behave import *

from leap_year import is_leap_year

@step(u'the year {year:d} is not a leap year')
def step_impl(context, year):
    assert not is_leap_year(year)

@step(u'the year {year:d} is a leap year')
def step_impl(contet, year):
    assert is_leap_year(year)
