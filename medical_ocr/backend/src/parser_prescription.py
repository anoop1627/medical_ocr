import re
from parser_generic import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name' : self.get_field('patient_name'),
            'patient_address' : self.get_field('patient_address'),
            'patient_medicine': self.get_field('patient_medicine'),
            'patient_directions': self.get_field('patient_directions'),
            'patient_refill': self.get_field('patient_refill')
        }

    def get_field(self, field_name):


        pattern_dict = {
            'patient_name': {'pattern' : 'Name:(.*)Date','flags': 0},
            'patient_address': {'pattern' : 'Address:(.*)\n', 'flags': 0},
            'patient_medicine': {'pattern' : 'K\n(.*\n.*)Directions', 'flags': re.DOTALL},
            'patient_directions': {'pattern' : 'Directions:..(.*..*)Refill', 'flags': re.DOTALL},
            'patient_refill': {'pattern' : 'Refill: (\d) times', 'flags': 0}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


if __name__=='__main__':
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
    pp = PrescriptionParser(document_text)
    print(pp.parse())