import re
def multi_bracket_validation(input):
    
    value=False
    if input.count('{')==input.count('}') and input.count('(')==input.count(')') and \
        input.count('[')==input.count(']'):
        value=True
    try :
        if re.search("\(.?}", input) or re.search("\[.?}", input) or \
            re.search("\[.?)", input) or re.search("\(.?]", input) or \
            re.search("\{.?)", input) or re.search("\{.?]", input):
            value=False
    except:
        return value
    return value








print(multi_bracket_validation('{}(){}'))

