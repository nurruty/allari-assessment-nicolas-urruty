from datetime import datetime

def normalize_phone(phone_number):
    if phone_number == None:
        return ""
    
    digits = ''.join(filter(str.isdigit, phone_number))
    if len(digits) == 11 and digits[0] == '1':
        digits = digits[1:]
    return digits

def overlaps_days(start1, end1, start2, end2, days = 90):
    today = datetime.today().date()
    end_or_today1 = end1 or today
    end_or_today2 = end2 or today
         
    if(start1 <= end_or_today2 and end_or_today1 >= start2) or (start2 <= end_or_today1 and end_or_today2 >= start1):
        diff = 0
        # When one range contains another
        if(start1 <= start2) and (end_or_today1 >= end_or_today2):
            diff = end_or_today2 - start2
             
        # When one range is included in the other
        if(start2 <= start1) and (end_or_today1 <= end_or_today2):
            diff = end_or_today1 - start1

        # When ranges partially intercept - right
        if(start1 >= start2) and (end_or_today1 >= end_or_today2):
            diff = end_or_today2 - start1

        #When ranges partially intercept - left
        if(start1 <= start2) and (end_or_today1 <= end_or_today2):
            diff = end_or_today1 - start2
        
        return diff.days >= days
    else:
        return False