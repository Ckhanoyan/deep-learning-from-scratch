# Self Attention Intuition 

It is a crucial mechanism in modern deep learning models that allows relevant parts of the sequence for each word or token. We have Query, Key, and Value (Q, K, V) that three vectors are derived:
* Q: represents the word in focus
* K: represents each word as a reference to match against
* V: represents the actual information we want to transfor from each word in the sequence

The core idea behind self-attention is to compute how much focus each word should have on every other word. 
