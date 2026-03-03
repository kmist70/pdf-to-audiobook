# 📖 PDF to Audiobook

A Python command-line tool that converts any PDF document into spoken audio using text-to-speech. Supports PDFs of 500+ pages with full input validation and adjustable speech rate.

## Features

- 🔊 Reads any page of a PDF aloud using `pyttsx3`
- 📄 Handles large PDFs (500+ pages) via `PyPDF2` parsing
- ✅ Robust input validation â€” catches invalid page numbers and non-integer inputs with 100% error coverage
- 🎚️ Adjustable speech rate (default: 200 WPM)
- ⏹️  Stop playback at any time with `Ctrl + C`
- 🔁 Loop to read multiple pages in one session

## Demo

```
Welcome to Text-To-Speech!
Ex: To read a specific page, enter the current page number (in the PDF reader, not the actual PDF).

Enter page number: 3
The current speech rate is 200 WPM.
Would you like to change the speech rate? Enter 'YES' to change it: no

You can stop the speech process at anytime by pressing Ctrl + C

Would you like to read more pages? Enter 'YES' to continue: no

Thank you for using Text-To-Speech!
```

## Prerequisites

- Python 3.7+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kmist70/pdf-to-audiobook.git
   cd pdf-to-audiobook
   ```

2. Install dependencies:
   ```bash
   pip install pyttsx3 PyPDF2
   ```

## Usage

1. Place your PDF file in the project directory and rename it `sample.pdf` (or update the filename in `main.py`).
2. Run the script:
   ```bash
   python main.py
   ```
3. Follow the prompts to select a page and optionally adjust the speech rate.

## How It Works

1. Opens `sample.pdf` in binary read mode using `PyPDF2.PdfReader`
2. Prompts the user for a page number, with a validation loop that rejects out-of-range and non-integer inputs
3. Optionally adjusts speech rate via `pyttsx3.setProperty('rate', ...)`
4. Extracts the page text with `.extract_text()` and reads it aloud
5. Handles `KeyboardInterrupt` (Ctrl+C) to gracefully stop mid-speech
6. Repeats until the user chooses to exit

## Project Structure

```
pdf-to-audiobook/
â”œâ”€â”€ main.py        # Core application logic
â”œâ”€â”€ sample.pdf     # Sample PDF for testing
â””â”€â”€ .vscode/       # VS Code workspace settings
```

## Dependencies

| Library   | Purpose                          |
|-----------|----------------------------------|
| `pyttsx3` | Offline text-to-speech engine    |
| `PyPDF2`  | PDF parsing and text extraction  |

## Future Improvements

- [ ] Accept any PDF file path as a command-line argument
- [ ] Add support for reading a range of pages
- [ ] Export audio output to an `.mp3` or `.wav` file

## Author

**Krishna M** — [github.com/kmist70](https://github.com/kmist70)
