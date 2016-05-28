# name_collisions
A couple of functions that help in dealing with lists of names that may not be unique, but have to be made unique.  Also supports length constraints.

It's really annoying when you have a list of names that are supposed to be unique, but aren't.  It's even more annoying when you have to deal with length constraints on those names.  For ecample, when you need to input these names into the excel tab name property, which has a maximum length of 30 characters.  I have written two functions to hopefully make your life a little bit easier when you run into this problem.

Function the first: find_collisions(in_list, max_length=0):

This function takes a list and an optional max_length parameter, and returns a dictionary counting the number of collisions that will occur given a hypothetical truncation at this character index.

Function the second: remove_collisions(in_list, max_length=0, base=10):

This function takes a list, the optional max_length parameter as described above in find_collisions(), and another optional base parameter.  It iterates through the list and tacks on an incrementing number to the end of a name if a collision is detected.  If the max_length is shorter than required to tack on the number, it gets right-padded, overwriting the string just enough to add the number.  If you need more room, you can tell it to count in hex by setting the base parameter to 16.

Output is a list in the same order as the original in_list, but with collisions removed.

It's not a terribly pretty output, but at least you know that each one is unique.

A couple of notes:

Things start to get screwy if the incrementing numbers themselves start to get longer than the max_length.  I tried to figure out a way to detect and stop this but haven't come across one yet.  But I think if you are working under such tiny length constraints you are going to have to take a radically different approach anyway.

I wanted to have find_collisions return a dict that only contains entries where there are actually collisions occuring, but it was proving too much of a headache to remove items from a dict while iterating through it.
