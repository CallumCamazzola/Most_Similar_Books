# Book Similarity Analyzer

## Overview
The **Book Similarity Analyzer** is a program that takes a list of books and a corresponding set of user reviews and determines which books are most similar to each other. It does this by using a **vector-based similarity system** to measure how closely related one book is to another based on user sentiment, keywords, and review structure.

## Features
- **Vector-Based Similarity Measurement:** Uses numerical representations of user reviews to compare books.
- **Cosine Similarity Calculation:** Determines how closely related two books are based on review content.
- **Ranked Similarity Output:** Generates a ranked list of the most similar books for each book in the dataset.

## How It Works
1. **Input:** The program takes two inputs:
   - A list of books (titles and metadata).
   - A list of user reviews associated with each book.
2. **Processing:**
   - Converts reviews into vector representations.
   - Applies **cosine similarity** to measure the relationships between books.
3. **Output:**
   - A ranked list of books that are most similar to each other based on user review content.

## Usage
1. Prepare a dataset containing:
   - A txt file containig a listing of books.
   - A second file containing user reviews mapped to each book.
2. Run the program with the dataset as input.
3. View the output, which will list book pairings along with their similarity scores.



