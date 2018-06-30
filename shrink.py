infilename = "ebook-list-authors.txt"
outfilename = "ebook-list-authors-shrunk.txt"

lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
