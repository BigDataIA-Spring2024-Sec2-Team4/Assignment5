### Methods for Extracting, Selecting, and Engineering Features from Textual Data

When working with textual data, there are specific methods for extracting, selecting, and engineering features to prepare the data for machine learning models. Here is a detailed summary of these methods:

1. **Text Extraction:**
   - **Text Problem Formulation:** Define the problem statement related to the textual data.
   - **Text Curation:** Collect and curate the text data from various sources.
   - **Text Preparation and Wrangling:** Clean the text data by removing HTML tags, punctuation, numbers, and white spaces.
   - **Text Exploration:** Use techniques like word clouds to understand the composition of the text data.

2. **Text Preprocessing:**
   - **Normalization:** Lowercase the text, remove stop words, perform stemming, and lemmatization.
   - **Creating Bag-of-Words (BOW) and N-Grams:** Convert the text into a numerical format.
   - **Document Term Matrix (DTM):** Organize the BOW and N-Grams into a matrix for analysis.

3. **Feature Selection:**
   - **Term Frequency (TF):** Measure the frequency of terms in the text data.
   - **Document Frequency:** Determine how often a term appears in different documents.
   - **Chi-Square Test:** Evaluate the independence between terms and classes.
   - **Mutual Information Measure:** Assess the relationship between terms and classes.

4. **Feature Engineering:**
   - **Converting Numbers into Tokens:** Transform numerical data into text tokens.
   - **Creating N-Grams:** Generate combinations of words for analysis.
   - **Name Entity Recognition:** Identify and extract named entities from the text.
   - **Parts of Speech Tagging:** Label words in the text with their parts of speech.

These methods help in preparing textual data for machine learning models by converting unstructured text into structured data that can be used for analysis and prediction. By following these steps, data scientists can effectively leverage textual data for various applications in fintech and other industries.