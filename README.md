# Tiny-Troupe
# Question 1: How to install Tinytroupe packages 
# Step 1: Open a terminal from Codespace on Github. In the terminal, we need to run the following command to clone the repository:

git clone https://github.com/microsoft/tinytroupe
Change directory into the tinytroupe folder:

cd tinytroupe
# Installing the tinytroupe packages with following command:

pip install .

# Step 2: Setup API Key
In the terminal that you just installed packages, use the following command to setup API Key:

export OPENAI_API_KEY="xxxx"

# Question 2: What is Turing Test? In today's world with Large Language Models (LLMs), what is the definition of Turing Test?
The Turing Test, created by the brilliant mathematician Alan Turing in 1950, is basically a way to figure out if a machine can think like a human. Imagine you're having a conversation with someone, but you can't see them or hear their voice—it's all text-based. In the original test, you'd be chatting with both a human and a machine, and the goal is to see if you can tell who's who. If you can't tell the machine from the human based on their responses, then the machine has "passed" the Turing Test.

Now, with today's Large Language Models (LLMs) like GPT-4, the Turing Test still applies, but there's a bit more to consider. These models can carry on conversations that sound pretty human-like, especially in short exchanges. They can write essays, answer questions, tell stories, and even crack jokes, often fooling us into thinking we're talking to a person.

But here's the catch: while LLMs can sound human in many situations, they don't really understand what they're saying. They're just really good at predicting what words should come next based on patterns they've learned. So, if you keep talking to one of them long enough, you might notice that it starts to make weird mistakes, lacks emotional depth, or can't carry on a deep conversation without getting confused.

In today's world, the Turing Test isn't just about whether a machine can talk like a human; it's also about understanding how well it can handle complex conversations, emotions, and contexts that go beyond just spitting out words. It's still an important milestone, but now we know it doesn't necessarily mean the machine "thinks" the way humans do—it just knows how to talk like we do.

# Question 3: Create a simulation of your own topic and show me the transcript. This implies define at least two personas of your own choice with conflict built in and observe their conversation. You can simply copy/paste the conversation in a .md file. Please comment on the transcript whether you think the Turing Test is passed.

>>> from tinytroupe.examples import create_lisa_the_data_scientist
Looking for default config on: /workspaces/Tiny-Troupe/tinytroupe/tinytroupe/utils/../config.ini
Failed to find custom config on: /workspaces/Tiny-Troupe/tinytroupe/config.ini
Will use only default values. IF THINGS FAIL, TRY CUSTOMIZING MODEL, API TYPE, etc.

!!!!
DISCLAIMER: TinyTroupe relies on Artificial Intelligence (AI) models to generate content. 
The AI models are not perfect and may produce inappropriate or inacurate results. 
For any serious or consequential use, please review the generated content before using it.
!!!!


=================================
Current TinyTroupe configuration 
=================================
[OpenAI]
api_type = openai
azure_api_version = 2023-05-15
model = gpt-4o-mini
max_tokens = 4000
temperature = 1.2
freq_penalty = 0.0
presence_penalty = 0.0
timeout = 60
max_attempts = 5
waiting_time = 1
exponential_backoff_factor = 5
embedding_model = text-embedding-3-small
cache_api_calls = False
cache_file_name = openai_api_cache.pickle
max_content_display_length = 1024

[Simulation]
rai_harmful_content_prevention = True
rai_copyright_infringement_prevention = True

[Logging]
loglevel = ERROR

>>> lisa_ds = create_lisa_the_data_scientist()
>>> lisa_ds.listen_and_act("Tell me about your life.")
USER --> Lisa Carter: [CONVERSATION] 
          > Tell me about your life.
Lisa Carter acts: [THINK] 
                 > I need to share about my life, including my background, education, and current
                 > job. I should also mention my interests and personal life.
Lisa Carter acts: [TALK] 
                 > Sure! I grew up in Vancouver, Canada, in a tech-savvy family. My parents were
                 > software engineers, which inspired my interest in technology from a young age. I
                 > pursued a Master's in Data Science at the University of Toronto, focusing on
                 > improving search relevance using context-aware models. Now, I work as a Data
                 > Scientist at Microsoft in the M365 Search team, where I analyze user behavior to
                 > enhance search results. I also enjoy cooking, playing the piano, and watching
                 > movies in my free time.
Lisa Carter acts: [DONE] 

>>> from tinytroupe.agent import TinyPerson
>>> bhairavi = TinyPerson("Bhairavi")
>>> bhairavi.define("age", 24)  
>>> bhairavi.define("nationality", "Indian")
>>> bhairavi.define("occupation", "She is a Data Science Grad student at university.")
>>> bhairavi.listen_and_act("Tell me about yourself.")
USER --> Bhairavi: [CONVERSATION] 
          > Tell me about yourself.
Bhairavi acts: [THINK] 
              > I need to introduce myself. I should mention my name, age, nationality, and what I'm
              > currently doing.
Bhairavi acts: [TALK] 
              > My name is Bhairavi, I'm 24 years old, and I'm from India. I'm currently a Data
              > Science graduate student at university. I'm really passionate about data and how it
              > can be used to solve real-world problems.
Bhairavi acts: [DONE] 

>>> mike = TinyPerson("Mike")
>>> mike.define("age", 35)  
>>> mike.define("nationality", "American")
>>> 
>>> mike.define("occupation", "He is a Machine Learning professor in a university.")
>>> from tinytroupe.environment import TinyWorld
>>> world = TinyWorld("Classroom", [bhairavi, mike])
>>> world.make_everyone_accessible()
>>> mike.listen("I want more explaination on Decision Trees and want extension for homework")
USER --> Mike: [CONVERSATION] 
          > I want more explaination on Decision Trees and want extension for homework
TinyPerson(name='Mike')
>>> world.run(3) 
──────────────────────────────────────────────────────────────────── Classroom step 1 of 3 ────────────────────────────────────────────────────────────────────
Bhairavi acts: [THINK] 
              > I should wait for a response or a follow-up question. It's important to be attentive
              > and ready to engage further in the conversation.
Bhairavi acts: [DONE] 

Bhairavi --> Mike: [CONVERSATION] 
              > My name is Bhairavi, I'm 24 years old, and I'm from India. I'm currently a Data
              > Science graduate student at university. I'm really passionate about data and how it
              > can be used to solve real-world problems.
Mike acts: [TALK] 
          > Hi Bhairavi! It's great to meet you. Decision Trees are a popular method in machine
          > learning for classification and regression tasks. They work by splitting the data into
          > subsets based on the value of input features, creating a tree-like model of decisions.
          > Would you like me to explain how they work in more detail or provide some examples?
Mike acts: [THINK] 
          > Bhairavi is interested in Decision Trees and wants more explanation. I should provide a
          > clear and concise explanation, possibly with an example to help her understand better. I
          > also need to think about how to extend her homework related to this topic.
Mike acts: [TALK] 
          > To extend your homework, you could try implementing a Decision Tree from scratch using a
          > programming language like Python. This will help you understand the underlying mechanics
          > better. Would you like some guidance on how to start that?
Mike acts: [DONE] 

Mike --> Bhairavi: [CONVERSATION] 
          > Hi Bhairavi! It's great to meet you. Decision Trees are a popular method in machine
          > learning for classification and regression tasks. They work by splitting the data into
          > subsets based on the value of input features, creating a tree-like model of decisions.
          > Would you like me to explain how they work in more detail or provide some examples?
Mike --> Bhairavi: [CONVERSATION] 
          > To extend your homework, you could try implementing a Decision Tree from scratch using a
          > programming language like Python. This will help you understand the underlying mechanics
          > better. Would you like some guidance on how to start that?
──────────────────────────────────────────────────────────────────── Classroom step 2 of 3 ────────────────────────────────────────────────────────────────────
Bhairavi acts: [THINK] 
              > Mike is suggesting I implement a Decision Tree from scratch in Python. This sounds
              > like a great idea to deepen my understanding. I should consider asking for guidance
              > on how to start this project.
Bhairavi acts: [TALK] 
              > Yes, I would love some guidance on how to start implementing a Decision Tree in
              > Python! It sounds like a valuable exercise to understand the mechanics better.
Bhairavi acts: [THINK] 
              > I should consider what specific aspects of Decision Trees I want to learn about.
              > Maybe I can ask Mike about the best resources or libraries to use in Python for this
              > implementation.
Bhairavi acts: [DONE] 

Bhairavi --> Mike: [CONVERSATION] 
              > Yes, I would love some guidance on how to start implementing a Decision Tree in
              > Python! It sounds like a valuable exercise to understand the mechanics better.
Mike acts: [THINK] 
          > Bhairavi is eager to learn how to implement a Decision Tree in Python. I should provide
          > a step-by-step guide that includes setting up the environment, importing necessary
          > libraries, and writing the code for a simple Decision Tree model.
Mike acts: [TALK] 
          > Great! To start implementing a Decision Tree in Python, you'll need to have Python
          > installed on your computer along with some libraries like `pandas` for data manipulation
          > and `scikit-learn` for building the Decision Tree model. Here’s a simple outline to get
          > you started: 1. Install the necessary libraries using pip: `pip install pandas scikit-
          > learn`. 2. Import the libraries in your Python script: `import pandas as pd` and `from
          > sklearn.tree import DecisionTreeClassifier`. 3. Load your dataset using
          > `pd.read_csv('your_dataset.csv')`. 4. Split your data into features and target
          > variables. 5. Create a Decision Tree model using `model = DecisionTreeClassifier()`. 6.
          > Fit the model with your data using `model.fit(X_train, y_train)`. 7. Finally, you can
          > make predictions using `predictions = model.predict(X_test)`. Would you like me to
          > elaborate on any specific step?
Mike acts: [DONE] 

Mike --> Bhairavi: [CONVERSATION] 
          > Great! To start implementing a Decision Tree in Python, you'll need to have Python
          > installed on your computer along with some libraries like `pandas` for data manipulation
          > and `scikit-learn` for building the Decision Tree model. Here’s a simple outline to get
          > you started: 1. Install the necessary libraries using pip: `pip install pandas scikit-
          > learn`. 2. Import the libraries in your Python script: `import pandas as pd` and `from
          > sklearn.tree import DecisionTreeClassifier`. 3. Load your dataset using
          > `pd.read_csv('your_dataset.csv')`. 4. Split your data into features and target
          > variables. 5. Create a Decision Tree model using `model = DecisionTreeClassifier()`. 6.
          > Fit the model with your data using `model.fit(X_train, y_train)`. 7. Finally, you can
          > make predictions using `predictions = model.predict(X_test)`. Would you like me to
          > elaborate on any specific step?
──────────────────────────────────────────────────────────────────── Classroom step 3 of 3 ────────────────────────────────────────────────────────────────────
Bhairavi acts: [THINK] 
              > Mike provided a detailed outline for implementing a Decision Tree in Python. I need
              > to think about which step I want to ask him to elaborate on. The initial steps seem
              > clear, but I might need more information on how to split the data or fit the model.
Bhairavi acts: [TALK] 
              > Could you elaborate on how to split the data into features and target variables? I'm
              > a bit unsure about that step.
Bhairavi acts: [THINK] 
              > I need to wait for Mike's response regarding how to split the data into features and
              > target variables. It's important to be patient and attentive to his explanation.
Bhairavi acts: [DONE] 

Bhairavi --> Mike: [CONVERSATION] 
              > Could you elaborate on how to split the data into features and target variables? I'm
              > a bit unsure about that step.
Mike acts: [THINK] 
          > Bhairavi is unsure about how to split the data into features and target variables. I
          > need to explain this step clearly, emphasizing the importance of identifying which
          > columns in the dataset represent the input features and which one is the target
          > variable.
Mike acts: [TALK] 
          > To split your data into features and target variables, you first need to identify which
          > column in your dataset is the target variable (the one you want to predict) and which
          > columns are the features (the inputs used for prediction). For example, if you have a
          > dataset with columns like 'Age', 'Salary', and 'Purchased', and you want to predict
          > whether someone purchased a product, 'Purchased' would be your target variable. You can
          > split the data using pandas like this:   ```python X = data[['Age', 'Salary']]  #
          > Features Y = data['Purchased']        # Target variable ```  This way, `X` contains the
          > features and `Y` contains the target variable. Would you like to know more about how to
          > handle categorical variables or any other specific aspect?
Mike acts: [DONE] 

Mike --> Bhairavi: [CONVERSATION] 
          > To split your data into features and target variables, you first need to identify which
          > column in your dataset is the target variable (the one you want to predict) and which
          > columns are the features (the inputs used for prediction). For example, if you have a
          > dataset with columns like 'Age', 'Salary', and 'Purchased', and you want to predict
          > whether someone purchased a product, 'Purchased' would be your target variable. You can
          > split the data using pandas like this:   ```python X = data[['Age', 'Salary']]  #
          > Features Y = data['Purchased']        # Target variable ```  This way, `X` contains the
          > features and `Y` contains the target variable. Would you like to know more about how to
          > handle categorical variables or any other specific aspect?

# Comment on wether the turing test is passes or not: 
In this case, Mike, as a TinyPerson AI, is engaging in a conversation with Bhairavi (another TinyPerson), giving explanations and responding with helpful advice.
Based on the dialogue:

The AI (Mike) responds naturally to Bhairavi's questions, providing detailed, human-like explanations.

The AI knows how to guide Bhairavi through a technical concept (Decision Trees in Python) and engages in back-and-forth conversation that feels coherent.

The AI also adjusts based on Bhairavi's responses, continuing the conversation appropriately.

While the conversation feels natural, the AI isn’t really “understanding” things the way a human would. It's just following patterns and rules to respond. It can have a smooth back-and-forth, but it lacks real awareness, emotional depth, or deeper thinking. So, while it might seem human-like in basic tasks, it doesn't pass the Turing Test in a deeper sense because it doesn't truly "think" or "feel" like a person does.
In short, while this conversation might pass the Turing Test in a casual, task-oriented scenario (where the focus is on a specific question and answer format), it wouldn't pass it in the sense of "human-like thinking," as the AI lacks true understanding, consciousness, or emotional intelligence. So, it might pass a superficial Turing Test but not a deeper one.



