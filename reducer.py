#!/usr/bin/python3

"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

sys.path.append('.')

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print("%s%s%d" % (current_word, separator, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    main()
#total = 0
#lastword = None

#for line in sys.stdin:
 #   line = line.strip()

    # recuperer la cle et la valeur et conversion de la valeur en int
  #  word, count = line.split()
   # count = int(count)

    # passage au mot suivant (plusieurs cles possibles pour une même exécution de programme)
   # if lastword is None:
   #     lastword = word
   # if word == lastword:
   #     total += count
   # else:
     #   print("%s\t%d occurences" % (lastword, total))
    #    total = count
      #  lastword = word

#if lastword is not None:
 #  print("%s\t%d occurences" % (lastword, total))