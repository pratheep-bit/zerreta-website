#!/usr/bin/env python3

import re
import os

def convert_mhtml_to_html(input_file, output_file):
    """Convert MHTML file to clean HTML format"""
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Extract the HTML part from MHTML
    html_match = re.search(r'Content-Type: text/html.*?<!DOCTYPE html>(.*?)(?:------MultipartBoundary|\Z)', 
                          content, re.DOTALL)
    
    if not html_match:
        print("Could not extract HTML content")
        return False
    
    html_content = "<!DOCTYPE html>" + html_match.group(1)
    
    # Clean up the quoted-printable encoding
    # Replace =XX with actual characters
    def replace_quoted_printable(match):
        hex_code = match.group(1)
        return chr(int(hex_code, 16))
    
    html_content = re.sub(r'=([0-9A-F]{2})', replace_quoted_printable, html_content)
    
    # Fix linebreaks in attributes
    html_content = re.sub(r'\n\s*([a-z-]+)=', r' \1=', html_content)
    
    # Format HTML for readability
    # This is a simple approach - a full formatter would be much more complex
    indent_level = 0
    formatted_lines = []
    
    for line in html_content.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        # Decrease indent for closing tags
        if re.match(r'</[^>]+>', line) and indent_level > 0:
            indent_level -= 1
            
        # Add current line with proper indentation
        formatted_lines.append('    ' * indent_level + line)
        
        # Increase indent after opening tags (not self-closing)
        if re.search(r'<[^/][^>]*>(?!.*</)', line) and not re.search(r'/>|<(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\b', line, re.IGNORECASE):
            indent_level += 1
    
    formatted_html = '\n'.join(formatted_lines)
    
    # Write the formatted HTML to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_html)
    
    print(f"Conversion complete. Written to {output_file}")
    return True

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    os.makedirs("formatted_files", exist_ok=True)
    
    # Convert MHTML to HTML
    convert_mhtml_to_html("Magic UI.mhtml", "formatted_files/Magic_UI_Clean.html")