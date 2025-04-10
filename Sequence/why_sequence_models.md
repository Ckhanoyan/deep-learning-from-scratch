# Why Sequence Models?

Sequence models are essential in deep learning because they enable the processing and generation of data where the order and context of elements in a sequence matter. These models are applied to tasks such as text processing, speech recognition, time-series analysis, and video processing. 

For instance, in natural language processing, sequence models are used to understand relationships between words in a sentence, allowing applications such as language translation, sentiment analysis, and text generation. By leveraging methods like one-hot encoding, as demonstrated in examples like encoding words in "Harry Potter," sequence models such as Recurrent Neural Networks (RNNs), Long Short-Term Memory (LSTM) networks, and Transformers can capture dependencies across time or positions to learn meaningful patterns. 

### Example: One-Hot Encoding

One-hot encoding represents each word in a sentence as a unique binary vector where only one element is `1` (indicating the word's index in the vocabulary), and all other elements are `0`. Here's an example for the sentence:  
*"Harry Potter and Chris Khanoyan invented a new spell."*

#### Steps:
1. **Vocabulary Creation**: List all unique words in the sentence.  
   Vocabulary: `['Harry', 'Potter', 'and', 'Chris', 'Khanoyan', 'invented', 'a', 'new', 'spell']`

2. **One-Hot Encoding**: Each word is represented as a vector of length 9 (size of vocabulary), with a `1` at the index corresponding to the word in the vocabulary.

#### One-Hot Encoding Table:
| Word       | One-Hot Vector                     |
|------------|------------------------------------|
| Harry      | `[1, 0, 0, 0, 0, 0, 0, 0, 0]`     |
| Potter     | `[0, 1, 0, 0, 0, 0, 0, 0, 0]`     |
| and        | `[0, 0, 1, 0, 0, 0, 0, 0, 0]`     |
| Chris      | `[0, 0, 0, 1, 0, 0, 0, 0, 0]`     |
| Khanoyan   | `[0, 0, 0, 0, 1, 0, 0, 0, 0]`     |
| invented   | `[0, 0, 0, 0, 0, 1, 0, 0, 0]`     |
| a          | `[0, 0, 0, 0, 0, 0, 1, 0, 0]`     |
| new        | `[0, 0, 0, 0, 0, 0, 0, 1, 0]`     |
| spell      | `[0, 0, 0, 0, 0, 0, 0, 0, 1]`     |

### Dictionaries and Vocabulary Sizes

In natural language processing, a **dictionary** (or vocabulary) is a mapping of unique words to indices. This allows the conversion of words into numerical representations that models can process.

Small Vocabulary (e.g., <10,000 words):
Small vocabularies are often used when dealing with constrained datasets or specific domains, such as legal documents or medical texts. They work well when the language used is limited, avoiding the need to handle rare or out-of-vocabulary words.

Large Vocabulary (e.g., >50,000 words):
Larger vocabularies are necessary for more general datasets like books, websites, or multilingual corpora. They improve the model's ability to capture nuances and rare words but come with increased computational cost, slower training, and larger memory usage.
