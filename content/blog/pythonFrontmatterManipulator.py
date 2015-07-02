import re
import sys
import os
import glob

new_author = "rami_taibah" # Changethe new author here
new_layout = "post"        # Change the new layout here
new_categories = "Blog Linux Linuxologist"    # Change categories here; space seperated
new_tags = ""              # Change tags here; space seperated


######################################################################
#                               TODO                                 #
######################################################################

# Load only frontmatter not the full blogpost, write it to a temp file and replace 
# it in the original blogpost

# Add new attributes to the frontmatter





# Change the Author of a post in a YAML front matter
def changeAuthor(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  change_author = re.sub( r'author:.*','author: ' + new_author, mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(change_author)
  fo.truncate()
  fo.close


# Change the Layout of a post in a YAML front matter
def changeLayout(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  change_layout= re.sub( r'layout:.*','layout: ' + new_layout, mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(change_layout)
  fo.truncate()
  fo.close


# Change categories of a post in a YAML front matter
def changeCategory(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  change_categories= re.sub( r'(categories:\n)(-.*\n)+(?=---)' | r'(categories:.+','categories: ' + new_categories +'\n', mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(change_categories)
  fo.truncate()
  fo.close


# Change tags of a post in a YAML front matter
def changeTags(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  change_tags= re.sub( r'(tags:\n)(-.*\n)+(?=---)','tags: ' + new_tags+'\n', mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(change_tags)
  fo.truncate()
  fo.close


# When converting an old Wordpress blog into markdown, the tool used (npm html-markdown) grabbed some front matter that is no longer valid or I otherwise do not need: tweetbackscheck, shorturls, twittercomments, and tweetcount. We remove these here.

def deleteShorturls(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  delete_shorturls= re.sub( r'(shorturls:\n)(-.*\n)+','', mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(delete_shorturls)
  fo.truncate()
  fo.close
  

def deleteTweetbackscheck(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  delete_tweetbackscheck= re.sub( r'(tweetbackscheck:\n)(-.*\n)+','', mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(delete_tweetbackscheck)
  fo.truncate()
  fo.close


def deleteTwittercomments(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  delete_twittercomments= re.sub( r'(twittercomments:\n)(-.*\n)+','', mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(delete_twittercomments)
  fo.truncate()
  fo.close


def deleteTweetcount(filename):
  fo = open(filename, "r+")
  mdFile= fo.read()
  delete_tweetcount= re.sub( r'(tweetcount:\n)(-.*\n)+','', mdFile, re.M|re.I)
  fo.seek(0)
  fo.write(delete_tweetcount)
  fo.truncate()
  fo.close()


for filename in glob.iglob(os.path.join('*.md')):
    #changeAuthor(filename)
    #changeLayout(filename)
    changeCategory(filename)
    #changeTags(filename)
    #deleteShorturls(filename)
    #deleteTweetbackscheck(filename)
    #deleteTwittercomments(filename)
    #deleteTweetcount(filename)

