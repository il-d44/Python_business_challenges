import json
import os

def extract_code_cells(ipynb_path, py_path):
    # Read the notebook file
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Extract code cells
    code_cells = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            code_cells.append(''.join(cell['source']))
    
    # Write to a Python file
    with open(py_path, 'w', encoding='utf-8') as f:
        for cell in code_cells:
            f.write(cell + '\n\n')

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

exercise_extracted_file_names = {
    "../0-Python_practices__basic.ipynb": "../extracted/basic_extracted.py",
    "../1-Python_practices__medium.ipynb": "../extracted/medium_extracted.py",
    "../2-Python_practices__advanced.ipynb": "../extracted/advanced_extracted.py",
}

for ipynb_path, py_path in exercise_extracted_file_names.items():
    extract_code_cells(os.path.join(current_dir, ipynb_path), os.path.join(current_dir, py_path))
