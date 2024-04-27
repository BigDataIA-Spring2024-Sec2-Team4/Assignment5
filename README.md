# Assignment5

## Architectural Diagram
![image](https://github.com/BigDataIA-Spring2024-Sec2-Team4/Assignment5/assets/145082704/501a51ee-a3e5-4093-ab01-e4e27e3ae316)


## Problem Statement:
Development of a Structured Database and Text Extraction System for Finance Professional Development Resources

## Project Goals
Utilize Pinecone and OpenAI APIs to create knowledge summaries, generate a contextual knowledge base, utilize vector databases for question answering, and employ GPT-based summaries to provide accurate answers.

## Project Tasks
  
### Step1 Generating Technical Notes from LOS:
        
    1. The script Step1_Summary_LOS.py utilizes OpenAI's GPT to generate technical notes summarizing key Learning Outcome Statements (LOS).
    2. Furthermore, the script integrates with Pinecone for efficient data storage by chunking each LOS and its corresponding technical note and uploading it to Pinecone for retrieval.

 ### Step 2: Question Bank Creation and Data Organization

    1. Question Bank Creation: Generate question banks for each assigned topic. Save these questions as separate TXT files for each topic.
    2. Parsing TXT Files to Generate JSON Schema: Develop a parser to extract questions from TXT files. Create a JSON schema for all questions within each set (Set A and Set B). Include metadata such as the topic to identify the source of the questions.
    3. Data Organization and Storage: Save parsed data in JSON format. Utilize Pinecone for data storage with topics as namespaces.


### Step 3: Using a Vector Database to Find and Answer Questions
    
    1. Utilizing RAG for Question Similarity Search: The system employs RAG (Retrieval-Augmented Generation) to search for similar questions based on information stored in Pinecone. It retrieves relevant question-answer pairs from Set A to assess the accuracy of answers from Set B.
    2. GPT-4 Question Answering Process: Question-answer pairs from Set A are passed to GPT-4 along with a question from Set B and answer choices. GPT-4 processes the input and generates responses, simulating human-like comprehension and reasoning.
    3. Evaluation of Answer Correctness: The system evaluates the correctness of answers provided by GPT-4 and compares them to the actual answers. Results are presented to the user, allowing for further analysis and refinement of the question answering process.

    
### Step 4: Use Knowledge Summaries to Answer Questions
    
    1. Utilizing RAG in Pinecone Vector Database: The system employs RAG (Retrieval-Augmented Generation) within the Pinecone vector database to search for similar embeddings and Learning Outcome Statements (LOS) containing answers to questions from both Set A and Set B.
    2. Tabulating Answer Accuracy: The accuracy of answers to the 100 questions/topics is tabulated and presented to the user.
    3. Evaluation and Discussion: The effectiveness of this approach is discussed in comparison to Task 3, highlighting its strengths and areas for improvement.
    Alternative designs for enhanced question answering are proposed, considering factors such as accuracy, efficiency, and user experience.

## Conclusion

By completing these tasks, we aim to evaluate different approaches for knowledge retrieval and question answering using MaaS APIs, contributing valuable insights for enterprise applications.


## To run the application locally, follow these steps:

1. **Clone the Repository**: Clone the repository onto your local machine.

   ```bash
   git clone https://github.com/BigDataIA-Spring2024-Sec1-Team4/Assignment5
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**: Activate the virtual environment.

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS**:

     ```bash
     source venv/bin/activate
     ```

4. **Run MakeFile to start Docker Compose**: Start the Docker containers using Docker Compose.

   ```bash
   cd Assignment5
   make build-up
   ```

5. **Access Streamlit Interface**: Open your web browser and go to `34.75.0.13:8000` to access the Streamlit interface.

6. **Step1**: On the Streamlit homepage,Users can select a topic from the available topics. generate summaery and save it in pinecone.

7. **Step2 Question_Generation_Page.**:Users can select topics from a dropdown menu and specify the number of questions to generate. Upon clicking the "Generate Questions" button, save data in pinecone
8. **Step3 Question Answers Report** :Upon clicking the "Run QA Workflow" button, the script loads questions from a JSON file and displayes results
9. **Step4 LOS Answers** :  Upon clicking the "Generate Report" button, Generates a pie chart for each topic depicting the distribution of correct and incorrect answers.

5. ## Team Information and Contribution

| Name       | Contribution % | Contributions                             |
|------------|----------------|-------------------------------------------|
| Riya Singh  | 40%            | ContentPDFClass, Schema design, Pydantic validation, Testing with Pytest, Architecture Diagram, README |
| Nidhi Nitin Kulkarani   | 33%            | URLClass, DBT transformation, Schema design, Pydantic validation, Testing with Pytest |
| Deepakraja Rajendran   | 27%            | MetaDataPDFClass, Snowflake Integration, Pydantic validation, Testing with Pytest, README |


