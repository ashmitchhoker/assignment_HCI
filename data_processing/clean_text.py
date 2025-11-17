import re

def clean_pdf_text(text):
    # --- Remove page markers like: --- Page 51 ---
    text = re.sub(r'-{2,}\s*Page\s*\d+\s*-{2,}', ' ', text, flags=re.IGNORECASE)

    # --- Remove timestamps (with or without seconds) ---
    text = re.sub(r'\d{1,2}-[A-Za-z]{3}-\d{2}\s+\d{1,2}:\d{2}(:\d{2})?\s*[APMapm]{2}', ' ', text)

    # --- Remove PDF header/footer garbage like: ---
    # Career Guidance Book Vol-2_Engineering_1-96.indd 27
    # ...Vol-3 - Research and Development_335-408.indd_ 342
    text = re.sub(r'Career Guidance Book.*?indd[_\s-]*\d{1,4}', ' ', text, flags=re.IGNORECASE)

    # --- Remove standalone page numbers (e.g., "66 |") ---
    text = re.sub(r'\b\d{1,4}\s*\|', ' ', text)

    # --- Remove lines containing only numbers (page numbers) ---
    text = re.sub(r'^\s*\d{1,4}\s*$', ' ', text, flags=re.MULTILINE)

    # --- Remove leftover bullets, pipes, dots ---
    text = re.sub(r'[|·•◦▪]+', ' ', text)

    # --- Remove stray unicode quotes and artifacts ---
    text = text.replace('“', '"').replace('”', '"')
    text = text.replace('’', "'").replace('‘', "'")
    text = text.replace('—', ' ')   # em-dash
    text = text.replace('–', ' ')   # en-dash
    text = text.replace('­', '')    # soft hyphen

    # --- Remove unreadable unicode (OCR junk) ---
    text = text.encode("ascii", errors="ignore").decode()

    # --- Collapse weird spacing ---
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# Read the extracted text file
with open("raw_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Clean the text
cleaned_text = clean_pdf_text(raw_text)

# Write the cleaned text to a new file
with open("cleaned_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)
