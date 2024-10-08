import tkinter as tk
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv('GEMINI_API_KEY')

# Function to send API request
def send_request():
    # Get the input from the text box
    user_input = input_text.get("1.0", tk.END).strip()
    
    # Define your Gemini API endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
    
    # Set headers
    headers = {
        "Content-Type": "application/json"
    }

    # Create the payload according to the specified structure
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": user_input  # User input text to be sent to the API
                    }
                ]
            }
        ]
    }

    # Print the payload to the console for debugging
    print("Payload sent to API:", json.dumps(payload, indent=4))

    try:
        # Make the API request
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response_data = response.json()

        # Print the full response to the console for debugging
        print("Full response from API:", json.dumps(response_data, indent=4))

        # Extract the text from the response
        response_text_content = response_data['candidates'][0]['content']['parts'][0]['text']

        # Update the response box with the response text
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, response_text_content)  # Show only the text in the app

    except Exception as e:
        response_text.delete("1.0", tk.END)
        response_text.insert(tk.END, str(e))

# Create the main window
root = tk.Tk()
root.title("Gemini API Client")

# Configure window size and background color
root.geometry("600x600")
root.configure(bg="#ADD8E6")  # Light blue background

# Create a label for instructions
instructions_label = tk.Label(root, text="Enter text to generate content:", bg="#ADD8E6", font=("Helvetica", 12))
instructions_label.pack(pady=10)

# Create a text box for input (user inputs the text)
input_text = tk.Text(root, height=3, width=50, font=("Helvetica", 12), bg="#ffffff", fg="#000000")
input_text.pack(pady=10)

# Create a button to send the request
send_button = tk.Button(root, text="Send Request", command=send_request, font=("Helvetica", 12), bg="#4CAF50", fg="white")
send_button.pack(pady=10)

# Create a label for the response
response_label = tk.Label(root, text="Response from Gemini:", bg="#ADD8E6", font=("Helvetica", 12))
response_label.pack(pady=10)

# Create a text box for displaying the response
response_text = tk.Text(root, height=15, width=50, font=("Helvetica", 12), bg="#ffffff", fg="#000000")
response_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
