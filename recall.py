#!/usr/bin/env python

import os
import sys
import subprocess
import webbrowser

current_directory = os.getcwd()
tags = sys.argv[1:]

if not tags:
    print >>sys.stderr, "Hey, you need to give me some tags"
    sys.exit(1)

tags = set([t.lower() for t in tags])

matched_filenames = []
for filename in os.listdir(current_directory):
    without_ext = filename.rsplit(".", 1)[0]  # strip out extension if exists
    filename_tags = without_ext.lower().split(",")
    filename_tags = [t.strip() for t in filename_tags]
    if tags & set(filename_tags):
        # tags intersect
        matched_filenames.append(filename)

if not matched_filenames:
    print >>sys.stdout, "Hmm.. no matching files"
    
for f in matched_filenames:
    webbrowser.open(f)
