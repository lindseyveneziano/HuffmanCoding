# Huffman Coding Implementation

## Overview

This project implements the Huffman coding algorithm in Python, which is used for lossless data compression. Huffman coding is a popular algorithm that assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters, thereby reducing the overall size of the data.

## Features

- **Text Compression**: Compresses text files using Huffman coding.
- **Text Decompression**: Decompresses the encoded files back to their original text form.
- **Binary Tree Structure**: Utilizes a binary tree for efficient encoding and decoding of characters.
- **Performance Analysis**: Provides performance metrics comparing compression ratios and execution times with other algorithms.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/lindseyveneziano/huffman-coding.git
   cd huffman-coding

2. **Install dependencies:**
Ensure you have Python installed. Then, you can create a virtual environment and install necessary libraries using:

```sh
python -m venv venv

source venv/bin/activate  (On Windows use `venv\Scripts\activate`)

pip install -r requirements.txt
```

## Usage
1. Encoding a Text File:
`python main.py encode <input_file.txt> <output_file.bin>`

2. Decoding an Encoded File:
   `python main.py decode <output_file.bin> <decoded_file.txt>`


## Project Structure

- `main.py`: The main script containing the implementation of the Huffman coding algorithm.
- `encoded_file*.txt`: Sample text files used for encoding.
- `encoded_file*.txt.bin`: Encoded binary files.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Project documentation.

## Implementation Details

1. **HuffmanNode Class**:
   - Represents a node in the Huffman tree, storing characters and their frequencies.

2. **Frequency Calculation**:
   - Calculates the frequency of each character in the input text.

3. **Tree Construction**:
   - Builds the Huffman tree using a priority queue to merge nodes based on their frequencies.

4. **Code Assignment**:
   - Assigns binary codes to characters by traversing the Huffman tree.

5. **Encoding and Decoding**:
   - Encodes the text using the assigned Huffman codes.
   - Decodes the binary file back to its original text using the Huffman tree.
  
## Author
Lindsey Veneziano

[LinkedIn](http://www.linkedin.com/in/lindsey-veneziano)
