usage: instatags.py [-h] [-i [INFILE]] [-c [CATEGORIES [CATEGORIES ...]]]
                    [-a [ADD_TAGS [ADD_TAGS ...]]]
                    [-d [DEL_TAGS [DEL_TAGS ...]]]
                    [-p [PLUS_TAGS [PLUS_TAGS ...]]]

Instagram tags ar eessential to getting your post noticed, but they're a pain in the arse.  This command-line tool helps you  manage Instagram tags by category, hopefully making the process a little easier.

optional arguments:
  -h, --help            show this help message and exit
  -i [INFILE], --infile [INFILE]
                        JSON file containing tag data
  -c [CATEGORIES [CATEGORIES ...]], --categories [CATEGORIES [CATEGORIES ...]]
                        List of categories
  -a [ADD_TAGS [ADD_TAGS ...]], --add_tags [ADD_TAGS [ADD_TAGS ...]]
                        List of tags to add to a category
  -d [DEL_TAGS [DEL_TAGS ...]], --del_tags [DEL_TAGS [DEL_TAGS ...]]
                        List of tags to delete from a category
  -p [PLUS_TAGS [PLUS_TAGS ...]], --plus_tags [PLUS_TAGS [PLUS_TAGS ...]]
                        List of tags to include in output, but not save


Inspecting the tag hierarchy.  Prints to STDOUT.
++++++++++++++++++++
To print out entire tag hierarchy:

    instatags.py

Creating the tag list for a post:
++++++++++++++++++++++++++++++++++++++++++++++++++

To print out tags for a list of categories:

    instatags.py -c <category1> <category2>

To print out additional tags you want in your post, but don't want to add to hierarchy:
 
    instatags.py -p <tag1> <tag2> <tag3> 

    (don't include the '#' in the tag name, that'll be added)

Updating the tag hierarchy:
    + add tags you plan to use frequently 
    + remove tags you no longer want
+++++++++++++++++++++++++++++++++++++++++++++++++++

To add new tags to a category.  Prints out the updated tag hierarchy:

    instatags.py -c <category> -a <tag1> <tag2> <tag3>

To remove existing tags from a category.  Prints out the updated hierarchy:

    instatags.py -c <category> -d <tag1> <tag2> <tag3>

