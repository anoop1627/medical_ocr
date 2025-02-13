#  Medical OCR Project

##  Overview
The **Medical OCR Project** automates text extraction from scanned medical documents (PDFs) using Optical Character Recognition (OCR). It minimizes the time required for manual data entry by processing **prescriptions** and **patient details** based on the provided input.

## Project Structure

- **backend/**: contains the FastAPI backend server code.
- **tests/**: Contains the test cases for backend.
- **requirements.txt**: Lists all the required Python packages.
- **readme.md**: Provides an overview and instructions for the project.

##  Features
 - Converts PDFs to images using `pdf2image`  
 - Enhances image clarity with **adaptive thresholding** (`OpenCV`)  
 - Extracts text using `pytesseract` (Tesseract OCR)  
 - Uses **regex** to extract structured data  
 - Supports both **prescription and patient details extraction**  
 - API tested with **Postman**  

##  Technologies Used
- `opencv-python`  (Image Processing)  
- `Pillow`  (Image Manipulation)  
- `pdf2image`  (PDF to Image Conversion)  
- `pytesseract`  (OCR Text Extraction)  
- `re`  (Regex for Structured Text Extraction)  

##  Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/anoop1627/medical_ocr
   cd medical-ocr
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
