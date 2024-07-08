# tiktok_sales
Effortlessly manage your sales tasks with AI-driven Smart Sales Helper, integrated seamlessly with Todoist for optimal productivity.
## Smart Sales Helper

Smart Sales Helper is an AI-driven web application designed to enhance the efficiency and productivity of sales teams. It leverages Azure OpenAI for intelligent response generation, Azure Speech for real-time speech recognition, and Todoist for task management integration.

### Table of Contents

- [Features](#features)
- [Built With](#built-with)
- [Installation](#installation)
- [Usage](#usage)
- [Inspiration](#inspiration)
- [What We Learned](#what-we-learned)
- [Challenges Faced](#challenges-faced)
- [License](#license)

### Features

- **Real-time Speech Recognition**: Converts speech to text using Azure's Speech SDK.
- **AI Response Generation**: Generates intelligent responses during sales calls using Azure OpenAI.
- **Task Management Integration**: Adds tasks to Todoist based on extracted to-do items from conversations.
- **Safeguard Check**: Ensures generated responses do not contain any to-be-avoided words or phrases.
- **Conversation Summarization**: Summarizes the conversation and speculates on user emotions and potential follow-up possibilities.
- **Sales Tips**: Provides learning tips based on successful sales strategies.
- **BI Analysis**: Generates business intelligence reports based on conversation and sales data.

### Built With

- **Python**
- **Flask**
- **todoist-api-python**
- **azure-cognitiveservices-speech**
- **openai**
- **spacy**
- **Azure**
- **Azure OpenAI**
- **Azure Speech Service**
- **Todoist API**
- **Azure Cognitive Services API**
- **Pandas**
- **Jupyter Notebook**
- **Git**

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/smart-sales-helper.git
cd smart-sales-helper
```

2. **Create and activate a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required packages**:

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
```

5. **Run the application**:

```bash
flask run
```

6. **Access the application**:

Open your web browser and navigate to `http://127.0.0.1:5000/`.

### Usage

- **Generate Response**: Enter a prompt and click "Generate Response" to get an AI-generated response.
- **Check Safeguard**: Enter phrases to avoid and click "Check Safeguard" to ensure the response does not contain these phrases.
- **Summarize Text**: Click "Summarize Text" to get a summary of the conversation.
- **Extract To-Dos**: Click "Extract To-Dos" to generate a to-do list from the conversation.
- **Generate Sales Tips**: Click "Generate Sales Tips" to get tips based on successful sales strategies.
- **Generate BI Report**: Enter BI data in JSON format and click "Generate BI Report" to get a business intelligence report.
- **Add to Todoist**: Enter your Todoist API token and click "Add to Todoist" to add tasks to your Todoist account.

### Inspiration

The inspiration for this project came from the need to enhance the efficiency and productivity of sales teams. Sales professionals often juggle multiple tasks, follow-ups, and client interactions, which can be overwhelming and lead to missed opportunities. By leveraging AI and integrating with popular task management tools like Todoist, we aimed to create a seamless and intelligent assistant that can streamline sales processes and improve overall performance.

### What We Learned

- **Integration of AI with Existing Tools**: How to effectively integrate AI capabilities with task management tools like Todoist to create a comprehensive solution.
- **Natural Language Processing**: The intricacies of using NLP to extract actionable items from conversations and generate meaningful summaries.
- **User Authentication and Security**: Ensuring secure handling of user tokens and sensitive information.
- **Error Handling and User Experience**: The importance of robust error handling and providing clear feedback to users to enhance their experience.

### Challenges Faced

- **API Integration**: One of the significant challenges was integrating different APIs seamlessly and ensuring smooth communication between them.
- **Accurate NLP**: Extracting precise to-do items from natural language conversations proved to be complex and required fine-tuning of the NLP models.
- **User Security**: Handling user tokens securely and ensuring that sensitive information was not exposed was crucial and required careful implementation.
- **Error Handling**: Ensuring robust error handling to provide clear and helpful feedback to users when something went wrong was essential for a smooth user experience.

