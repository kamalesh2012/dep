import streamlit as st
from datetime import date
from fpdf import FPDF
import base64

# Function to generate PDF
def generate_pdf(quantity, cost_per_brick, company_name, logo_path):
    total_cost = quantity * cost_per_brick
    today = date.today().strftime("%Y-%m-%d")
    
    pdf = FPDF()
    pdf.add_page()

    # Add logo
    pdf.image(logo_path, 10, 8, 33)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Invoice", ln=True, align='C')

    pdf.ln(10)  # Add a line break

    pdf.cell(200, 10, txt=f"Date: {today}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Company Name: {company_name}", ln=True, align='L')

    pdf.ln(10)  # Add a line break

    pdf.cell(200, 10, txt=f"Quantity: {quantity} bricks", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Cost per Brick: ${cost_per_brick:.2f}", ln=True, align='L')

    pdf.ln(10)  # Add a line break

    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=f"Total Amount: ${total_cost:.2f}", ln=True, align='L')

    return pdf

def get_pdf_download_link(pdf):
    pdf_output = pdf.output(dest="S").encode("latin1")
    b64 = base64.b64encode(pdf_output).decode('latin1')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="invoice.pdf">Download PDF</a>'
    return href

def main():
    st.title('AKC Bricks Bill Generator')
    st.markdown("<style>body {background-color: #f0f0f0;}</style>", unsafe_allow_html=True)
    
    quantity = st.number_input('Enter quantity of bricks:', min_value=1, step=1)
    cost_per_brick = st.number_input('Enter cost per brick ($):', min_value=0.01, step=0.01)
    logo_path = "https://musigma-my.sharepoint.com/:i:/g/personal/kamalesh_a_mu-sigma_com/Ee2hoQ70QzRIl52pNNRMdHgBth5f2UtGr1-ftDaoXc266w?e=yse0Uh"  # Path to the company logo
    
    if st.button('Generate Bill'):
        company_name = 'AKC Bricks'
        
        pdf = generate_pdf(quantity, cost_per_brick, company_name, logo_path)
        download_link = get_pdf_download_link(pdf)
        
        st.markdown(download_link, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
