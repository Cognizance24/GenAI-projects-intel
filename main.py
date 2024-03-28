    from flask import Flask, request, jsonify, render_template
    from transformers import pipeline
    from diffusers import DiffusionPipeline
    import os

    app = Flask(__name__)

    # Load the pre-trained models
    text_generator = pipeline("text-generation", model="aspis/gpt2-genre-story-generation")
    text_to_image_model = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
    text_to_image_model.to("cpu")  # Switch to CPU

    # Define the directory where the images are saved
    IMAGE_DIR = "/home/sdp"

    @app.route('/')
    def index():
        return render_template('indextest.html')

    @app.route('/generate', methods=['POST'])
    def generate():
        try:
            # Get inputs from the frontend
            genre = request.form['genre']
            starter_text = request.form['starter_text']
            word_limit = int(request.form['word_limit'])

            # Construct the input prompt
            input_prompt = f"<BOS> <{genre.lower()}> {starter_text}"

            # Generate a story based on the input prompt
            story = text_generator(input_prompt, max_length=word_limit, truncation=True, do_sample=True,
                        repetition_penalty=1.5, temperature=1.2,
                        top_p=0.95, top_k=50)

            # Generate image based on the generated story
            images = text_to_image_model(prompt=story[0]['generated_text']).images[0]
            image_path = os.path.join(IMAGE_DIR, "generated_image.png")  # Path to save the image
            images.save(image_path)

            # Return the generated story and image path
            response = {
                'story': story[0]['generated_text'],
                'image_path': image_path  # Return the path to the image
            }
            return jsonify(response)
        except Exception as e:
            error_message = f"Error: {e}"
            print(error_message)
            return jsonify({'error': error_message}), 500

    if __name__ == '__main__':
        app.run(debug=True)
