import webbrowser
import os

# Read the .txt file
with open('output.txt', 'r') as f:
    data = f.readlines()

# print(data)

# Start the HTML output
html_output = '<pre>\n'

# Add the data
html_output += ''.join(data)

# End the HTML output
html_output += '</pre>'

# Write the HTML output to a file
with open('output.html', 'w') as f:
    f.write(html_output)

# Open the HTML file in the default web browser
webbrowser.open('file://' + os.path.realpath('output.html'))
