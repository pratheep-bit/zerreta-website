#!/usr/bin/env python3

import re
import os

def beautify_html(input_file, output_file):
    """Format HTML file for better readability with proper indentation"""
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Break content into lines for processing
    lines = content.replace('><', '>\n<').split('\n')
    
    # Format HTML with proper indentation
    indent_level = 0
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Decrease indent for closing tags
        closing_tag = re.match(r'^</.*?>', line)
        if closing_tag and indent_level > 0:
            indent_level -= 1
        
        # Special handling for self-closing tags or tags without content
        if '</head>' in line and '<head>' in line:
            # Special case for collapsed head tag
            head_open, head_close = line.split('</head>')
            formatted_lines.append('    ' * indent_level + head_open + '</head>')
            continue
            
        # Add the current line with proper indentation
        formatted_lines.append('    ' * indent_level + line)
        
        # Increase indent after opening tags, but not for self-closing tags
        if re.match(r'^<[^/!][^>]*>$', line) and not re.search(r'/>$', line) and not re.search(r'^<(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\b', line, re.IGNORECASE):
            indent_level += 1
    
    # Add HTML comments for structure
    formatted_content = '<!-- START OF FORMATTED HTML -->\n'
    formatted_content += '\n'.join(formatted_lines)
    formatted_content += '\n<!-- END OF FORMATTED HTML -->'
    
    # Write the beautified HTML to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(formatted_content)
    
    print(f"Beautification complete. Written to {output_file}")

if __name__ == "__main__":
    # Ensure output directory exists
    os.makedirs("formatted_files", exist_ok=True)
    
    # Beautify the HTML
    beautify_html("formatted_files/Magic_UI_Clean.html", 
                  "formatted_files/Magic_UI_Beautiful.html") 