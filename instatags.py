#!/usr/bin/env python3

r"""Command-line tool to manage Instagram tags by category

USAGE::
    add usage someday

"""

import argparse
import itertools
import json

TAGFILE = '/Users/cmills/Proj/InstaTools/instagram_tags.json'

def main():
    description = ('Command-line tool to manage Instagram tags by category.')
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-i', '--infile', nargs='?', type=argparse.FileType(),
                        help='JSON file containing tag data', default=TAGFILE)
    parser.add_argument('-c', '--categories', nargs='*',
                        help='List of categories', default=[]) 
    parser.add_argument('-a', '--add_tags', nargs='*',
                        help='List of tags to add to a category', default=[])
    parser.add_argument('-d', '--del_tags', nargs='*', 
                        help='List of tags to delete from a category', default=[])
    parser.add_argument('-p', '--plus_tags', nargs='*',
                        help='List of tags to include in output, but not save', default=[])
    options = parser.parse_args()

    infile     = options.infile
    categories = options.categories
    add_tags   = ['#'+t for t in options.add_tags]
    del_tags   = ['#'+t for t in options.del_tags]
    plus_tags  = ['#'+t for t in options.plus_tags]

    with infile:
        try:
            obj = json.load(infile)
        except ValueError as e:
            raise SystemExit(e)

        changes_flag = False 
        if len(categories) == 1:
            category = categories[0]
            if len(add_tags) > 0:
                for t in add_tags:
                    if obj[category].count(t) == 0:
                        obj[category].append(t)
                        print('Added {} to category {}'.format(t, category))
                        changes_flag = True
                    else:
                        print('Skipping {} for category {}, already there'.format(t, category))


            if len(del_tags) > 0:
                for t in del_tags:
                    if obj[category].count(t) > 0:
                        obj[category].remove(t)
                        print('Removed {} from category {}'.format(t, category))
                        changes_flag = True
                    else:
                        print('Skipping {} for category {}, wasn\'t there'.format(t, category))

        if categories and not changes_flag:
            cat_lists = [obj.get(c, []) for c in categories]   # using get() to deal with invalid
            out = list(itertools.chain.from_iterable(cat_lists))
            out = plus_tags + out
            print('\n'.join(out))
        else:
            print(json.dumps(obj, sort_keys=True, indent=4))

if __name__ == '__main__':
    main()
