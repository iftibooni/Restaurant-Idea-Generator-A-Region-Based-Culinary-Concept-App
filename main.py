import streamlit as st
import Langchain_helper

# Custom CSS for styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    
    :root {
        --primary: #FF6B6B;
        --secondary: #4ECDC4;
        --dark: #292F36;
        --light: #F7FFF7;
        --accent: #FFE66D;
    }
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background-color: #f8f9fa;
    }
    
    .title {
        color: var(--primary);
        font-size: 2.5rem !important;
        font-weight: 600 !important;
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .sidebar .sidebar-content {
        background-color: var(--dark) !important;
        color: white !important;
    }
    
    .sidebar .stSelectbox label {
        color: white !important;
        font-weight: 400 !important;
    }
    
    .sidebar .stSelectbox select {
        background-color: var(--light) !important;
        color: var(--dark) !important;
        border: 2px solid var(--secondary) !important;
        border-radius: 8px !important;
    }
    
    .restaurant-name {
        color: var(--dark) !important;
        font-size: 2rem !important;
        font-weight: 600 !important;
        text-align: center;
        padding: 1rem;
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid var(--primary);
    }
    
    .menu-title {
        color: var(--secondary) !important;
        font-size: 1.5rem !important;
        border-bottom: 2px solid var(--secondary);
        padding-bottom: 0.5rem;
        margin-top: 1.5rem !important;
    }
    
    .menu-item {
        background-color: white;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.2s;
        font-size: 1rem;
        color: var(--dark) !important;
    }
    
    .menu-item:hover {
        transform: translateX(5px);
        border-left: 3px solid var(--accent);
    }
    
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #6c757d;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# App title with custom class
st.markdown('<div class="title">Restaurant Name Generator</div>', unsafe_allow_html=True)

# Sidebar with dish selection
with st.sidebar:
    st.markdown("""
    <div style="padding: 1rem; border-bottom: 1px solid #4ECDC4;">
        <h2 style="color: #4ECDC4; margin-bottom: 1.5rem;">Cuisine Selector</h2>
        <p>Choose a regional Pakistani cuisine to generate restaurant name and menu items.</p>
    </div>
    """, unsafe_allow_html=True)
    
    dish = st.selectbox("Pick A Dish", ('Peshawri', 'Lahori', 'Gilgiti', 'Chitrali', 'Karachi', 'Quetta', 'Balochi'))

# Main content
if dish:
    response = Langchain_helper.resturant_Genearator(dish)
    
    # Restaurant name with custom styling
    st.markdown(f'<div class="restaurant-name">{response["restaurant_name"].strip()}</div>', unsafe_allow_html=True)
    
    # Menu items - fixed display logic
    st.markdown('<div class="menu-title">Menu Items</div>', unsafe_allow_html=True)
    
    # Improved menu items processing
    menu_items = response['menu_items'].strip().split(",")
    menu_items = [item.strip() for item in menu_items if item.strip()]
    
    if menu_items:
        for item in menu_items:
            st.markdown(f'<div class="menu-item">🍲 {item}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="menu-item">No menu items found</div>', unsafe_allow_html=True)

