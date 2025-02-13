#  Medical OCR Project

##  Overview
The **Medical OCR Project** automates text extraction from scanned medical documents (PDFs) using Optical Character Recognition (OCR). It minimizes the time required for manual data entry by processing **prescriptions** and **patient details** based on the provided input.

##  Features
✅ Converts PDFs to images using `pdf2image`  
✅ Enhances image clarity with **adaptive thresholding** (`OpenCV`)  
✅ Extracts text using `pytesseract` (Tesseract OCR)  
✅ Uses **regex** to extract structured data  
✅ Supports both **prescription and patient details extraction**  
✅ API tested with **Postman**  

##  Technologies Used
- `opencv-python` 🖼️ (Image Processing)  
- `Pillow` 🖌️ (Image Manipulation)  
- `pdf2image` 📄 (PDF to Image Conversion)  
- `pytesseract` 🔍 (OCR Text Extraction)  
- `re` 🔡 (Regex for Structured Text Extraction)  

##  Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-link>
   cd medical-ocr
2. **Install dependencies:**
   pip install -r requirements.txt