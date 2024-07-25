import pandas as pd
from fpdf import FPDF

# Load the Excel file
file_path = r'E:\Nuclear Engineering\Disertation Related Projects\Advanced Screening Approaches for Accelerating Development of Separations Technologies\CFA Obj. 1 Lit. Review Tracker.xlsx'
sheet_name = 'Co-Solvent Extraction System'

# Load the specific sheet into a DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Extract the row with Reference ID 20002
reference_id = 20002
reference_row = df[df['Reference ID'] == reference_id]

# Extract the required information
if not reference_row.empty:
    reference_info = {
        'Key Words': reference_row['Key Words'].values[0],
        'Objective': reference_row['Objective'].values[0],
        'Methodology': reference_row['Methodology'].values[0],
        'Key Findings': reference_row['Key Findings'].values[0],
        'Relevance to Study': reference_row['Relevance to Study'].values[0],
        'Critical Parameters Identified': reference_row['Critical Parameters Identified'].values[0]
    }
    print(reference_info)
else:
    print("Reference ID not found in the data.")

# Example usage
reference_id = 20002
reference_info = extract_reference_info(reference_id)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'REFERENCE: {reference_id}', 0, 1, 'L')
        self.ln(10)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def section_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln(4)

# Create the PDF document
def create_pdf(reference_info):
    pdf = PDF()
    pdf.add_page()
    
    for section, content in reference_info.items():
        pdf.section_title(section)
        pdf.section_body(content)
    
    # Save the PDF
    output_path = f'Reference_{reference_id}.pdf'
    pdf.output(output_path)
    print(f"PDF created: {output_path}")

# Create PDF if reference info was found
if reference_info:
    create_pdf(reference_info)
