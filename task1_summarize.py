import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import docx
import PyPDF2

# -------------------------------
# LOAD MODEL (BART)
# -------------------------------
@st.cache_resource
def load_model():
    model_name = "facebook/bart-large-cnn"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# -------------------------------
# READ FILE CONTENT
# -------------------------------
import docx
import PyPDF2

def read_file_content(uploaded_file):
    if uploaded_file is None:
        return ""

    file_name = uploaded_file.name.lower()

    try:
        # ✅ TXT FILE
        if file_name.endswith(".txt"):
            return uploaded_file.read().decode("utf-8", errors="ignore")

        # ✅ PDF FILE
        elif file_name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted
            return text

        # ✅ DOCX FILE
        elif file_name.endswith(".docx"):
            doc = docx.Document(uploaded_file)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text

        else:
            return ""

    except Exception as e:
        return ""

# -------------------------------
# SUMMARIZATION FUNCTION
# -------------------------------
def summarize_text(text, max_length, min_length):
    inputs = tokenizer(
        text[:1024],
        max_length=1024,
        truncation=True,
        return_tensors="pt"
    )

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# -------------------------------
# UI
# -------------------------------
st.title("🧠 NLP Text Summarizer (BART Model)")
st.write("Upload a file and generate a concise summary using NLP.")

# File uploader
uploaded_file = st.file_uploader(
    "📁 Upload a file",
    type=["txt", "pdf", "docx"]
)

text = ""

# Read file
if uploaded_file is not None:
    text = read_file_content(uploaded_file)
    st.success(f"✅ File uploaded: {uploaded_file.name}")

    if text.strip() == "":
        st.error("❌ Could not extract text from file!")

# Sliders
col1, col2 = st.columns(2)

with col1:
    max_length = st.slider(
        "📏 Maximum Summary Length",
        min_value=30,
        max_value=200,
        value=130,
        step=10
    )

with col2:
    min_length = st.slider(
        "📝 Minimum Summary Length",
        min_value=10,
        max_value=100,
        value=30,
        step=5
    )

# Button
if st.button("Summarize"):
    if text.strip() != "":
        with st.spinner("Processing... ⏳"):
            summary = summarize_text(text, max_length, min_length)

        st.subheader("📌 Summary:")
        st.success(summary)

        # Stats
        original_words = len(text.split())
        summary_words = len(summary.split())

        st.write(f"📝 Original Length: {original_words} words")
        st.write(f"✂️ Summary Length: {summary_words} words")

        if original_words > 0:
            st.write(f"📊 Compression Ratio: {(summary_words / original_words) * 100:.1f}%")

    else:
        st.warning("⚠️ Please upload a valid file first!")