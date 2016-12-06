# WikiSummary

## Overview
WikiSummary gives command line users a way to read summaries of wikipedia articles in their command line. Whether you're a dev that just wants a reminder of what an invariant is or simply bored of browsing reddit and instead wants to read an indefinite amount of summaries of wikipedia articles.

## How to use

First, clone the repository, <br />
`git clone https://github.com/Mikerah/WikiSummary.git`

Second, change current working directory into the cloned repository <br />
`cd WikiSummary`

Third, download all the dependencies using pip <br />
`pip install -r requirements.txt`

Lastly, use python to use WikiSummary <br />
1. `python wiki_summary.py -r Beyonce` : To read a specific wikipedia article <br />
2. `python wiki_summary.py -R 5`: To read 5 random wikipedia articles <br />
3. `python wiki_summary.py -rf`: To read an indefinite amount of random wikipedia articles until the user types stop <br />
4. `python wiki_summary.py -h`: For help 

![Alt text](docs/sample_output.gif?raw=true)

## Requirements
Have python 3.5 installed, along with pip.

## How to contribute
There are a lot of bugs in this simple program and a lot of improvements can be made. You can help me submitting a pull request and reporting issues.
