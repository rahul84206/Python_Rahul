import PyPDF2
from docx import Document


def pdf_to_word(pdf_path, word_path):
    # Open the PDF and Word files
    pdf_file = open(pdf_path, 'rb')
    pdf = PyPDF2.PdfReader(pdf_file)
    doc = Document()

    # Iterate through each page in the PDF
    for page in pdf.pages:
        # Extract the text from the page
        page_text = page.extract_text()
        # Add the text to the Word document
        doc.add_paragraph(page_text)

    # Save the Word document
    doc.save(word_path)


# Test the function with a PDF and Word file
pdf_to_word(r'C:/Users/rahul/Downloads/English_Test_1.pdf',
            r'C:/Users/rahul/Downloads/English_Test_1.docx')
