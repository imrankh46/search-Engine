# Text Improvement Engine

## Project Overview

The Text Improvement Engine is a tool that analyzes a given text and suggests improvements based on the similarity to a list of "standardized" phrases. These standardized phrases represent the ideal way certain concepts should be articulated, and the tool recommends changes to align the input text closer to these standards.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- User-friendly interface for inputting text.
- Semantically analyzes input text using cosine similarity with word embeddings.
- Suggests replacements for phrases in the input text with their more "standard" versions.
- Provides similarity scores for suggested improvements.

## Requirements

- Python (>= 3.6)
- Gradio (>= 3.14.0)
- spaCy (>= 2.3.0)
- scikit-learn (>= 0.23.0)

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
```
## Setup
Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/text-improvement-engine.git
```
Navigate to the project directory:
```bash
cd text-improvement-engine
```
Install the required packages (as mentioned in the Requirements section).

Run the Text Improvement Engine using the provided Gradio interface:
```bash
python text_improvement_engine.py
```
Access the tool through your web browser at the provided URL (e.g., http://localhost:7860).

## Usage
Enter the text you want to analyze into the input text box.
Click the "Submit" button.
The tool will provide a list of suggestions to replace phrases in the input text with their more "standard" versions.
Each suggestion includes the original phrase, the recommended replacement, and the similarity score.

## Documentation

For more detailed documentation on the code structure, design decisions, and usage, please refer to the [Documentation](documentation.md) file.

## Contributing

We welcome contributions from the community. If you would like to contribute to this project, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
