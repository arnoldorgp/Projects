# Problem 1: Full name formatter example
full_name_input = "                 Arnoldo René Gudiño Ponce          "

# 1. Normalize by removing extra spaces at ends
cleaned_name = full_name_input.strip()
words = cleaned_name.split()

# 2. Validation: must not be empty and must have at least two words
if len(words) >= 2 and cleaned_name:
    formatted_name = cleaned_name.title()
    # Extract initials using list comprehension and string joining
    initials = "".join([word[0].upper() + "." for word in words])

    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")
else:
    print("Error: invalid input")

