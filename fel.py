#!/bin/env python3

import itertools as it
import hashlib as hl
import multiprocessing as mp


def main():
    target = 'cbd6dce96e2f33c6ba04cb7d640e160c'
    wordlist = 'dictionary.txt'

    with open(wordlist) as f:
        print('started read file')
        words = [x.rstrip('\n') for x in f]
        print('file read finished')

    word4 = [x for x in words if len(x) == 4]
    print(len(word4), word4[0])
    word2 = [x for x in words if len(x) == 2]
    print(len(word2), word2[0])
    word6 = [x for x in words if len(x) == 6 and x[0] == 'A']
    print(len(word6), word6[0])

    def work(x):
        if hl.md5(bytes(' '.join(x), 'utf-8')).hexdigest() == target:
            print(str(' '.join(x)))
            return True

    with mp.Pool(maxtasksperchild=10000000) as p:
        a = p.imap_unordered(work, it.product(word4, word2, word6), 1000000)
        for _ in a:
            if _:
                break

    print('Finished search')
if __name__ == '__main__':
    main()
