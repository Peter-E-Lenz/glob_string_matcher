Glob_string_matcher provides unix-style glob pattern matching for python strings. It exposes two functions; one that lists only the best matching pattern per-string and one that lists all matching patterns per-string.

glob_match(strings:LIST OF STRINGS,patterns:LIST OF STRINGS,distance_func:OPTIONAL FUNCTION) -> DICTIONARY OF STRINGS:
Given an iterable of strings to test and glob format patterns(also strings) it returns a dictionary whose keys are members of strings and value is the best matching pattern where best is defined as the pattern with the lowest edit distance as determined by distance_func. By default this is Levenshtein distance but a custom distnace function can be supplied as longs as it accepts two strings as input and returns an int in the form DISTANCE_FUNCTION(STRING_A:string STRING_B:string) -> INT. This algorithim uses hill-climbing to determine the best function and thus uses less memory

glob_match_all(strings:LIST OF STRINGS,patterns:LIST OF STRINGS) -> DICTIONARY OF LISTS OF STRINGS:
Given an iterable of strings to test and glob format patterns (also strings) it returns a dictionary whose keys are members of strings and values are a list of patterns that match said key. Since this function stores all matches it uses more memory
