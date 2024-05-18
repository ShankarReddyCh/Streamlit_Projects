import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write('''
# DNA Nucleotide Web App

This app counts the nucleotide composition of query DNA!

***
''')


st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area(label='Sequence Input', value=sequence_input, height=200)


sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)
sequence

# horizontal line separator

st.write('''
***
''')

st.header('Input (DNA query)')

sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print Dictionary')

def DNA_nucleotide(sequence):
    d = dict([
        ('A',sequence.count('A')),
        ('C',sequence.count('C')),
        ('G',sequence.count('G')),
        ('T',sequence.count('T'))
    ])
    
    return d

X = DNA_nucleotide(sequence=sequence)

X

### 2. Print text
st.subheader('2. Print text')
st.write(f'There are {X['A']} adenine(A)')
st.write(f'There are {X['C']} cytosine(C)')
st.write(f'There are {X['G']} guanine(G)')
st.write(f'There are {X['T']} thymine(T)')

### 3. Display Dataframe
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0:'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='Count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)








