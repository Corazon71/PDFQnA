# PDFQnA: A Langchain Chatbot for Querying PDF Documents

This project demonstrates a simple yet powerful question-answering chatbot built with LangChain. It leverages the power of Google Vertex AI's Gemini Pro model for understanding and responding to your questions based on the content of uploaded PDF documents. 

## Features

* **PDF Uploads:** Seamlessly upload your PDF documents to the chatbot interface.
* **Contextual Understanding:** Ask questions in natural language, and the chatbot will search the uploaded document for relevant information.
* **Accurate Responses:**  Get concise and accurate answers powered by Google's advanced language model, Gemini Pro. 

## Technologies Used

* **LangChain:** A framework for building applications with large language models.
* **Google Vertex AI:** Google Cloud's platform for machine learning, providing the Gemini Pro LLM.
* **ChromaDB:** An open-source embedding database for fast and efficient semantic search.
* **Gradio:** A Python library for creating intuitive machine learning demos and web applications.

## Getting Started

1. **Set up Google Cloud Platform:**
   * Create a Google Cloud Project.
   * Enable the Vertex AI API.
   * Create a service account and download its JSON credentials file.
   * Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of your JSON credentials file.

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Configure Credentials:**
   * Open the `.env` file and update the `GOOGLE_APPLICATION_CREDENTIALS` value with the path to your downloaded Google Cloud service account credentials JSON file. 

4. **Run the application:**
   ```bash
   python main.py 
   ```

5. **Use the Chatbot:**
   * Open the Gradio interface in your web browser (the URL will be displayed in your terminal).
   * Upload a PDF document.
   * Start asking questions!