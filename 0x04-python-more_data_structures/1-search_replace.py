#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_destroy(x):
        return(x if x!=search else replace)
    return list(map(search_destroy, my_list))
