#!/usr/bin/env python
from __future__ import print_function

import os
import sys
import webbrowser

current_directory = os.getcwd()
tags = sys.argv[1:]

if not tags:
    print("Hey, you need to give me some tags", file=sys.stderr)
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
    print("Hmm.. no matching files", file=sys.stdout)
    
for f in matched_filenames:
    browser_friendly_path = "file://{}".format(os.path.abspath(f))
    print(browser_friendly_path)
    webbrowser.open(browser_friendly_path)
