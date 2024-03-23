# Interactive Storyteller with Text-to-Text and Text-to-Image Models

Welcome to our GitHub repository for the Interactive Storyteller project! In this project, we leverage the power of text-to-text and text-to-image large language models to create immersive and interactive stories.

## Overview

Our pipeline involves the following steps:

1. *Input Collection*: Users provide brief inputs about characters, plot, and theme of the story.

2. *Text-to-Text Story Generation*: Using text-to-text large language models, we generate the story based on the provided inputs. The model crafts a narrative that unfolds based on the characters, plot, and theme provided by the user.

3. *Story Division*: The generated story is divided into pivotal sections, ensuring that each section captures a significant moment or development in the narrative.

4. *Text-to-Image Generation*: Each pivotal section of the story is fed into a text-to-image model to generate corresponding images. These images help visualize key scenes and characters from the story.

5. *User Interaction*: Users have the opportunity to review the story. If satisfied, they can proceed with enjoying the image narrative. If not, they can provide feedback on what to edit or improve in the story.

6. *Story Regeneration*: Based on user feedback, the story may undergo regeneration, incorporating suggested edits or improvements. This iterative process ensures that the final story meets the user's expectations.

## Repository Structure

- Contains the jupyter notebook for the Interactive Storyteller project.
- Documentation files, including this README.
- Sample output images folder corresponding to the initial user prompt-
  Name of characters along with their description- Anna is pretty girl with long hair, short height  and  Peter is a handsome boy with short hair, blue eyes.
  Plot- The characters were in a relationship initially, but Peter cheated on Anna, Anna conspired to kill Peter.
  Theme- Romance, Thriller, Big City setting.
  ### Note- Since Text to Image models are still under research, very precise images werent produced, but we have tried to establish a sense of narrative coherence using audio playback when each image is shown.
## Usage

To use the Interactive Storyteller:

1. Clone the repository to your local machine.
2. Install the necessary dependencies as specified in the requirements.txt file.
3. Run the provided notebook.
4. Find the generated visual narrative in result folder created.

## Contributions

We welcome contributions from the community to enhance and expand the capabilities of the Interactive Storyteller. Whether you're interested in improving the story generation algorithms, optimizing the text-to-image models, or enhancing the user interface, your contributions are valuable.

Happy storytelling! 📚🖼
