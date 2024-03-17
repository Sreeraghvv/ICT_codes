This repository contains Python code for three different utilities: a Text Summarizer, a Simple Calculator, and a Data Preprocessor. Each utility serves a specific purpose and can be used independently. Below is a brief overview of each utility along with instructions on how to use them.

1. Text Summarizer:
The Text Summarizer is designed to generate a concise summary of a given text document. It utilizes natural language processing techniques to extract the most important sentences from the input text and form a coherent summary. Here's how to use it:

Usage:
Import the TextSummarizer class from text_summarizer.py.
Initialize an instance of TextSummarizer.
Call the summarize(text) method, passing the input text as an argument.
The method returns the summarized text.
2. Simple Calculator:
The Simple Calculator provides basic arithmetic operations such as addition, subtraction, multiplication, and division. It accepts mathematical expressions as input and evaluates them to produce the result. Here's how to use it:

Usage:
Import the SimpleCalculator class from simple_calculator.py.
Initialize an instance of SimpleCalculator.
Call the evaluate(expression) method, passing the mathematical expression as a string argument.
The method returns the result of the evaluation.
3. Data Preprocessor:
The Data Preprocessor offers functionalities to preprocess tabular data, including handling missing values, encoding categorical variables, and scaling numerical features. It provides a convenient way to prepare data for machine learning tasks. Here's how to use it:

Usage:
Import the DataPreprocessor class from data_preprocessor.py.
Initialize an instance of DataPreprocessor.
Call the preprocess(data) method, passing the input data (pandas DataFrame) as an argument.
The method returns the preprocessed data ready for machine learning.
Dependencies:
The Text Summarizer utilizes the nltk library for natural language processing tasks.
The Data Preprocessor relies on pandas for handling tabular data.
Example Usage:
