# LinkedInk: AI-Powered Post Generator 🤖

Hey everyone! 👋,

Welcome to my new project LinkedInk 🚀.

LinkedInk is a powerful tool that leverages large language models (LLMs) to generate engaging and professional LinkedIn posts based on user input. With LinkedInk, you can effortlessly create captivating posts for various purposes, such as announcing a new job, showcasing a project, or celebrating an achievement.

## Technologies Used 🛠️
LinkedInk utilizes the following technologies:

- **LLM**: The project uses the llama-2-7b-chat.ggml model, a powerful language model trained by the team behind the Llama project. This model enables LinkedInk to understand natural language input and generate coherent and relevant LinkedIn post content.
- **Langchain**: LinkedInk leverages the Langchain library, which provides a framework for building applications with large language models. Langchain simplifies the process of interacting with LLMs and allows for easy integration and customization.
- **Streamlit**: The project is deployed as a web application using Streamlit, a Python library that allows for the rapid development and deployment of data-driven applications. Streamlit provides an intuitive user interface for users to input their post details and generate LinkedIn content.

## Installation 📥
To run LinkedInk locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/LinkedInk.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the llama-2-7b-chat.ggml model and place it in the `models` directory.

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
   This will start the LinkedInk application, and you should be able to access it in your web browser at [http://localhost:8501](http://localhost:8501).

## Usage 🚀
1. Enter the details you want to include in your LinkedIn post in the "Enter the post details" input field.
2. Specify the desired number of words for the post in the "No of Words" input field.
3. Select the type of post you want to generate from the "Make a post for" dropdown menu (e.g., new job, new project, new achievement).
4. Click the "Generate" button.
5. LinkedInk will process your input and generate a relevant LinkedIn post, which will be displayed on the page.
   
### Sample working:

<img width="700" alt="image" src="https://github.com/Sukrit-garg/LinkedInk/assets/101797008/1b5f2b8f-0c72-4394-96e7-3097cfe1ab44">

<img width="700" alt="image" src="https://github.com/Sukrit-garg/LinkedInk/assets/101797008/b66ea6f2-c329-4e19-8e70-497c982de159">



Feel free to experiment with different input parameters and post types to create a variety of engaging LinkedIn content using the power of AI.

## Contributing 🤝
Contributions to LinkedInk are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the project's GitHub repository.

## Acknowledgments🙌
LinkedInk wouldn't be possible without the incredible work done by the teams behind Llama, Langchain, and Streamlit. I extend my gratitude to these open-source projects and their contributors. Special thanks to Krish Naik for creating absolutely amazing tutorials for LLMs and end to end projects using various models.
