def find_collisions(in_list, max_length=0):

    """
    Takes a list of names and count all the collisions by storing every unique item in a dictionary and incrementing its
    value every time a collision is found.  A length constraint can be specified with "max_length".  This will check for
    collisions after every name in the list is truncated to its max length.

    @param in_list A list of strings.
    @type in_list List
    @param max_length Maximum length of all items in the list given a hypothetical truncation at this char index.  For
                      example, "apple_pie" and "apple_strudel" will collide with a max_length of 6 or below, but will
                      not collide with a higher max_length.
    @type max_length int
    """

    count_dict = {}

    # If there is no max_length...
    if max_length == 0:
        for name in in_list:
            
            # Put name in count_dict, initialize its value at 0 and increment it every time there a collision is found.
            if name not in iter(count_dict):
                count_dict[name] = 0
            else:
                count_dict[name] += 1

    # If there is a max_length...
    else:
        for name in in_list:

            # Put every name (truncated at max_length) in count_dict, initialize its value at 0 and increment it every
            # time there a collision is found.
            if name[:max_length] not in iter(count_dict):
                count_dict[name[:max_length]] = 0
            else:
                count_dict[name[:max_length]] += 1

    return count_dict

def remove_collisions(in_list, max_length=0, base=10):

    """
    Takes a list of names and removes all collisions by sticking incrementing numbers to the end.  A length constraint
    can be specified with "max_length".  In the event of a length constraint, the incrementing number will be
    right-padded in the returned name.  If you need extra room, "base" can be set to 16 to encode the incrementing
    number as hex.  Returns a list of values with collisions removed in the same order as the original.

    @param in_list A list of strings.
    @type in_list List
    @param max_length Maximum length of all returned strings.  Default is 0, which means no maximum length.
    @type max_length int
    @param base Base with which to increment the appended numbers.  Default is 10, but can also be set to 16.
    @type base int
    """

    count_dict = {}
    out_list = []

    # If there is no max_length...
    if max_length == 0:
        for name in in_list:

            # If name is not already a key in count_dict, append it to out_list and add it to count_dict as a key with a
            # value of 1.
            if name not in iter(count_dict):
                out_list.append(name)
                count_dict[name] = 1

            # Otherwise, append it to out_list with its current value in count_dict, and increment the value by 1.
            else:
                if base == 10:
                    out_list.append(name + str(count_dict[name]))
                elif base == 16:
                    # (the read the [2:] slice is here is because it will otherwise add '0x' to the front)
                    out_list.append(name + str(hex(count_dict[name]))[2:])
                count_dict[name] += 1

    # If there is a max_length...
    else:
        for name in in_list:

            # If the name (truncated to its max_length) is not already a key in count_dict, append it to out_list and
            # add it to count_dict as a key with a value of 1.
            if name[:max_length] not in iter(count_dict):
                out_list.append(name[:max_length])
                count_dict[name[:max_length]] = 1

            # Otherwise, stick the count_dict value to the end of it (right-padded, given the max_length), append it to
            # out_list and increment the value by 1.
            else:
                if base == 10:
                    unique_name_base = name[:max_length-len(str(count_dict[name[:max_length]]))]
                    unique_name_num = str(count_dict[name[:max_length]])
                    out_list.append(unique_name_base + unique_name_num)
                elif base == 16:
                    # (the read the [2:] slice is here is because it will otherwise add '0x' to the front)
                    unique_name_base = name[:max_length-len(str(hex(count_dict[name[:max_length]])[2:]))]
                    unique_name_num = str(format(hex(count_dict[name[:max_length]])[2:]))
                    out_list.append(unique_name_base + unique_name_num)
                count_dict[name[:max_length]] += 1

    return out_list
