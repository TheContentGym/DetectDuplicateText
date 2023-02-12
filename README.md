# DetectDuplicateText
Detects duplicate text in a page - same thing written multiple times using same or different words:

![image](https://user-images.githubusercontent.com/67150538/213660797-b4bbf859-965f-4d8f-9622-cae668202132.png)


A python script to detect duplicate sentences on a web page.

## Table of Contents

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)

## Dependencies

The following python packages are required to run this script:

- beautifulsoup4
- requests
- re
- nltk

## Installation

To install the required packages, run the following command in your terminal/command prompt:


## Usage

1. Clone the repository or download the script.
2. Open terminal/command prompt and navigate to the script's directory.
3. Run the script with the following command:
4. The script will prompt you to enter the URL of the web page you want to check for duplicates. Enter the URL and hit enter.
5. The script will display any duplicate sentences found on the web page.

## Code Explanation

The script performs the following steps to detect duplicate sentences on a web page:

1. Imports the required packages.
2. Downloads the 'punkt' dataset, which is used by the sent_tokenize function to tokenize text into sentences.
3. Defines a `clean_text` function to clean the text by removing punctuation and converting it to lowercase.
4. Accepts the URL of the web page to be checked for duplicates as input.
5. Makes a request to the web page and retrieves its HTML content.
6. Parses the HTML content using BeautifulSoup to extract the text.
7. Tokenizes the text into sentences using the sent_tokenize function.
8. Cleans each sentence and creates a Counter object with the cleaned sentences as keys.
9. Finds duplicate sentences by looping through the items in the Counter object and checking if the count is greater than 1.
10. Prints the duplicate sentences.
