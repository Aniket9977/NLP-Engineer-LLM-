import pdfplumber

def extract_content(filename, content):
    if filename.endswith(".pdf"):
        with open(filename, "wb") as f:
            f.write(content)
        return extract_from_pdf(filename)
    elif filename.endswith(".txt"):
        return {"text": content.decode("utf-8")}
    else:
        return {"error": "Unsupported file format"}

def extract_from_pdf(filepath):
    extracted_data = {"text": "", "tables": []}
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            extracted_data["text"] += page.extract_text() or ""
            tables = page.extract_tables()
            if tables:
                extracted_data["tables"].extend(tables)
    return extracted_data
