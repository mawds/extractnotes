#!/usr/bin/env python

"""Extract speaker's notes from an Markdown presentation.  """

import sys
import re

if len(sys.argv) <= 1:
   print "Pass the name of the presentation to extract the notes from as an argument" 
   quit()
else:
    infile = sys.argv[1]

slide_regex = re.compile(r"^(#|-{3})(.*)")
comment_regex = re.compile(r"\[\]\((.+)\)")

current_slide = "Untitled"

with open(infile, "r") as f:
    for line in f:
        slidematch = slide_regex.findall(line)
        commentmatch = comment_regex.findall(line)
        if slidematch:
            if len(slidematch[0][1]) > 0:
                current_slide = slidematch[0][1]
            else:
                current_slide = current_slide + "+"
        elif commentmatch:
                # Comments will also extract images, so we filter these out
                if not re.findall(r"\.(png|jpg|jpeg)", commentmatch[0]):
                    print current_slide
                    print commentmatch[0]
                    print
        
