# Read the two lists
color_list1 = input("Enter colors in color-list1 (comma-separated): ").split(',')
color_list2 = input("Enter colors in color-list2 (comma-separated): ").split(',')

# Remove any leading/trailing white spaces in color names and convert to lowercase
color_list1 = [color.strip().lower() for color in color_list1]
color_list2 = [color.strip().lower() for color in color_list2]

# Find colors in color-list1 not contained in color-list2
unique_colors = [color for color in color_list1 if color not in color_list2]

# Print the unique colors
print("Colors in color-list1 not contained in color-list2:")
for color in unique_colors:
    print(color)
