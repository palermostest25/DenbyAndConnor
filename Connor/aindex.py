import os

def replace_noindex_with_index(directory=os.getcwd()):  # Set default to current directory
    """Replaces the word "noindex" with "index" in all HTML files within a directory."""

    for filename in os.listdir(directory):
        if filename.endswith(".html"):  # Check for HTML files
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                content = file.read()  # Read the file's content

            new_content = content.replace("noindex", "index")  # Perform the replacement

            with open(filepath, "w") as file:
                file.write(new_content)  # Write the modified content back to the file

            print(f"Replaced 'noindex' with 'index' in {filename}")  # Print confirmation

# Now you can directly call the function without specifying a directory:
replace_noindex_with_index()  # Automatically processes the current directory

