#! /bin/bash

scripts=`dirname "$0"`
base=$scripts/..

data=$base/data

tools=$base/tools

# tokenize, fix vocabulary upper bound

cat $data/adv_cleaned.txt | python $base/scripts/preprocess.py --vocab-size 8000 --tokenize --lang "en" --sent-tokenize > \
    $data/adv_preprocessed_large.txt

# split into train, valid and test

head -n 800 $data/adv_preprocessed_large.txt > $data/adv_large/valid.txt
head -n 1600 $data/adv_preprocessed_large.txt | tail -n 800 > $data/adv_large/test.txt
tail -n 8335 $data/adv_preprocessed_large.txt > $data/adv_large/train.txt
