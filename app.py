from flask import Flask, request, jsonify
from transformers import pipeline, set_seed
from gtts import gTTS
from moviepy.editor import *
import torch
from diffusers import StableDiffusionPipeline

app = Flask(__name__)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    data = request.get_json()
    text = data.get('text', 'a girl lost in the woods')
    
    # Generate the story
    generator = pipeline('text-generation', model='gpt2-medium')
    set_seed(42)
    prompt = "generate a story on" + text
    max_length = 1080
    story = generator(prompt, max_new_tokens=max_length, truncation=True)[0]['generated_text']
    
    # Create narration from the story
    narration = gTTS(text=story, lang='en-us', slow=True, tld='com')
    narration.save("narration.mp3")
    audio = AudioFileClip("narration.mp3")
    duration = audio.duration

    # Generate images related to the story
    h = 800
    w = 640
    steps = 25
    guidance = 7.5
    neg = "easynegative,no repetation, lowres,partial view, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot,"
    num_images = int(duration / 10)
    for i in range(num_images):
        prompt = text  # Use the original text as the prompt
        image = pipe(prompt, height=h, width=w, number_inference_steps=steps, guidance_scale=guidance, negative_prompt=neg).images[0]
        image.save(f"image_{i + 1}.png")  # Save the image with a unique name

    # Create a blank video clip with the same duration as the audio
    video = ColorClip((1280, 720), color=(0, 0, 0), duration=duration)

    # Set the text for the video
    txt = story

    # Add the text clip to the video
    video = video.set_audio(audio)
    video = video.set_duration(duration)
    video = video.set_fps(24)
    video = video.set_audio(audio)
    video = video.set_duration(duration)
    video = video.set_fps(24)

    # Add images to the video
    image_clips = [ImageClip(f"image_{i + 1}.png").set_duration(duration / num_images) for i in range(num_images)]
    images_video = concatenate_videoclips(image_clips, method="compose")

    # Overlay the images video on top of the main video
    final_video = CompositeVideoClip([video.set_position(('center', 'center')), images_video.set_position(('center', 'center'))])

    # Write the final video to a file
    final_video_path = "story_video.mp4"
    final_video.write_videofile(final_video_path, codec='libx264', fps=24)

    return jsonify({"message": "Video generated successfully", "video_path": final_video_path})

if __name__ == '__main__':
    app.run(debug=True)
