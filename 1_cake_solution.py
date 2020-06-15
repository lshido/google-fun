import pdb


def solution(s):
    """Given a string, abcabcabcabc, return 4 equal parts
    """
    # Step 1: Get the complete list of sub-strings for the entire string by iterating.
    substrings = get_substrings(s)
    pdb.set_trace()
    for sub in substrings:
        # Step 2: For each sub-string, test if a.count(sub-string) is greater than 0.If not, continue to next substring.
        if not substring_in_string(sub, s):
            continue
        else:
            # Step 3: If it is, check that there are no leftover bits.
            if not no_leftovers(sub, s):
                continue
            else:
                # Step 5: If it is, break, and return a.count(sub-string).
                break

    return s.count(sub)


def get_substrings(s):
    substrings = []
    for i in range(1, len(s)+1):
        substrings.append(s[:i])
    return substrings


def substring_in_string(substring, s):
    if s.count(substring) > 0:
        return True
    else:
        return False


def no_leftovers(substring, s):
    if len(s) - (len(substring) * s.count(substring)) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    solution('abcabc')