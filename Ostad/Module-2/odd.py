import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

# Read input
string = input().strip()
max_width = int(input().strip())

# Call function and print result
result = wrap(string, max_width)
print(result)
