import streamlit as st
import boto3

def fetch_file_from_s3(bucket_name, file_name):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = response['Body'].read().decode('utf-8')
        return file_content
    except Exception as e:
        st.error(f"Error fetching file from S3: {str(e)}")

def app():
    st.title('Questions Set A and Set B')

    # Define AWS S3 bucket and file names
    bucket_name = 'your_bucket_name'
    file_set_a = 'set_a.txt'
    file_set_b = 'set_b.txt'

    # Function to handle button clicks
    def handle_button_click(button_name):
        if button_name == 'Set A':
            file_content = fetch_file_from_s3(bucket_name, file_set_a)
            st.text_area('Set A Content', value=file_content, height=400)
        elif button_name == 'Set B':
            file_content = fetch_file_from_s3(bucket_name, file_set_b)
            st.text_area('Set B Content', value=file_content, height=400)

    # Display buttons
    st.write('Select a Set:')
    if st.button('Set A'):
        handle_button_click('Set A')
    if st.button('Set B'):
        handle_button_click('Set B')

if __name__ == "__main__":
    app()
