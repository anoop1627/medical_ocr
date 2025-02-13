from pdf2image import convert_from_path
import pytesseract
import util
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser
from project.backend.test.test_prescription_parser import document_text



def extract(file_path, file_format):
    POPPLER_PATH = r'C:\poppler-24.08.0\Library\bin'
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''
    if len(pages)>0:
        page = pages[0]
        processed_img = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_img, lang='eng')
        document_text = '\n' + text

    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()

    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid File Format: {file_format}")

    return extracted_data

if __name__ == '__main__':
    data = extract('../resources/patient_details/pd_2.pdf','patient_details')
    print(data)