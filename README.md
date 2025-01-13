# Web Starter Kit Automation

A Python-based automation tool that generates the basic structure for a simple HTML, CSS, and JavaScript project.

## Features

- Creates a project directory with the following structure:
  - `index.html`: A basic HTML file linked to CSS and JS files.
  - `css/`: A folder containing an empty `style.css`.
  - `js/`: A folder containing an empty `script.js`.


## Folder Structure

After running the automation script, the following folder structure will be created:

```
<project_name>/
│
├── css/
│   └── style.css      (empty)
│
├── js/
│   └── script.js      (empty)
│
└── index.html         (HTML file linked to CSS and JS)
```

- **`<project_name>/`**: The root folder of your project.
  - **`css/`**: A folder containing an empty `style.css` file for styling.
  - **`js/`**: A folder containing an empty `script.js` file for JavaScript code.
  - **`index.html`**: The main HTML file that links to the `style.css` and `script.js` files.

## Requirements

- Python 3.x
- Git (Optional, for version control)

## Installation

1. Clone or download this repository.
2. Ensure Python 3.x is installed on your system.
3. (Optional) Install Git if you plan to use version control.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project folder where the script is located.
3. Run the Python script:
   ```bash
   python web_project_setup.py
   ```
4. Enter the desired project name when prompted.

The script will create the necessary project folder structure as follows:

```
<project_name>/
│
├── css/
│   └── style.css  (empty)
│
├── js/
│   └── script.js  (empty)
│
└── index.html
```

## License

This project is licensed under the MIT License.
