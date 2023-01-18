# bookstore-management
https://github.com/gamv335/bookstore-management/edit/main/README.md
## Table of Contents
1. [Description](https://github.com/gamv335/bookstore-management/edit/main/README.md#description)
2. [Installation](https://github.com/gamv335/finalCapstone/blob/main/README.md#installation)
3. [Usage](https://github.com/gamv335/finalCapstone/blob/main/README.md#usage)
4. [Credits](https://github.com/gamv335/finalCapstone/blob/main/README.md#credits)

## Description
The program available in this repository aims to allow user to manage inventory levels of SKUs across diverse geographical locations. 

## Installation
you will first need to have Python and Git installed on your computer. You can download the latest version of Python from the official website: https://www.python.org/downloads/ and git from https://git-scm.com/downloads

Once you have Python and Git installed, you can use the following steps to run the file:

Open a command prompt or terminal window.

Use the "git clone" command to download the file from GitHub:

    git clone https://github.com/gamv335/finalCapstone.git

Navigate to the directory where the file was downloaded. For example:

    cd <repository>

Run the Python file using the "python" command. For example:

    python <filename>.py

Dependencies required to run the program, may also need to install those using pip. You can install them by running the command:

    pip install -r requirements.txt

Please make sure the requirements.txt file is present in the same directory where the script is located, also ensure to have internet connection as pip will download the dependencies from the internet.

## Usage
The program open up a menu with the following features:
1. Update shoe list from database: automatically reads the database file and update the relevant variables.
2. Add stock entry: Allow a field by field entry of a stock.
3. Code search SKU: Allos the user to enter a SKU number and return the stock data of the product. 
4. Display stock data: Prints a table with the latest stock data including total cost of the inventory per stock entry.
5. Re-stock tool: Finds the lowest stock entry and ask the user if wants to add stock and how many.
6. Run automated sale: Run a 20% discount on the entry with highest stock levels.

## Credits
* gamv335

