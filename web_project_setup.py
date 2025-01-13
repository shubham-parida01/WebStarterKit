import os

def create_project_structure(project_name):
    # Define folder and file structure
    directories = [
        os.path.join(project_name, 'css'),
        os.path.join(project_name, 'js')
    ]
    
    files = [
        os.path.join(project_name, 'index.html'),
        os.path.join(project_name, 'css', 'style.css'),
        os.path.join(project_name, 'js', 'script.js')
    ]
    
    # Create the directories
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Create the HTML file
    with open(files[0], 'w') as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Project</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <h1>Welcome to the Simple Project</h1>
    <script src="js/script.js"></script>
</body>
</html>""")
    
    # Create empty CSS file
    with open(files[1], 'w') as f:
        f.write("")  # Empty content for style.css
    
    # Create empty JS file
    with open(files[2], 'w') as f:
        f.write("")  # Empty content for script.js
    
    print(f"Project '{project_name}' structure created successfully!")

# Usage: Call the function with your desired project name
project_name = input("Enter project name: ")
create_project_structure(project_name)
