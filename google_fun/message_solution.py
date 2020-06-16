from itertools import permutations


def solution(l):
    # You don't have to use all of the numbers.
    # Given a list of numbers, get the highest possible number divisible by three.
    found = False
    answer = 0
    # Step 1: Get the length of the list.
    max_length = len(l)
    for length in reversed(range(1, max_length + 1)):
        # Step 7: If not, find all permutations using length of max - 1 and repeat steps 2 to 6.
        if not found:
            # Step 2: Using permutation from itertools, get all permutations for the entire list and the length of the list.
            perms = permutations(l, length)
            possibilities = [''.join([str(i) for i in x]) for x in perms]
            #get rid of duplicates
            possibilities = list(set(possibilities))
            # Step 3: Sort in descending order. 
            possibilities.sort(reverse=True)
            # Step 4: For each item in list, check to see if divisible by 3.
            for number in possibilities:
                if int(number) % 3 == 0:
                    # Step 5: If it's divisible, break.
                    found = True
                    # Step 6: Return the last value.
                    answer = int(number)
                    break
        else:
            answer = int(number)
            break
    return answer

