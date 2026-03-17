import os

def extract(input_file_path, output_file_path="demo.jsonl"):
    total_lines = 0
    with open(input_file_path, 'r', encoding='utf-8') as f:
        for _ in f:
            total_lines += 1
    lines_to_extract = min(1, total_lines)    
    with open(input_file_path, 'r', encoding='utf-8') as infile, \
        open(output_file_path, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile):
            if i >= 1:
                break
            outfile.write(line)

if __name__ == "__main__":
    INPUT_JSONL_FILE = "browsecomp_plus_decrypted.jsonl"
    OUTPUT_DEMO_FILE = "demo.jsonl"
    extract(INPUT_JSONL_FILE, OUTPUT_DEMO_FILE)