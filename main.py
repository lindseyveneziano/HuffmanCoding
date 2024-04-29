import heapq
import os

class HuffmanNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def calculate_character_frequencies(text):
    frequency_dict = {}
    for char in text:
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict

def build_huffman_tree(char_frequencies):
    priority_queue = [HuffmanNode(char, freq) for char, freq in char_frequencies.items()]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left.frequency + right.frequency)
        merged_node.left_child = left
        merged_node.right_child = right
        heapq.heappush(priority_queue, merged_node)
    return priority_queue[0]

def assign_huffman_codes(root_node, prefix="", code_map={}):
    if root_node:
        if root_node.character is not None:
            code_map[root_node.character] = prefix
        assign_huffman_codes(root_node.left_child, prefix + "0", code_map)
        assign_huffman_codes(root_node.right_child, prefix + "1", code_map)
    return code_map

def encode_text_using_huffman(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

def decode_text(encoded_text, huffman_tree):
    decoded_output = []
    node = huffman_tree
    for symbol in encoded_text:
        node = node.left_child if symbol == '0' else node.right_child
        if node.character:
            decoded_output.append(node.character)
            node = huffman_tree
    return ''.join(decoded_output)

def encode_to_file(input_text, huffman_codes, output_file_name):
    encoded_text = encode_text_using_huffman(input_text, huffman_codes)
    # Padding the encoded text to make its length a multiple of 8
    padding = 8 - len(encoded_text) % 8
    encoded_text += '0' * padding
    # Adding information about the padding to the encoded text
    padded_info = "{0:08b}".format(padding)
    encoded_text = padded_info + encoded_text

    with open(output_file_name, 'wb') as output_file:
        for i in range(0, len(encoded_text), 8):
            byte = encoded_text[i:i+8]
            output_file.write(bytes([int(byte, 2)]))
    return encoded_text

def decode_from_file(encoded_file_name, huffman_tree):
    with open(encoded_file_name, 'rb') as encoded_file:
        padded_info = encoded_file.read(1)
        padding = int.from_bytes(padded_info, byteorder='big')
        # Now read the rest of the file
        encoded_text = ''
        byte = encoded_file.read(1)
        while byte:
            encoded_text += f'{int.from_bytes(byte, byteorder="big"):08b}'
            byte = encoded_file.read(1)
        # Remove the padding
        encoded_text = encoded_text[:-padding]

    return decode_text(encoded_text, huffman_tree)

def process_files(file_list):
    for input_file_name in file_list:
        if not os.path.exists(input_file_name):
            print(f"File {input_file_name} does not exist, skipping.")
            continue

        print(f"\nProcessing {input_file_name}...")
        with open(input_file_name, 'r') as file:
            input_text = file.read()

        char_frequencies = calculate_character_frequencies(input_text)
        huffman_tree = build_huffman_tree(char_frequencies)
        huffman_codes = assign_huffman_codes(huffman_tree)

        encoded_file_name = f'encoded_{input_file_name}.bin'  # Change the extension to .bin
        decoded_file_name = f'decoded_{input_file_name}'

        encoded_text = encode_to_file(input_text, huffman_codes, encoded_file_name)
        decoded_text = decode_from_file(encoded_file_name, huffman_tree)

        print("Character Frequencies:")
        for char, freq in char_frequencies.items():
            print(f"{char}: {freq}")

        print("\nHuffman Codes:")
        for char, code in huffman_codes.items():
            print(f"{char}: {code}")

        print("\nEncoded Text:")
        print(encoded_text)

        print("\nDecoded Text (Verification):")
        print(decoded_text)

        original_size_bytes = os.path.getsize(input_file_name)
        encoded_size_bytes = os.path.getsize(encoded_file_name)

        print(f"Original File Size: {original_size_bytes} bytes")
        print(f"Encoded File Size: {encoded_size_bytes} bytes")

        compression_ratio = (1 - (encoded_size_bytes / original_size_bytes)) * 100
        print(f"Compression Ratio for {input_file_name}: {compression_ratio:.2f}%")

def main():
    # List of filenames to process
    file_list = [f"file{i}.txt" for i in range(1, 21)]
    process_files(file_list)

if __name__ == "__main__":
    main()
