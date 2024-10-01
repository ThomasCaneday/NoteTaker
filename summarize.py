import openai

# Function to turn a txt file into lecture notes
def txt_to_lecture_notes(file_path, api_key):
    # Load the content of the txt file
    try:
        with open(file_path, 'r') as file:
            text_content = file.read()
    except FileNotFoundError:
        return "Error: File not found. Please check the file path."
    
    # OpenAI API Key
    openai.api_key = api_key
    
    # Use OpenAI's API to summarize the text content into lecture notes
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # You can choose a different model if needed
            messages=[
                {"role": "system", "content": "You are an expert lecturer. Summarize the following text into concise, well-structured lecture notes."},
                {"role": "user", "content": text_content}
            ],
            temperature=0.5,
            max_tokens=1500  # Adjust as needed depending on the length of the text
        )

        # Extract and return the response text
        lecture_notes = response['choices'][0]['message']['content']
        return lecture_notes

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
api_key = "your_openai_api_key"
file_path = "path_to_your_txt_file.txt"
notes = txt_to_lecture_notes(file_path, api_key)
print(notes)
