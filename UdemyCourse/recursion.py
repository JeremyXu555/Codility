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

### Permutation

def permute(s):

    out = []

    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):

            for perm in permute(s[:i] + s[i+1:]):
                ## try to see the way human manually do the permutation, hold one
                ## letter and keep changing the rest of the letters, we are actually
                ## doing the recursion in our brain without notice it
                out += [let + perm]
    return out
