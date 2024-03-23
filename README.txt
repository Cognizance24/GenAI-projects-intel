Educational Platform Application
This project is an educational platform developed with Flask, integrating various functionalities including user authentication, course enrollment and progress tracking, and a chatbot interface for answering user queries. Below you will find instructions on how to set up and run the application, along with a description of its features.

Features
User registration and login with password encryption.
Course enrollment and progress tracking.
A chatbot interface for interacting with users via text or speech.
A books interface, accessible at a specific URL, for searching and browsing books. (Note: This requires an external service running Gradio on localhost:7861).
A predictive feature to forecast course completion based on study habits and provide suggestions for improvement.
Prerequisites
Python 3.6+
MongoDB
Flask, Flask-PyMongo, Flask-Bcrypt for the web framework and database interaction.
Hugging Face's transformers and gradio libraries for the chatbot interface.
librosa for audio processing in the chatbot.
datasets library to load and use datasets.
daal4py for efficient data analytics.
PyTorch, torchaudio, and Intel Extension for PyTorch (ipex) for advanced machine learning functionalities.

Setup
Clone the repository: First, clone this repository to your local machine.

Install dependencies: Install the required Python packages by running the following command:

bash
Copy code
pip install -r requirements.txt
This command assumes that you have a requirements.txt file listing all the necessary packages.

MongoDB: Ensure MongoDB is installed and running on your system. The application expects MongoDB to be accessible at mongodb://localhost:27017/EducationalPlatform.

Environment Variables: The application uses a secret key for Flask sessions. It's generated dynamically in this code but for a production environment, you should set it to a fixed value in the environment variables.

Running the Application
To start the application, navigate to the project directory in your terminal and run:

bash
Copy code
python app.py
This will start the Flask server, and the application will be accessible at http://localhost:5000.

Using the Application
Steps to execute:

# a. Register in Intel Developer Cloud
  1.Go to Intel Developer Cloud: https://cloud.intel.com/
  2.Click Get Started
  3.Subscribe to “Standard” service tier and complete cloud registration
  4.Select “Cloud Credits”
  5.Select “Redeem coupon”
  6.Enter your Intel Developer Cloud code provided to setup a bare metal server instance.

# b. Setup an instance 
  # 1.Setup a conda environment after you access the instance 

    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh

    ~/miniconda3/bin/conda init bash

  # 2.Install the dependencies and library packages required to run the application

  Command:  pip install huggingface_hub gradio 

  # 3. Open a .py file and copy the code or upload the .py file

  # 4. Use the following command below :

  curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok- 
  agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok

  This command is a one-liner that installs `ngrok` on a Linux system. It's a sequence of commands combined using `&&` operator, which means 
  the next command will only run if the previous command succeeds. Let's break it down:
  `curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null`

   This command downloads the GPG key for the ngrok package from the ngrok-agent S3 bucket using `curl`. The `-s` option makes curl silent, 
   so it doesn't show progress or error messages. The downloaded key is then piped (`|`) into the `sudo tee 
   /etc/apt/trusted.gpg.d/ngrok.asc` command, which writes the key into the `/etc/apt/trusted.gpg.d/ngrok.asc` file. The `>/dev/null` part 
  discards the standard output of the `tee` command, so it doesn't clutter your terminal.

  `echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list`

   This command adds the ngrok repository to your APT sources. The `echo` command prints the string, which is then piped into `sudo tee 
  /etc/apt/sources.list.d/ngrok.list`, creating a new file `ngrok.list` in the `/etc/apt/sources.list.d/` directory with the ngrok 
  repository information.

  `sudo apt update`

   This command updates the package lists for upgrades and new package installations from the repositories defined in your system, including 
   the ngrok repository we just added.

   `sudo apt install ngrok`

   This command installs the ngrok package.

   In summary, this command sequence is adding the ngrok repository to your system's package manager, updating the package list, and then 
   installing ngrok.

  # 5.Use the following command:

    ngrok config add-authtoken <authtoken>

  # 6. Open another terminal 
  
    Use the following command 

    ngrok http 7860 

    The command `ngrok http 7860` is used to expose a local web server to the internet. 



Or if You want To Run In local Machine 

Steps to Execute:-
1.	Install the libraries
2.	Copy the code in Python IDE
3.	Run and Execute The code

Video is provided to show how to use in the drive link provided below

https://drive.google.com/drive/folders/12gMuYiPEifqRr9Tb7V02yip7VrXcT6x9?usp=sharing
