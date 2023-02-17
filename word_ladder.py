#!/bin/python3


from copy import deepcopy
def word_ladder(start_word, end_word, dictionary_file=('words5.dict')):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]
    from collections import deque
    dictionary_file = open('words5.dict')
    dictionary = []
    for line in dictionary_file:
        dictionary.append(line.strip())
    start = list([])
    start += [start_word]
    q = deque()
    q.append(start)
    while len(q) != 0:
        x = q.popleft()
        i = 0
        while i < len(dictionary):
            if _adjacent(dictionary[i], x[-1]):
                if dictionary[i] == end_word:
                    x.append(dictionary[i])
                    answer = x
                    return answer
                new = deepcopy(x)
                #new = x.copy()
                new.append(dictionary[i])
                q.append(new)
                dictionary.remove(dictionary[i])
            else:
                i += 1
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == []:
        return False
    for x in range(len(ladder) - 1):
        if not _adjacent(ladder[x], ladder[x + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    count = 0
    for x in range(len(word1)):
        if word1[x] != word2[x]:
            count += 1
    if count == 1:
        return True
    return False
