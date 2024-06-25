import streamlit as st
from datetime import date

# Function to generate bill
def generate_bill(quantity, cost_per_brick, company_name):
    total_cost = quantity * cost_per_brick
    today = date.today().strftime("%Y-%m-%d")

    bill = f"""
    <div style="padding: 10px; border: 2px solid #000; border-radius: 5px; max-width: 600px; margin: auto; font-family: Arial, sans-serif;">
        <h2 style="text-align: center;">Invoice</h2>
        <p><strong>Date:</strong> {today}</p>
        <p><strong>Company Name:</strong> {company_name}</p>
        <hr>
        <p><strong>Quantity:</strong> {quantity} bricks</p>
        <p><strong>Cost per Brick:</strong> ${cost_per_brick:.2f}</p>
        <hr>
        <h3><strong>Total Amount:</strong> ${total_cost:.2f}</h3>
    </div>
    """
    return bill

def main():
    st.title('AKC Bricks Bill Generator')
    st.markdown("<style>body {background-color: #f0f0f0;}</style>", unsafe_allow_html=True)
    
    quantity = st.number_input('Enter quantity of bricks:', min_value=1, step=1)
    cost_per_brick = st.number_input('Enter cost per brick ($):', min_value=0.01, step=0.01)
    
    if st.button('Generate Bill'):
        company_name = 'AKC Bricks'
        bill = generate_bill(quantity, cost_per_brick, company_name)
        
        st.markdown(bill, unsafe_allow_html=True)
        
        # Add a print button
        print_button_code = '''
        <script>
        function printBill() {
            var printContents = document.body.innerHTML;
            var originalContents = document.body.innerHTML;
            document.body.innerHTML = printContents;
            window.print();
            document.body.innerHTML = originalContents;
        }
        </script>
        <button onclick="printBill()" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">Print</button>
        '''
        st.markdown(print_button_code, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
