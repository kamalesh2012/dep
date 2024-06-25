import streamlit as st
from datetime import date

def generate_bill(quantity, cost_per_brick, company_name):
    total_cost = quantity * cost_per_brick
    today = date.today().strftime("%Y-%m-%d")
    
    bill = f"""
    ## Invoice
    
    Date: {today}
    Company Name: {company_name}
    
    Quantity: {quantity} bricks
    Cost per Brick: ${cost_per_brick:.2f}
    
    Total Amount: ${total_cost:.2f}
    """
    return bill

def main():
    st.title('AKC Bricks Bill Generator')
    
    quantity = st.number_input('Enter quantity of bricks:', min_value=1, step=1)
    cost_per_brick = st.number_input('Enter cost per brick ($):', min_value=0.01, step=0.01)
    
    if st.button('Generate Bill'):
        company_name = 'AKC Bricks'  # You can customize this
        
        bill = generate_bill(quantity, cost_per_brick, company_name)
        st.markdown(bill)

if __name__ == '__main__':
    main()

