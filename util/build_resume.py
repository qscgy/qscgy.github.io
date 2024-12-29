#!/usr/bin/env python
import shutil
import subprocess

input_file = "resume.md"
output_file = "resume.pdf"
css_file = "resume.css"
html_file = "resume.html"

command = ['pandoc', input_file, '-o', output_file, '--pdf-engine', 'weasyprint',
            '--css', css_file]
result = subprocess.run(command, capture_output=True, text=True)
if result.returncode == 0:
    print("Pandoc executed successfully")
else:
    print(f"Pandoc failed with error: {result.stderr}")
    
command = ['pandoc', input_file, '-o', html_file, '-t', 'html5',
            '--css', css_file]
result = subprocess.run(command, capture_output=True, text=True)
if result.returncode == 0:
    print("Pandoc executed successfully")
else:
    print(f"Pandoc failed with error: {result.stderr}")

with open(html_file) as f:
    lines = f.readlines()

with open(html_file, 'w') as f:
    f.writelines([
        "---\n",
        "title: Curriculum Vitae\n",
        "permalink: /cv/\n",
        "---\n",
        '<span class="resume">\n'
        ] + lines + ["</span>\n"])
    
shutil.move(html_file, '../_pages/resume.html')