#! /bin/bash

scripts=`dirname "$0"`
base=$(realpath $scripts/..)

models=$base/models
data=$base/data
tools=$base/tools


num_threads=8
device=""

SECONDS=0

(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python main.py --data $data/adv_large \
        --epochs 40 \
        --log-interval 100 \
        --emsize 300 --nhid 300 --dropout 0.4 --tied \
        --save $models/model_large300_dp04.pt
)

echo "time taken:"
echo "$SECONDS seconds"
