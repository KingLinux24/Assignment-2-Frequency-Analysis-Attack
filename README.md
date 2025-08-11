# Cryptography Labs
This repository contains my practical implementations and exercises in cryptography.

# Assignment 2: Frequency Analysis Attack
This assignment implements a Frequency Analysis Attack to cryptanalyze a Caesar cipher ciphertext.

Features:
Frequency Counting: Calculates the frequency of letters in the given ciphertext.

Key Estimation: Estimates the most likely key by comparing the most frequent ciphertext letter to 'E' (the most frequent letter in English).

Decryption: Decrypts the ciphertext using the estimated key.

Assumptions: Relies on the standard English letter frequency distribution ("ETAOINSHRDLCUMWFGYPBVKJXQZ").

How to Run:
1. Clone this repository:

`Bash`

`git clone https://github.com/YourUsername/Cryptography-Labs.git`<br>
`cd Cryptography-Labs/Assignment_2_Frequency_Analysis # Adjust path if different`


2. Execute the Python script:

`Bash`

`python frequency_analysis.py`


The script will directly process the pre-defined ciphertext and output the estimated key and decrypted text.
