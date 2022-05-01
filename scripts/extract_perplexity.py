#! usr/bin/env/ python3
# -*- coding: utf-8 -*-
# author: moritz.steiner2

import argparse
import re
import pandas as pd
import matplotlib.pyplot as plt


def cli_extract():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="inputfile")
    parser.add_argument("-o", help="outfile")
    arguments = parser.parse_args()
    return arguments


def cli_aggregate():
    parser = argparse.ArgumentParser()
    parser.add_argument("oo")
    parser.add_argument("ot")
    parser.add_argument("of")
    parser.add_argument("os")
    parser.add_argument("oe")
    arguments = parser.parse_args()
    return arguments


def extract(input_f, output):
    valid_p = list()
    training_p = list()
    with open(input_f, "r", encoding="utf-8") as infile:
        for line in infile:
            if re.search("\| ppl    \d\d?\d?\.\d\d", line):
                valid_p.append(re.search("\| ppl    \d\d?\d?\.\d\d", line).group().lstrip("| ppl    "))
            elif re.search("\| ppl   \d\d?\d?\.\d\d", line):
                valid_p.append(re.search("\| ppl   \d\d?\d?\.\d\d", line).group().lstrip("| ppl   "))
            elif re.search("valid ppl   \d\d?\d?\.\d\d", line):
                training_p.append(re.search("valid ppl   \d\d?\d?\.\d\d", line).group().lstrip("valid ppl   "))
            elif re.search("valid ppl    \d\d?\d?\.\d\d", line):
                training_p.append(re.search("valid ppl    \d\d?\d?\.\d\d", line).group().lstrip("valid ppl    "))
    with open(output, "w", encoding="utf-8") as outfile:
        for i, (v, t) in enumerate(zip(valid_p, training_p)):
            outfile.write(f"epoch {i+1}\t{v}\t{t}\n")


def aggregate(in00, in02, in04, in06, in08, perp: int):
    out = {"0.0": [], "0.2": [], "0.4": [], "0.6": [], "0.8": []}
    for line in in00:
        out["0.0"].append(float(line.split("\t")[perp].rstrip("\n")))
    for line in in02:
        out["0.2"].append(float(line.split("\t")[perp].rstrip("\n")))
    for line in in04:
        out["0.4"].append(float(line.split("\t")[perp].rstrip("\n")))
    for line in in06:
        out["0.6"].append(float(line.split("\t")[perp].rstrip("\n")))
    for line in in08:
        out["0.8"].append(float(line.split("\t")[perp].rstrip("\n")))
    return out


def plot(perplex: dict[list]):
    df = pd.DataFrame({"0.0": perplex["0.0"], "0.2": perplex["0.2"], "0.4": perplex["0.4"],
                       "0.6": perplex["0.6"], "0.8": perplex["0.8"]}, index=[i+1 for i in range(40)])
    lines = df.plot.line()
    plt.show()


if __name__ == "__main__":
    """This script serves a double purpose: 
    1. EXTRACT the perplexity scores form cli output of each training procedure in textfile format and write to tsv
    2. AGGREGATE all .tsv into python data and plot it"""
    # Purpose 1:
    # Run like this: python3 scripts/extract_perplexity.py -i log_04.txt -o dp04.tsv
    # args = cli_extract()
    # extract(args.i, args.o)
    # Purpose 2
    # Run like this: python3 scripts/extract_perplexity.py dp00.tsv dp02.tsv dp04.tsv dp06.tsv dp08.tsv
    args = cli_aggregate()
    with open(args.oo, "r") as inf00, open(args.ot, "r") as inf02, open(args.of, "r") as inf04,\
            open(args.os, "r") as inf06, open(args.oe, "r") as inf08:
        # these are single use generators, so I had to run the script two times, commenting out the plot I didn't want
        d_val = aggregate(inf00, inf02, inf04, inf06, inf08, 1)
        plot(d_val)
        # d_tra = aggregate(inf00, inf02, inf04, inf06, inf08, 2)
        # plot(d_tra)

