# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 12:46:22 2018

@author: Victor Me

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

"""

## Check if year is leapyear
def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

## Calculates the days past given the year, month, and day
def daysPastYear(year, month, day):
    days_past = 0
    base_month = 1
    days_in_month = {
            1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
            7:31, 8:31, 9:30, 10:31, 11:30, 12:31
    }
    while base_month < month:
        if base_month == 2 and isLeapYear(year):
            days_past = days_past + days_in_month[base_month] + 1
            base_month += 1
        else:
            days_past = days_past + days_in_month[base_month]
            base_month += 1
    for days in range(day):
        days_past += 1
    return days_past - 1 # Correct for 1 day

## Calculates the days passed between two dates
def daysOld(byear,bmonth,bday,cyear,cmonth,cday):
    days_count = 0
    birth_year_past = daysPastYear(byear,bmonth,bday)
    current_year_past = daysPastYear(cyear,cmonth,cday)
    if byear == cyear:
        days_count = current_year_past - birth_year_past
    else:
        if isLeapYear(byear):
            days_count = 366 - birth_year_past
        else:
            days_count = 365 - birth_year_past
        days_count = days_count + current_year_past
        byear += 1
        while byear < cyear:
            if isLeapYear(byear):
                days_count = days_count + 366
                byear += 1
            else:
                days_count = days_count + 365
                byear +=1
    return days_count
        
    
    
    
    
    
    
    
    
    