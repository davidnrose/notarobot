import pandas as pd
import time
import streamlit as st

# read lines of the poem
lines = pd.read_csv("words.txt", header=None, names=["text"])

# randomly sample the lines, without replacement
lines = lines.sample(n=len(lines), replace=False)

# convert lines into list
lines = list(lines["text"])

# split those with a newline to keep order where relevant
lines_all = list()

for l in lines:
    line_split = l.split(r"\n")
    lines_all.extend(line_split)

# create function for initialising generator and streaming text
def stream(verse):
    for n in verse:
        yield n
        time.sleep(0.03)

# set page width using columns
col1, col2, col3 = st.columns([0.2, 0.6, 0.2])

with col2:
    # display the title
    st.header("CAPTCHA")

    # iterate over the lines and stream the text
    for l in lines_all:
        st.write_stream(stream(l))

    time.sleep(0.5)