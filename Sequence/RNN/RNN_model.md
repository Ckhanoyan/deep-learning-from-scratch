# RNN Model

## Understanding a Simple RNN Model with a Sentence Example

A Recurrent Neural Network (RNN) processes sequential data by maintaining a hidden state that captures information about previous elements in the sequence. Let's use the sentence: **"My dog likes to wake me up at 4:00 AM every day."** to illustrate how a simple RNN works.

### Step-by-Step Explanation

1. **Input Representation**:  
   Each word in the sentence is converted into a vector representation, typically using embeddings (e.g., Word2Vec or GloVe). For example:
   - "My" → [0.1, 0.3, 0.5, ...]
   - "dog" → [0.2, 0.4, 0.6, ...]

2. **Sequential Processing**:  
   The RNN processes one word at a time. At each step, it updates its hidden state based on the current word and the previous hidden state:

   **Hidden State Update**:  
   \( h_t = f(W_x \cdot x_t + W_h \cdot h_{t-1} + b) \)  
   Where:
   - \( h_t \): Current hidden state
   - \( x_t \): Current word's input vector
   - \( h_{t-1} \): Previous hidden state
   - \( W_x, W_h, b \): Learnable weights and biases
   - \( f \): Activation function (e.g., tanh or ReLU)

   For instance:
   - At \( t = 1 \), the word "My" is processed, and the initial hidden state (\( h_0 \)) is updated.
   - At \( t = 2 \), the word "dog" is processed using the updated hidden state from \( t = 1 \), and so on.

3. **Capturing Context**:  
   The hidden state at each step encodes information about the current word and the context provided by previous words. For example:
   - After processing "My dog likes", the hidden state might represent the idea that the subject (dog) "likes" something.

4. **Output**:  
   Depending on the task, the RNN can produce an output at each step or after processing the entire sequence. For example:
   - In a language modeling task, the RNN might predict the next word at each step.
   - In a sentiment analysis task, the RNN might produce a single output after processing the entire sentence.

---

## Incorporating EOS (End of Sentence)

The EOS (End of Sentence) token is a special token added to the vocabulary to indicate the end of a sequence or sentence. It helps the model understand where a sentence ends, which is crucial for tasks involving variable-length sequences.

### Example with EOS:
Let's say we want the RNN to process the sentence:  
**"My dog likes to wake me up at 4:00 AM every day."**

We can represent this as a sequence of tokens:

["My", "dog", "likes", "to", "wake", "me", "up", "at", "4:00", "AM", "every", "day", "EOS"]


The **EOS** token is appended to mark the end of the sentence.

---

## Example with \( y \) (Output)

Consider a language modeling task where the model predicts the next word in the sequence. For the input sequence:

x = ["My", "dog", "likes", "to", "wake", "me", "up", "at", "4:00", "AM", "every", "day"]

The target output sequence \( y \) would be:

y = ["dog", "likes", "to", "wake", "me", "up", "at", "4:00", "AM", "every", "day", "EOS"]


Here, each word in \( x \) maps to the next word in \( y \), and the last word in \( y \) is the EOS token.

---

## How EOS Works in RNN:

1. At each timestep, the RNN takes a word from \( x \) and predicts the next word in \( y \).
2. When the model encounters the EOS token in \( y \), it learns to stop generating further output.

### Example Workflow:

- Input: "My" → Output: "dog"
- Input: "dog" → Output: "likes"
- ...
- Input: "day" → Output: "EOS"

This mechanism ensures that the model can handle sequences of varying lengths and knows when to stop processing or generating text.
