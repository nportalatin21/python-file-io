import re
import sys

def find_word_occurrences(file_path, pattern):

    occurrences = []
    
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Skip the added text at the beginning of the file
    start_line = 0
    while not lines[start_line].startswith("Produced by"):
        start_line += 1
    lines = lines[start_line + 1:]

    # Skip the added text at the end of the file
    end_line = len(lines) - 1
    while not lines[end_line].startswith("End of the Project Gutenberg"):
        end_line -= 1
    lines = lines[:end_line]
    
    for line_num, line in enumerate(lines, start=1):
        matches = re.findall(pattern, line, re.IGNORECASE)
        for match in matches:
            occurrences.append((line_num, match))
    
    return occurrences

def write_occurrences_to_file(file_path, occurrences):
    """
    Write the word occurrences to a file.

    Args:
        file_path (str): Path to the output file.
        occurrences (list): A list of tuples containing the line number and matched word.
    """
    with open(file_path, 'w') as output_file:
        for line_num, word in occurrences:
            output_file.write(f"{line_num}\t{word}\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <pattern>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    word_pattern = sys.argv[2]
    output_file_path = 'output.txt'
    
    occurrences = find_word_occurrences(input_file_path, word_pattern)
    write_occurrences_to_file(output_file_path, occurrences)
