# TEXT-SUMMARIZATION-TOOL

*COMPANY* : CODTECH IT SOLUTIONS
*NAME* : PAVITRA SAVARAPU
*INTERN ID* : CTIS7186
*DOMAIN* : Artificial Intelligence
*DURATION* : 6 WEEKS
*MENTOR* : NEELA SANTOSH

*DESCRIPTION*:
task1_summarize.py is a Streamlit-based text summarization app that allows users to upload a document, extract its text, and generate a concise summary using a pretrained transformer model.

What the task does:
Provides a web UI with file upload support for .txt, .pdf, and .docx
Extracts raw text from the uploaded document
Applies a pretrained BART summarization model to generate a short summary
Displays summary output plus basic statistics like original length, summary length, and compression ratio
Lets users adjust summary length using UI sliders
ools and architecture
Streamlit: builds the interactive web interface and handles file upload, layout, buttons, and output display
Hugging Face Transformers: loads facebook/bart-large-cnn and uses it to tokenize input text, run generation, and decode the summary
Caching via @st.cache_resource to speed up repeated model loading

Libraries used:
streamlit
transformers
docx
PyPDF2

How it works:
Upload a file through the Streamlit uploader
The script reads the file contents:
.txt: plain text decode
.pdf: PDF extraction via PyPDF2
.docx: paragraph extraction via python-docx
The text is truncated to the model’s input limit and tokenized
The BART summarization model generates a summary with user-controlled max_length and min_length
The result is shown in the browser, with compression metrics

Why it is useful:
This task demonstrates a practical NLP pipeline for document summarization, combining document parsing, transformer-based generation, and a user-friendly web front end. It is suitable for rapid prototyping and presentation of an NLP summarization capability.

