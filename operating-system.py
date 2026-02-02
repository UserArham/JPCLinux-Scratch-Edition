os_list = [
    ("Windows 3.1", "https://scratch.mit.edu/projects/3242775/embed"),
    ("Windows 95", "https://scratch.mit.edu/projects/564499318/embed"),
    ("Windows 98", "https://scratch.mit.edu/projects/3241241/embed"),
    ("Windows 2000", "https://scratch.mit.edu/projects/384765648/embed"),
    ("Windows XP", "https://scratch.mit.edu/projects/1273557120/embed"),
    ("Windows Vista", "https://scratch.mit.edu/projects/1273585033/embed"),
    ("Windows 7", "https://scratch.mit.edu/projects/1273566678/embed"),
    ("Windows 8 (Old)", "https://scratch.mit.edu/projects/1273827404/embed"),
    ("Windows 10", "https://scratch.mit.edu/projects/1273563839/embed"),
    ("Windows 11", "https://scratch.mit.edu/projects/554147954/embed")
]

html = '<ul id="osList">\n'
for os_name, _ in os_list:
    html += f'  <li>{os_name}</li>\n'
html += '</ul>\n\n'

for os_name, link in os_list:
    html += f'<div class="iframe-box">\n'
    html += f'  <h2>{os_name}</h2>\n'
    html += f'  <iframe src="{link}" allowtransparency="true" width="485" height="402" frameborder="0" scrolling="no" allowfullscreen></iframe>\n'
    html += f'</div>\n\n'

with open("index.html", "w") as f:
    f.write(html)

print("HTML gallery generated successfully!")
