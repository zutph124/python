Recall that the re module comes with quite a few functions, per docs.python.org/3/library/re.html, including search and findall.
Recall that regular expressions support quite a few special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best to use Python’s raw string notation for regular expression patterns, else pytest will warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,” per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, which you can access individually with group, per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.

Note that * and + are “greedy,” insofar as “they match as much text as possible,” per docs.python.org/3/library/re.html#regular-expression-syntax. Adding ? immediately after either, a la *? or +?, “makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched.”

Note that \b is “defined as the boundary between a \w and a \W character (or vice versa), or between \w at the beginning/end of the string,” per docs.python.org/3/library/re.html#regular-expression-syntax.
You might find regex101.com or regexr.com helpful for testing regular expressions (and visualizing matches).
See thefreedictionary.com/words-containing-um for some words that contain “um”.
