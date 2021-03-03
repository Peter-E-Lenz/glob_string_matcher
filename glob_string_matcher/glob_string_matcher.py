from fnmatch import filter as glob_filter
from editdistance import eval as __edit_dist

def __match_fitness_filter(st,a,b,dist_func):
    "Given a string to compare to and two glob format patterns (as strings) it returns the pattern that has the lowest edit distance to the string as determined by dist_func"
    if a==None and b!=None:
        return b
    elif b==None and a!=None:
        return a
    else:        
        ed_a=dist_func(st,a)
        ed_b=dist_func(st,b)
    
        if  ed_a>=ed_b:
            return a
        else:
            return b

def glob_match(strings,patterns,distance_func=__edit_dist):
    "Given an iterable of strings to test and glob format patterns(also strings) it returns a dictionary whose keys are members of strings and value is the best matching pattern where best is defined as the pattern with the lowest edit distance as determined by distance_func. By default this is Levenshtein distance but a custom distnace function can be supplied as longs as it accepts two strings as input and returns an int in the form DISTANCE_FUNCTION(STRING_A:string STRING_B:string) -> INT. This algorithim uses hill-climbing to determine the best function and thus uses less memory"
    res={s:None for s in strings}
    for pattern in patterns:
        matching=glob_filter(strings,pattern)
        for match in matching:
            res[match]=__match_fitness_filter(match,res[match],pattern,distance_func)
    return {r:res[r] for r in res if res[r] != None}

def glob_match_all(strings,patterns):
    "Given an iterable of strings to test and glob format patterns (also strings) it returns a dictionary whose keys are members of strings and values are a list of patterns that match said key. Since this function stores all matches it uses more memory"
    res={s:[] for s in strings}
    for pattern in patterns:
        matching=glob_filter(strings,pattern)
        for match in matching:
            res[match].append(pattern)
    return {r:res[r] for r in res if len(res[r]) > 0}