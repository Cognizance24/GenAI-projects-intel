# Problem Statement

### Team leader Email : [Eklavya Kumar](eklavyakumarsingh100@gmail.com)
## Interactive story telling using Generative AI
Develop an innovative platform for interactive storytelling that employs AI-driven tools, allowing users to actively shape the plot and characters through their input using use of Intel®️ oneAPI as the primary programming paradigm.
The aim is to craft captivating visual narratives using advanced AI techniques such as Stable Diffusion or Gen AI models. 
The interactive storytelling experience is designed to immerse users in a personalized and distinctive narrative, facilitated by generative AI technology, fostering engagement and creativity.


## Intel OneAPI toolkit libraries used:
1. **Intel® oneAPI intel_extension_for_pytorch** : Optimizes PyTorch for Intel hardwares. It provides performance optimizations for a variety of PyTorch operations, including:
Operator optimizations, Graph optimizations &Runtime optimizations:
2. **Intel® oneAPI Math Kernel Library (oneMKL)**: Leverage oneMKL for optimized mathematical operations, improving the overall performance of machine learning algorithms and computations.

## Workflow 1:
![Workflow 1](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/SimpleStoryGenerator.png)

In this workflow we used a text to image generator stable diffusion model. 
The steps of the overall workflow is as follows:
1. User gives a prompt about the plot of the story and characters involved.
2. A creative story is generated using an LLM model (currently ChatGPT API) in about 1000-1500 words.
3. The story is splitted into different paragraphs of around 150-200 words.
4. Each paragraph is sent to the LLM model (currently using ChatGPT API) to generate a simple, straightforward and small size prompt defining the characters and surrounding\scenario of that paragraph.
   The LLM model is prompted to follow some rules inorder to generate this prompts so as to make it easier for stable diffusion model to generate images based on simple and small prompts describing the part of story in that paragraph
5. **LLM generated prompt** is sent to the Stable diffusion model to generate image for each part of story seperately.

## Workflow 2:
![Workflow 2](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/CoherentStoryGenerator.png)

In this workflow we used a image to image generator stable diffusion model. 
The steps of the overall workflow is as follows:
1. User gives a prompt about the plot of the story and characters involved.
2. A creative story is generated using an LLM model (currently ChatGPT API) in about 1000-1500 words.
3. The story is splitted into different paragraphs of around 150-200 words.
4. Each paragraph is sent to the LLM model (currently using ChatGPT API) to generate a simple, straightforward and small size prompt defining the characters and surrounding\scenario of that paragraph. The LLM model is prompted to follow some rules inorder to generate this prompts so as to make it easier for stable diffusion model to generate images based on simple and small prompts describing the part of story in that paragraph.
5. Each paragraph is sent to the LLM model again to give a integer number back (between 1-13) the number returned is used to **retrieve a base image** out of the 13 base images already saved in a folder. Each base image represent a location/surrounding in either daytime or nighttime. The LLM model infere from the paragraph what is the most probable/suitable location and day/night time the events described in that paragraph corresponds and return the appropriate number which is then used to retrieve that base image. This base image responsible to affect the colors of the image generated for this paragraph.
6. **Retrieved Base image & generated prompt** is sent to the image to image Stable diffusion model to generate image for each part of story seperately.

### Example of some base images used:
Base image corresponding to surrounding of a mountain in day time
![image 1](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/base/12.jpg)

Base image corresponding to surrounding of a sea in night time
![image 2](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/base/5.jpg)

## An example story generated using the above workflow:
**Prompt by the user** : A student with his friends in a school
![image 1](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/1.jpeg)
![image 1](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/2.jpeg)
![image 1](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/3.jpeg)
![image 1](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/4.jpeg)
![image 1](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/5.jpeg)

## Future Scope:
To incorporate open source LLM models instead of using ChatGPT API.
Improve the coherency of the images generated in workflow 2 by incorporating better base images/ developing another way of selecting the base images for each round.

## Video description:
[![Video](https://github.com/eklavyaK/GenAI_Hackathon/blob/master/images/Thumbnail.jpg)](https://www.youtube.com/watch?v=MAmnOYT1qhU)
