import Utilities

def parse_story(file_name):
    ''' 
    (str) -> List[str]
    
    Returns the an ordered list of the words in file_name with "bad characters" (", (, ), {, }, [, ], _) removed
    
    >>> parse_story('test_text_parsing.txt')
    ['the', 'code', 'should', 'handle', 'correctly', 'the', 'following', ':', 'white', 'space', '.', 'sequences', 'of', 'punctuation', 'marks', '?', '!', '!', 'periods', 'with', 'or', 'without', 'spaces', ':', 'a', '.', '.', 'a', '.', 'a', "don't", 'worry', 'about', 'numbers', 'like', '1', '.', '5', 'remove', 'capitalization']
    '''
    
    test_file = open('test_text_parsing.txt')
    file_to_list = []
    lines = test_file.readlines()
    whitelines = lines.count("\n")
    
    for i in range(whitelines):
        lines.remove("\n")
    for number in lines:
        templist = []
        string = ''
        for character in number:
            if (character != ' ') and (character != '\n') and (character not in Utilities.VALID_PUNCTUATION) and (character not in Utilities.BAD_CHARS):
                templist.append(character)
                
            else:
                if len(templist) >= 1:
                    combine = string.join(templist)
                    file_to_list.append(combine.lower())
                    templist = []
                
            if character in Utilities.VALID_PUNCTUATION:
                file_to_list.append(character)
                
    return file_to_list
    
def get_prob_from_count(counts):
    '''
    (List[int]) -> List[float]
    
    Given a list of positive integer counts, this function returns a list of probabilities associated with these counts
    
    >>> get_prob_from_count([10, 20, 40, 30]) 
    [0.1, 0.2, 0.4, 0.3]
    '''
    
    output = []
    for i in counts:
        output.append(i / 100)
    return output
    
def build_ngram_counts(words, n):
    '''
    (List[str], int) -> Dict{tup: List[List[str], List[int]}
    
    Given a list of words and n, this function returns a dictionary of n-grams and the counts of the words following that n-gram.
    
    >>> words = [‘the’, ‘child’, ‘will’, ‘go’, ‘out’, ‘to’, ‘play’, ‘,’, ‘and’, ‘the’, ‘child’, ‘can’, ‘not’, ‘be’, ‘sad’, ‘anymore’, ‘.’]
    >>> build_ngram_counts(words, 2)
    {(‘the’, ‘child’): [[‘will’, ‘can’], [1, 1]],
    (‘child’, ‘will’): [[‘go’], [1]],
    (‘will’, ‘go’): [[‘out’], [1]],
    (‘go’, out’): [[‘to’], [1]],
    (‘out’, ‘to’): [[‘play’], [1]], 
    (‘to’, ‘play’): [[‘,’], [1]], 
    (‘play’, ‘,’): [[‘and’], [1]], 
    (‘,’, ‘and’): [[‘the’], [1]], 
    (‘and’, ‘the’): [[‘child’], [1]], 
    (‘child’, ‘can’): [[‘not’], [1]], 
    (‘can’, ‘not’): [[‘be’], [1]], 
    (‘not’, ‘be’): [[‘sad’], [1]], 
    (‘be’, ‘sad’): [[‘anymore’], [1]], 
    (‘sad’, ‘anymore’): [[‘.’], [1]]}
    '''
    
    dictionary = {}
    keys = []
    for i in range(len(words) - (n )):
        words_in_tuple = []
        for j in range(n):
            words_in_tuple.append(words[j + i])
        tuples = tuple(words_in_tuple)
        
        isDuplicate = False
        for j in range(len(keys)):
            if keys[j] == tuples:
                isDuplicate = True
        if isDuplicate == False:
            keys.append(tuples)
    
    for x in range(len(keys)):
        values = []
        list1 = []
        list2 = []
        for y in range(len(words) - n):
            isSame = True
            for i in range(n):
                if keys[x][i] != words[y + i]:
                    isSame = False
            if isSame and words[y + n] not in list1:
                list1.append(words[y + n])
                list2.append(1)
            elif isSame:
                for t in range(len(list1)):
                    if list1[t] == words[y + n]:
                        list2[t] += 1
        values.append(list1)
        values.append(list2)
        dictionary[keys[x]] = values
        
    return dictionary

def prune_ngram_counts(counts, prune_len):
    '''
    (Dict{tup: List[List[str], List[int]]}, int) -> Dict{tup: List[List[str], List[int]}
    
    Given a dictionary with n-grams and counts, this function goes through and keeps the prune_len highest frequency words.
    
    >>> prune_ngram_counts({(‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’, ‘no’], [20, 20, 10, 2]], (‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [8, 7, 5, 5]], ('toronto’, ‘is’): [[‘six’, ‘drake’], [2, 3]]}, 3)
    {(‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’], [20, 20, 10]], (‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [8, 7, 5, 5]], ('toronto’, ‘is’): [[‘six’, ‘drake’], [2, 3]]}
    '''
     #use a sort to sort list2 in values and swap list1 accordingly
    for key in counts.keys():
        list1 = counts[key][0]
        list2 = counts[key][1]
        
        #perform sort on count_list 
        for x in range(len(list2)):
            maximum = x
            temp_list = []
            for y in range(x + 1, len(list2)):
                if list2[maximum] < list2[y]:
                    maximum = y
            list2[x], list2[maximum] = list2[maximum], list2[x]
            list1[x], list1[maximum] = list1[maximum], list1[x]  
            
                    
            temp_list.append(list1[0 : prune_len])
            temp_list.append(list2[0 : prune_len])
            counts.update({key: temp_list})
        
    return counts


def probify_ngram_counts(counts):
    '''
    (Dict{tup: List[List(str), List(int)]}) -> Dict{tup: List[List(str), List(float)]}
    
    This function takes in a dictionary of n-grams and counts and converts the counts to probabilities
    
    >>> probify_ngram_counts({(‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’], [20, 20, 10]], (‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [8, 7, 5, 5]], ('toronto’, ‘is’): [[‘six’, ‘drake’], [2, 3]]}
    {
    (‘i’, ‘love’): [[‘js’, ‘py3’, ‘c’], [0.4, 0.4, 0.2]], (‘u’, ‘r’): [[‘cool’, ‘nice’, ‘lit’, 'kind’], [0.32, 0.28,
    0.2, 0.2]],
    ('toronto’, ‘is’): [[‘six’, ‘drake’], [0.4, 0.6]]
    }
    '''
    
    for key in counts.keys():
        list1 = counts[key][0]
        list2 = counts[key][1]
        temp_list = []
        total = 0
        for i in range(len(list2)):
            total += list2[i]
        for x in range(len(list2)):
            list2[x] = list2[x] / total
        
        temp_list.append(list1)
        temp_list.append(list2)
        counts.update({key: temp_list})
        
    return counts    


def build_ngram_model(words, n):
    '''
    (List[words], int) -> Dict{tup: List[List(str), List(float)]}
    
    This function returns a dictionary in the same format as the output of probify_ngram_counts. The results should appear in descending order of probability, and only the 15 most likely words should be kept.
    
    >>> build_ngram_model([‘the’, ‘child’, ‘will’, ‘the’, ‘child’, ‘can’, ‘the’, ‘child’, ‘will’, ‘the’, ‘child’, ‘may’, ‘go’, ‘home’, ‘.’], 2)
    {
    (‘the’, ‘child’): [[‘will’, ‘can’, ‘may’], [0.5, 0.25, 0.25]],
    (‘child’, ‘will’): [[‘the’], [1.0]], (‘will’, ‘the’): [[‘child’], [1.0]], (‘child’, ‘can’): [[‘the’], [1.0]], (‘can’, ‘the’): [[‘child’], [1.0]], (‘child’, ‘may’): [[‘go’], [1.0]], (‘may’, ‘go’): [[‘home’], [1.0]], (‘go’, ‘home’): [[‘.’], [1.0]]
    }
    '''
    dictionary = build_ngram_counts(words, n)
    
    pruned_dictionary = prune_ngram_counts(dictionary, 15)
    
    probified_dictionary = probify_ngram_counts(pruned_dictionary)
    
    return probified_dictionary


def gen_bot_list(ngram_model, seed, num_tokens=0):
    '''
    (Dict{tup: List[List(str), List(float)]}, int, int) -> List[str]
    
    This function returns a randomly generated list of strings that begins with the tokens in seed. The list cannot be longer than num_tokens.
    
    >>> ngram_model = {('the', 'child'): [['will', 'can','may'], [0.5, 0.25, 0.25]],
    ('child', 'will'): [['the'], [1.0]], ('will', 'the'): [['child'], [1.0]], ('can', 'the'): [['child'], [1.0]], ('child', 'may'): [['go'], [1.0]], ('may', 'go'): [['home'], [1.0]], ('go', 'home'): [['.'], [1.0]] }
    >>> gen_bot_list(ngram_model, ('hello', 'world')) []
    >>> gen_bot_list(ngram_model, ('hello', 'world'), 5) ['hello', 'world']
    >>> gen_bot_list(ngram_model, ('the', 'child'), 5) ['the', 'child', 'can']
    Note that the removal of the crossed out ('child', 'can') 2-gram is the reason for the termination.
    >>> gen_bot_list(ngram_model, ('the', 'child'), 5) ['the', 'child', 'will', 'the', 'child']
    '''
    seeds = list(seed)
    final = []
    keys = []
    for i in ngram_model.keys():
        keys.append(i)
    start = None
    
    for j in range(len(keys)):
        if seed == keys[j]:
            start = j
   
    if len(seed) > num_tokens:
        for i in range(num_tokens):
            final.append(seeds[i])
    elif start == None:
        final = seeds
    else:
        for x in range(len(keys)):
            spot = len(seeds)
            if spot >= num_tokens or start == None:
                final.append(seeds)
                return seeds
            else:
                begin = start
                temp = Utilities.gen_next_token(keys[begin], ngram_model)
                seeds.append(temp)
            for y in range(len(keys)):
                if temp == keys[y][len(seed) - 1]:
                    start= y
                    break
                else:
                    start = None
        return output

        

def gen_bot_text(token_list, bad_author):
    '''
    (List[str], bool) -> str
    
    If bad_author == True, this function returns the words in token_list as a string separated by spaces. If bad_author == False, the tokens are turned into a string where there are no spaces before any valid_punctuation, and is capitalized properly. 
    
    >>> gen_bot_text(['this', 'is', 'a', 'string', 'of', 'text', '.', 'which', 'needs', 'to', 'be', 'created', '.'], False)
    'This is a string of text. Which needs to be created.'
    '''

    output = ''
    if bad_author:
        list_with_spaces = []
        for i in range(len(token_list)):
            list_with_spaces.append(token_list[i])
            if i < len(token_list) - 1:
                list_with_spaces.append(" ")

        output = output.join(list_with_spaces)
        return output
    
    elif bad_author == False:
        good_list = []
        valid_punctuation = Utilities.VALID_PUNCTUATION
        end_punctuation = Utilities.END_OF_SENTENCE_PUNCTUATION
        capitalize = Utilities.ALWAYS_CAPITALIZE
        
        good_list.append(token_list[0].capitalize())
        for i in range(1, len(token_list)):
            if i != (len(token_list) - 1):
                if token_list[i] in valid_punctuation:
                    good_list.append(token_list[i])
                    good_list.append(" ")
            else:
                good_list.append(token_list[i])
            if (token_list[i - 1] in end_punctuation) or (token_list[i].capitalize() in capitalize):
                good_list.append(" ")
                good_list.append(token_list[i].capitalize())
            elif token_list[i] not in valid_punctuation:
                good_list.append(" ")
                good_list.append(token_list[i])   
        output = output.join(good_list)
        return output
    
    


if (__name__ == "__main__"):
    '''
    test_file = open('test_text_parsing.txt')
    print(parse_story(test_file))
    print(get_prob_from_count([25, 60, 5, 10]))
    print(build_ngram_counts(["the", "child", "will", "go", "out", "to", "play", ",", "and", "the", "child", "can", "not", "be", "sad", "anymore", "."], 2))
    ngram_counts = {('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]], ('u', 'r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]], ('toronto', 'is'): [['six', 'drake'], [2, 3]]}
    print(prune_ngram_counts(ngram_counts, 3))
    print(probify_ngram_counts(ngram_counts))
    words = ["the", "child", "will", "the", "child", "can", "the", "child", "will", "the", "child", "may", "go", "home", "."]
    tester = build_ngram_model(words, 2)
    print(gen_bot_list(tester, ('the', 'child'), 5))
    token_list = ['this', 'is', 'a', 'string', 'of', 'text', '.', 'which', 'needs', 'to', 'be', 'created', '.']
    print(gen_bot_text(token_list, False))
    text = ' '.join(parse_story('308.txt'))
    '''
    