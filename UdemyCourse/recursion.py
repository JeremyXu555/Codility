### reverse the string

def reverse(s):
    if len(s) <= 1:
        return s
    else:
        m = int(len(s) / 2)
        ## swap the string left half and right half
        return reverse(s[m:]) + (reverse((s[:m])))
