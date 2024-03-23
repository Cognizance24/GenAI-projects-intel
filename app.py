from threading import Thread
from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import os
from huggingface_hub import InferenceClient
import gradio as gr
from transformers import pipeline
import librosa
from datasets import load_dataset
import daal4py as d4p

try:
    import torch
    import torchaudio
    import intel_extension_for_pytorch as ipex
except ImportError:
    print("torchaudio is required. Install it with 'pip install torchaudio'.")

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/EducationalPlatform"
app.config["SECRET_KEY"] = os.urandom(24)

mongo = PyMongo(app)
bcrypt = Bcrypt(app)


def initialize_database():
    db = mongo.db
    if "students" not in db.list_collection_names():
        db.create_collection("students")


initialize_database()


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.students
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashed_pw = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            users.insert_one({
                'name': request.form['name'],
                'username': request.form['username'],
                'college_registration_number': request.form['college_registration_number'],
                'password': hashed_pw,
                'access_granted': True
            })
            flash('Registration successful!')
            return redirect(url_for('login'))

        flash('That username already exists!')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.students
        user = users.find_one({'username': request.form['username']})

        if user and bcrypt.check_password_hash(user['password'], request.form['password']):
            session['username'] = user['username']
            session['user_type'] = 'student'
            return redirect(url_for('index'))

        flash('Invalid username/password combination')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.')
    return redirect(url_for('login'))


@app.route('/update_password', methods=['GET', 'POST'])
def update_password():
    if 'username' in session:
        if request.method == 'POST':
            users = mongo.db.students
            user = users.find_one({'username': session['username']})
            if user and bcrypt.check_password_hash(user['password'], request.form['old_password']):
                new_password = bcrypt.generate_password_hash(request.form['new_password']).decode('utf-8')
                users.update_one({'username': session['username']}, {'$set': {'password': new_password}})
                flash('Password updated successfully.')
                return redirect(url_for('index'))
            flash('Old password is incorrect.')
        return render_template('update_password.html')
    return redirect(url_for('login'))


# Placeholder routes for other features
# @app.route('/predict-outcomes')
# def predict_outcomes():
#     return "Predict outcomes page (Under Construction)"
#
#
# @app.route('/books')
# def books():
#     return "Books page (Under Construction)"
#
#
# @app.route('/courses')
# def courses():
#     return "Opted Courses page (Under Construction)"


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', user_type='student')
    return redirect(url_for('login'))

def chatbot_interface():
    try:
        import torchaudio
    except ImportError:
        print("torchaudio is required. Install it with 'pip install torchaudio'.")

    # Initialize the Whisper model for speech-to-text conversion
    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

    # Initialize the InferenceClient for text generation with your AI model
    client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.1")

    def format_prompt(message, history=[]):
        prompt = "<s>"
        for user_prompt, bot_response in history:
            prompt += f"[INST] {user_prompt} [/INST]"
            prompt += f" {bot_response}</s> "
        prompt += f"[INST] {message} [/INST]"
        return prompt

    def generate(prompt, history=[], temperature=0.9, max_new_tokens=256, top_p=0.95, repetition_penalty=1.0):
        formatted_prompt = format_prompt(prompt, history)
        response = client.text_generation(formatted_prompt, temperature=temperature, max_new_tokens=max_new_tokens,
                                          top_p=top_p, repetition_penalty=repetition_penalty, do_sample=True,
                                          return_full_text=False)

        # Adjusted to handle different response structures
        if isinstance(response, str):
            output = response
        elif isinstance(response, list) and 'generated_text' in response[0]:
            output = response[0]['generated_text']
        elif isinstance(response, dict) and 'generated_text' in response:
            output = response['generated_text']
        else:
            output = "Failed to generate response. Please check the model response format."
        return output

    def process_audio(audio_file):
        y, sr = librosa.load(audio_file, sr=None)  # Load the audio file
        transcript = transcriber({"raw": y, "sampling_rate": sr})["text"]
        return transcript

    def handle_input(text_input, audio_input):
        if audio_input is not None:
            text_input = process_audio(audio_input)
        response = generate(text_input)
        return text_input, response

    def close_server():
        print("Closing the server...")
        gr.close_all()
    with gr.Blocks() as demo:
        with gr.Row():
            text_input = gr.Textbox(label="Type your question here", placeholder="Type here or use voice input...")
            audio_input = gr.Audio(label="Or speak your question here", type="filepath")
        submit_button = gr.Button("Submit")
        close_button = gr.Button("Close Server")
        output_text = gr.Textbox(label="You said:")
        output_response = gr.Textbox(label="AI Response:")

        submit_button.click(
            fn=handle_input,
            inputs=[text_input, audio_input],
            outputs=[output_text, output_response]
        )
        close_button.click(  # Define the action for the close_button
            fn=close_server,
            inputs=[],
            outputs=[]
        )

    demo.launch(share=True, inbrowser=True)
chatbot_interface()

# Ensure that the asyncio event loop is properly managed if this script is run standalone


dataset = load_dataset("biglam/blbooks-parquet")

# Functions to get a book, search for books, and list books
def get_book(index: int):
    try:
        book = dataset['train'][index]
        return f"Title: {book['title']}\nAuthor: {book['first_author']}\nDate of Publication: {book['pub_date']}"
    except IndexError:
        return "Book not found. Please enter a valid index."

def search_books(title_query: str):
    results = dataset['train'].filter(lambda x: title_query.lower() in x['title'].lower())
    books = []
    for book in results:
        books.append(f"Title: {book['title']}, Author: {book['first_author']}, Date: {book['pub_date']}")
    return "\n".join(books[:5]) if books else "No books found with that title."

def list_books(start_index: int, end_index: int):
    if start_index < 0 or end_index >= len(dataset['train']) or start_index > end_index:
        return "Invalid index range. Please enter a valid range."
    books = [f"Index: {i}, Title: {book['title']}, Author: {book['first_author']}, Date: {book['pub_date']}"
             for i, book in enumerate(dataset['train'][start_index:end_index + 1])]
    return "\n".join(books)

# Gradio interface for book search
def launch_book_interface():
    iface = gr.Interface(
        fn={
            "Get Specific Book": get_book,
            "Search Books by Title": search_books,
            "List All Books in Range": list_books
        },
        inputs={
            "Get Specific Book": gr.Number(label="Book Index for Direct Access"),
            "Search Books by Title": gr.Text(label="Search Book by Title"),
            "List All Books in Range": [gr.Number(label="Start Index"), gr.Number(label="End Index")]
        },
        outputs=gr.Textbox(label="Results"),
        title="Navigate and Search Books",
        description="Enter a book index to get its details, search by title, or list all books within a specified index range."
    )
    iface.launch(share=True, inbrowser=True, server_name="0.0.0.0", server_port=7861)
def initialize_courses():
    db = mongo.db
    if "courses" not in db.list_collection_names():
        db.create_collection("courses")
        # Here, you'd typically populate your courses collection from an external dataset or another source
        # For demonstration, this step is skipped

initialize_courses()
dataset = load_dataset("Xuehang/hi_smartedu_courses_datasets")
courses_data = dataset['train']  # Assuming 'train' is the correct split

@app.route('/courses')
def courses():
    return render_template('courses.html', courses=courses_data)

@app.route('/enroll_course/<course_id>', methods=['POST'])
def enroll_course(course_id):
    if 'username' not in session:
        flash('Please login to enroll in courses.')
        return redirect(url_for('login'))

    # Simulate adding to a "database" by storing in session
    if 'enrolled_courses' not in session:
        session['enrolled_courses'] = []
    if course_id not in session['enrolled_courses']:
        session['enrolled_courses'].append(course_id)
        flash('Successfully enrolled in course.')
    else:
        flash('Already enrolled in this course.')
    return redirect(url_for('courses'))

@app.route('/update_progress', methods=['POST'])
def update_progress():
    if 'username' not in session or 'enrolled_courses' not in session:
        flash('Please login to update course progress.')
        return redirect(url_for('login'))

    course_id = request.form.get('course_id')
    progress = request.form.get('progress', type=int)

    # Assuming a more complex data structure for progress; simplifying for this example
    if 'progress' not in session:
        session['progress'] = {}
    session['progress'][course_id] = progress
    flash('Course progress updated.')
    return redirect(url_for('courses'))

@app.route('/view_progress')
def view_progress():
    if 'username' not in session:
        flash('Please login to view your courses and progress.')
        return redirect(url_for('login'))

    enrolled_courses = session.get('enrolled_courses', [])
    progress = session.get('progress', {})

    # Fetch course details for each enrolled course
    courses_info = [courses_data[int(course_id)] for course_id in enrolled_courses]
    for course in courses_info:
        course_id = str(course['id'])  # Assuming course ID is under the 'id' key
        course['progress'] = progress.get(course_id, 0)

    return render_template('view_progress.html', courses=courses_info)
@app.route('/chatbot')
def chatbot():
    # Launch the chatbot interface in a new thread to avoid blocking
    Thread(target=chatbot_interface).start()
    # Redirect user or inform them where to find the chatbot
    return "Please wait a moment for the chatbot interface to launch."
@app.route('/books')
def book_search():
    return redirect("http://localhost:7861", code=302)


@app.route('/predict-outcomes', methods=['GET', 'POST'])
def predict_outcomes():
    if request.method == 'POST':
        course_id = request.form.get('course_id', type=int)
        total_hours_required = request.form.get('total_hours_required', type=int)
        current_hours_spent = request.form.get('current_hours_spent', type=int)
        increase_hours = request.form.get('increase_hours', type=int, default=0)
        take_tests = request.form.get('take_tests', type=bool, default=False)

        predictor = CourseProgressPredictor(course_id, total_hours_required, current_hours_spent)
        remaining_hours = predictor.predict_completion_time()
        suggestions = predictor.suggest_improvements(increase_hours, take_tests)

        return render_template('predict_outcomes_result.html', remaining_hours=remaining_hours, suggestions=suggestions)

    return render_template('predict_outcomes.html')

if __name__ == '__main__':
    Thread(target=launch_book_interface).start()  # Launch Gradio in a background thread
    app.run(debug=True, use_reloader=False)  # Start Flask app
