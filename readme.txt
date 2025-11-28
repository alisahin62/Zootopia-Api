# Animal Info Cards Generator

A Python project that generates dynamic HTML cards for animal information.

## Description

This program fetches information about a specific animal and creates attractive HTML cards with details such as diet, location, and type.

## Prerequisites

- Python 3.x
- `data_fetcher` module (for API queries)
- `animals_template.html` template file

## Installation

1. Clone the repository
2. Ensure `animals_template.html` is present in the project directory
3. The template must contain the placeholder `__REPLACE_ANIMALS_INFO__`

## Usage
```bash
python animals_web_generator.py
```

Enter an animal name when prompted. The program will then create an `animals.html` file with the animal information.

## How It Works

1. User enters an animal name
2. Data is fetched via `data_fetcher`
3. An HTML card is created for each animal found
4. The cards are inserted into the HTML template
5. The finished page is saved as `animals.html`

## Output

The generated cards display:
- **Name** of the animal
- **Diet**
- **Location**
- **Type** (optional)

