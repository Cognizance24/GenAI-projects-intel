
# Skin Diseases Analysis 
### Using CNN Model trained on IDC with help of OneAPI Tensorflow Extension (ITEX) + LLAMA-2 LLM Model running on Intel Xeon Processor Instance  

<br />

### Team - Akatsuki 
### Members - Shubham Tiwary & Rajat Balyan


<br />


## Problem Statement 

Skin diseases are pervasive health concerns affecting millions of individuals worldwide, posing significant challenges in diagnosis and treatment.
<br />
Despite advances in medical science, the accurate and timely identification of various skin conditions remains a considerable obstacle, leading to delayed interventions, misdiagnoses, and prolonged suffering for patients. 
<br />
Therefore, this Solution aims to develop robust ML & LLMsmodels capable of accurately identifying and classifying different skin diseases, as well as further providing symptoms and suggestions for encouraging further diagnosis with a medical professional.


<br />


## Breaking Down the Components

> [!IMPORTANT]
> The CNN and LLM Models are hosted on top Intel VMs via a Backend Server(`FastAPI`) and linked with Client Side(`Streamlit`) using Port Forwarding (`NGROK`), accessible with `Requests` 
>> To Check out in detail the Server Side Components: [Server Side Documentations](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/tree/main/server#hosted-on-intel-xeon-processor-vm-instance-on-a-python-fastapi-web-serverrunning-on-vms-localhost-with-ngrokport-forward-for-web-server)

<h4>1. Image Classification CNN Model</h3>

 -  The CNN Model acts as a first step multi-label classification via open source Skin Diseases datasets.
 -  Trained on `Intel Developer Cloud (IDC)` provided Next Gen `Intel Xeon-based Premium CPUs` with oneAPI Toolkit such as:  `ITEX`:  Intel OneAPI Extensions for Tensorflow
  

<br />

<h4>2. LLM (RAG) based Symptom Checker & Recommendation </h3>

- Further symptom checking process is passed on using a LLM Model that Processes Medical Books & Documents, Generating smart information on the suspected disease
- Using Open Source `Meta/LLAMA-2(7B) Model` running on `4th Gen Intel Xeon VM`
- Stores Contents from Books onto a VectorDB by Text Splitting + Storing the Vector Embeddings and then use a Retriever to Generate Responses from Queries





<br />


## Worflow Diagram

![psflow (1)](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/assets/67773966/119bb549-5a86-4025-bc68-3c808414aa97)




<br />


## Tech Stacks, Tools and Frameworks

 - `Streamlit` -> Interface
 - `FastAPI + Ngrok on Intel VM` -> Backend
 - `Tensorflow + ITEX on IDC` -> CNN Model (Deep Learning)
 - `Ctransformers + ChromaDB + Langchain ` -> LLM 





<br />


## Running the Application 

> For Setting up your own Server Side Component for this project in Intel Xeon Processor VM:  [Server Side Setup Documentations](https://github.com/ShubhamTiwary914/SkinDiseasesDiagnosis-IntelHackathon/tree/main/server#hosted-on-intel-xeon-processor-vm-instance-on-a-python-fastapi-web-serverrunning-on-vms-localhost-with-ngrokport-forward-for-web-server)

<br /><br />


1. Clone the Repository
```
  git clone https://github.com/ShubhamTiwary914/skinDiseasesCNN-IIT.git
```

2. Create & Activate Conda Environment 
```
  conda create --name <env-name> python=3.9
  conda activate <env-name>
```

2. Install the Dependencies
```
  cd skinDiseasesCNN-IIT
  pip install -r clientlibs.txt
```

3. Run the Application (Using Streamlit)
```
  streamlit run client.py
```



> [!NOTE]
> For Testing the Application, images to use as test input are provided in the `testImages` folder, feel free to use any other images available on the web


<br />


## Screenshots

![image](https://github.com/ShubhamTiwary914/skinDiseasesCNN-IIT/assets/67773966/ae714f72-c987-48ee-bff0-d1645fb537a7)


![image](https://github.com/ShubhamTiwary914/skinDiseasesCNN-IIT/assets/67773966/8914885f-44d2-4e8d-b3be-bb811c1acf3a)


![image](https://github.com/ShubhamTiwary914/skinDiseasesCNN-IIT/assets/67773966/bd99cdef-1638-4a92-880f-1788d8530f87)



