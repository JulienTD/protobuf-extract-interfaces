#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("USAGE: python3 {0} SOURCE_FILE_PATH DEST_FILE_PATH".format(sys.argv[0]))
    sys.exit(1)

print("Extracting interfaces from {0}".format(sys.argv[1]))

dest_lines = []

source_file = open(sys.argv[1], "r")
source_lines = source_file.readlines()

need_to_skip = False

for line in source_lines:
    clean_line = line.strip()
    if clean_line.startswith("import"):
        continue
    if clean_line.startswith("class"):
        need_to_skip = True
    if need_to_skip == False:
        if clean_line.startswith("interface"):
            dest_lines.append(line.replace("interface", "export interface"))
        elif clean_line.startswith("enum"):
            dest_lines.append(line.replace("enum", "export enum"))
        else:
            dest_lines.append(line)
    if clean_line.startswith("}") and len(clean_line) <= 2:
        need_to_skip = False
source_file.close()

dest_file = open(sys.argv[2], 'w')
dest_file.writelines((dest_lines))
dest_file.close()

print("Interfaces have been extracted to {0}".format(sys.argv[2]))
