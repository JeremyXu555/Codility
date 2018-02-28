### reverse the string

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        m = int(len(s) / 2)
        ## swap the string left half and right half
        return reverse(s[m:]) + (reverse((s[:m])))

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        # grab the first character of each recursion and put it on the back
        # of the string
        reverse(s[1:]) + s[0]
