import streamlit as st
import matplotlib.pyplot as plt

def app():
    st.write('Statistical Analysis via Visualizations')
    
    # Define data for the pie chart
    sizes = [45, 55]  # Sizes for Set A and Set B
    labels = ['Set A', 'Set B']
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Display the pie chart using Streamlit
    st.pyplot(fig)
