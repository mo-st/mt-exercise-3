# Readme
link to repo: https://github.com/mo-st/mt-exercise-3

# Changes made
I've decided to use a vocab size of 8000 instead of just 5000 because my data vocabulary has about that size and the model generates a lot of `<unk>` tags when training with just 5k, which is no fun. Also training with a total line count of nearly 10k didn't take more than 10 minutes so I thought I could up the vocab without causing any problems. I increased both the number of hidden units per layer and the embeddingsize to 300. As not to change any of the scripts I duplicated each and sufixed them with `_adv.sh`
# Thoughts on dropout
The overall best dropout rate seems to be somewhere around 0.4. Training and test perplexity more or less correspond and both suggest a minimum at 0.4-0.6, however validation perplexity diverges a lot from that. It seems the lower the dropout the better the validation score. It could be that this has to do with the distance of the train and validation text samples, test and training being close neighbours. As the text are scripts of a cartoon, the overlap across different episodes might not be as high and vary a lot depending on that episodes theme. Because there was no randomization involved in the splitting the split was linear. Although I tried to account for this by ordering the episodes not by release, there might still be a strong influence.
# Dropout tables

|training perplexity|    0.0 |    0.2 |    0.4 |    0.6 |    0.8 |
|---:|-------:|-------:|-------:|-------:|-------:|
|  1 | 234.79 | 254.45 | 271.71 | 273.99 | 285.32 |
|  2 | 150.37 | 142.28 | 150.5  | 158.72 | 179.62 |
|  3 | 121.12 | 121.85 | 125.75 | 125.63 | 148.47 |
|  4 | 114.7  | 113.63 | 111.88 | 116.25 | 135.61 |
|  5 | 116.45 | 110.45 | 110.24 | 111.75 | 129.99 |
|  6 | 111.93 | 114.75 | 110.3  | 109.7  | 126.12 |
|  7 | 116.16 | 110.61 | 104.75 | 110.12 | 124.07 |
|  8 | 117.01 | 109.45 | 104.71 | 104.44 | 121.71 |
|  9 | 117.37 | 109.97 | 105.79 | 104.56 | 121.17 |
| 10 | 117.34 | 109.76 | 104.95 | 104.18 | 120.1  |
| 11 | 117.31 | 109.65 | 105.09 | 104.55 | 120.2  |
| 12 | 117.31 | 109.64 | 105.08 | 104.6  | 116.83 |
| 13 | 117.31 | 109.64 | 105.07 | 104.58 | 116.65 |
| 14 | 117.31 | 109.64 | 105.07 | 104.58 | 116.09 |
| 15 | 117.31 | 109.64 | 105.07 | 104.58 | 115.69 |
| 16 | 117.31 | 109.64 | 105.07 | 104.58 | 116.21 |
| 17 | 117.31 | 109.64 | 105.07 | 104.58 | 116    |
| 18 | 117.31 | 109.64 | 105.07 | 104.58 | 116.2  |
| 19 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 20 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 21 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 22 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 23 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 24 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 25 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 26 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 27 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 28 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 29 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 30 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 31 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 32 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 33 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 34 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 35 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 36 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 37 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 38 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 39 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |
| 40 | 117.31 | 109.64 | 105.07 | 104.58 | 116.23 |

|Validation perplexity|    0.0 |    0.2 |    0.4 |    0.6 |    0.8 |
|---:|-------:|-------:|-------:|-------:|-------:|
|  1 | 658.15 | 672.64 | 667.63 | 663.81 | 730.21 |
|  2 | 146.78 | 158    | 160.06 | 177.08 | 214.34 |
|  3 |  82.76 |  88.76 |  95.11 | 108.61 | 152.69 |
|  4 |  61.21 |  66.62 |  74.12 |  87.1  | 129.72 |
|  5 |  49.26 |  54.76 |  62.4  |  74.96 | 115.94 |
|  6 |  35.29 |  46.81 |  54.84 |  67.68 | 107.06 |
|  7 |  30.82 |  35.64 |  44.73 |  62.32 | 101.33 |
|  8 |  27.31 |  31.99 |  41.13 |  54.44 |  96.67 |
|  9 |  26.12 |  30.81 |  38.99 |  51.33 |  92.67 |
| 10 |  25.74 |  30    |  37.05 |  49.44 |  89.88 |
| 11 |  25.61 |  29.59 |  36.02 |  48.49 |  87.44 |
| 12 |  25.58 |  29.6  |  35.84 |  47.58 |  81.62 |
| 13 |  25.57 |  29.5  |  35.85 |  47.65 |  78.08 |
| 14 |  25.57 |  29.64 |  35.76 |  47.83 |  76.15 |
| 15 |  25.57 |  29.54 |  35.51 |  47.32 |  74.51 |
| 16 |  25.57 |  29.64 |  35.76 |  47.53 |  73.28 |
| 17 |  25.57 |  29.65 |  35.77 |  47.52 |  72.14 |
| 18 |  25.57 |  29.63 |  35.84 |  47.58 |  71.11 |
| 19 |  25.57 |  29.6  |  35.73 |  47.57 |  70.98 |
| 20 |  25.57 |  29.54 |  35.76 |  47.51 |  71.33 |
| 21 |  25.57 |  29.64 |  35.71 |  47.67 |  70.9  |
| 22 |  25.57 |  29.52 |  35.76 |  47.49 |  70.95 |
| 23 |  25.57 |  29.57 |  35.7  |  47.38 |  71.07 |
| 24 |  25.57 |  29.65 |  35.76 |  47.39 |  70.75 |
| 25 |  25.57 |  29.55 |  35.74 |  47.61 |  71.09 |
| 26 |  25.57 |  29.62 |  35.66 |  47.28 |  70.99 |
| 27 |  25.57 |  29.56 |  35.59 |  47.46 |  70.63 |
| 28 |  25.57 |  29.6  |  35.66 |  47.32 |  70.73 |
| 29 |  25.57 |  29.6  |  35.76 |  47.5  |  70.93 |
| 30 |  25.57 |  29.57 |  35.81 |  47.34 |  71    |
| 31 |  25.57 |  29.59 |  35.63 |  47.21 |  70.7  |
| 32 |  25.57 |  29.55 |  35.69 |  47.54 |  70.83 |
| 33 |  25.57 |  29.68 |  35.79 |  47.3  |  71.06 |
| 34 |  25.57 |  29.53 |  35.77 |  47.46 |  70.69 |
| 35 |  25.57 |  29.53 |  35.82 |  47.37 |  71.4  |
| 36 |  25.57 |  29.55 |  35.7  |  47.38 |  70.89 |
| 37 |  25.57 |  29.55 |  35.74 |  47.45 |  71.13 |
| 38 |  25.57 |  29.58 |  35.77 |  47.65 |  70.94 |
| 39 |  25.57 |  29.54 |  35.65 |  47.41 |  71.18 |
| 40 |  25.57 |  29.6  |  35.84 |  47.43 |  70.79 |

|test perplexity|    0.0 |    0.2 |    0.4 |    0.6 |    0.8 |
|---:|-------:|-------:|-------:|-------:|-------:|
|result| 81.30 | 78.25 | 75.59 | 76.38 | 86.72 |
# Thoughts on results
The model performs reasonably well I think considering the small size of the training data. It didn't quite figure out how a transcript works, for example not all opening brackets have closing ones, dialog isn't always differentiated from metadescription etc. But all in all the themes are present, the overall tone of the show is easily recognized and the word ordering is also kind of right about 50% of the time. I wouldn't go so far as calling it "fluent" but it isn't just mumbo jumbo either.

# Steps to recreate
Assuming you have cloned the repo, activated the venv. The splitting and preprocessing isn't necessary because the needed files are already included in the repo but the scripts I used are included anyway in case you are interested.
## Running
1. run `./scripts/train_adv.sh` 
(the current dropout setting is 0.4 and produces a model called `model_large300_dp04` to make the difference between models clear)
2. run `./scripts/generate_adv.sh`
(Used the output of step 1 to produce a sample called `sample_large30004`)
## Preprocessing
In case you want to repeat each step, these were taken and each intermediate result is included in the repo so you can have a look without running.
1. Take `adventure_time_transcripts.txt` and preprocess it using the script `preproccess_raw.py` -> `adv_cleaned.txt`
2. apply `preprocess.py` with vocab size 8000 -> `adv_preprocessed_large.txt`.
In case you are wondering how different the model performs with the smaller vocab I included that as well: `adv_preprocessed.txt`
3. split the data using `split_adv_large.sh` -> dirctory `/data/adv_large/`
## Additional files
`extract_perplexity.py` was used to generate the charts, tables and extract the needed data from the commandline output during training.
