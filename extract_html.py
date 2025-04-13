#!/usr/bin/env python3

def extract_html_from_mhtml(input_file, output_file):
    """Extract and clean the HTML content from an MHTML file"""
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.readlines()
    
    # Find where the HTML content starts
    start_line = 0
    for i, line in enumerate(content):
        if '<!DOCTYPE html>' in line or '<html' in line:
            start_line = i
            break
    
    # Extract the HTML part
    html_content = content[start_line:]
    
    # Clean up the content
    cleaned_content = []
    for line in html_content:
        # Replace =3D with =
        line = line.replace('=3D', '=')
        # Replace other common quoted-printable encodings
        line = line.replace('=20', ' ')
        line = line.replace('=22', '"')
        line = line.replace('=27', "'")
        line = line.replace('=2F', '/')
        line = line.replace('=3A', ':')
        line = line.replace('=3B', ';')
        line = line.replace('=3C', '<')
        line = line.replace('=3E', '>')
        # Remove line breaks that are part of quoted-printable encoding
        if line.endswith('=\n'):
            line = line[:-2]
        # Add to cleaned content
        cleaned_content.append(line)
    
    # Join and write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(cleaned_content))
    
    print(f"Extraction complete. Written to {output_file}")

if __name__ == "__main__":
    extract_html_from_mhtml("Magic UI.mhtml", "formatted_files/Magic_UI_Clean.html") 