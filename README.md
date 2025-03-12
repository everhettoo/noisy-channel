# Noisy-Channel
This package implements noisy-channel for estimating correct word c given input w. \
`c = argmax P(w|c)P(c)`

## Acknowledgement
The code was adopted from Peter Norvig web: https://norvig.com

## How to consume the package?
### Install
`pip install git+https://github.com/everhettoo/noisy-channel.git`

### Class: Probability Distributor
This class reads a TSV corpus and calculates the word probability. The corpus should be in the following format:
```
artist	67421654
outside	67415846
```
To initialize the class:
```python
p = ProbaDistributor(datafile('data.tsv'))
```
To calculate the probability of the word:
```python
p('apple')
```
`output: 6.34494 x 10^-05`
### Class: Noisy Channel
```python
p_lang = ProbaDistributor(datafile('data/count_1w.tsv'))
p_error = ProbaDistributor(datafile('data/count_1edit.tsv'))
channel = ChannelV1(lang_model=p_lang,
                        error_model=p_error,
                        spell_error=(1. / 20.),
                        alphabet='abcdefghijklmnopqrstuvwxyz')

channel.correct('oraneg')
```
`output: orange`
## Unit Test
Unit test can be found in `/tests` folder for understanding the calculation in detail.
