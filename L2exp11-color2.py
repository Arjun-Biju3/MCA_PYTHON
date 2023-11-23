# Read color names from the user as a comma-separated string
color_names = input("Enter color names separated by commas: ")

# Split the input string into a list of color names
colors = [color.strip() for color in color_names.split(',')]

# Check if there are any colors in the list
if len(colors) > 0:
    # Display the first and last colors
    print("First color:", colors[0])
    print("Last color:", colors[-1])
else:
    print("No colors entered.")
