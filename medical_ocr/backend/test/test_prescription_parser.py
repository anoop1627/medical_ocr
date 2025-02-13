import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from parser_prescription import PrescriptionParser
import pytest


def test_get_name():
    pp = PrescriptionParser(document_text)
    assert pp.get_field('patient_name') == 'Marta Sharapova'

def test_get_address():
    pp = PrescriptionParser(document_text)
    assert pp.get_field('patient_address') == '9 tennis court, new Russia, DC'


document_text = '''Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times'''