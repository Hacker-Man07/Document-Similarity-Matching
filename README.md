# Document Similarity Matching System

## Overview

This project implements a system to automatically categorize incoming invoices by matching them to existing templates or previously processed invoices based on their content and structure.

## Features

- **Text Extraction**: Extracts text content from PDF invoices using PyPDF2.
- **Feature Extraction**: Extracts relevant features such as invoice numbers, dates, amounts, addresses, and item descriptions from the text.
- **Similarity Calculation**: Combines Cosine Similarity, Feature-based Similarity, and Jaccard Similarity to match invoices.
- **Database Integration**: Stores and retrieves existing invoices for comparison using a simple in-memory database.
- **Evaluation**: Evaluates the matching performance using predefined metrics.


## Getting Started

### Prerequisites

- Python 3.x
- IDE


## Installing Dependencies
Ensure your virtual environment is activated, then install dependencies:

### Create a virtual environment
```bash
python -m venv venv
```
### Activate the virtual environment (Windows)
```bash
venv\Scripts\activate
```
(Linux / Mac)
```bash
source venv/bin/activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Running the Code
#### Prepare Data:

- Place your training invoice PDF files in the data/training/ directory.
- Place your testing invoice PDF files in the data/testing/ directory.

## Run the Program:
```bash
python src/main.py
```
