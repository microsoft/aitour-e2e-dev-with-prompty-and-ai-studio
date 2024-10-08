# Prompty and Python

## Step 1: Edit the Prompty File
1. Let's start by opening your existing ``basic.prompty`` file.
1. Edit the model parameters by adding ``response_format`` set the response format type as a ``json_object``

``` json
parameters:
  max_tokens: 3000
  temperature: 0.7
  reponse_format:
    type: json_object
```
3. In the description, add the snippet below to generate an outdoors joke related to the question.

```
Add an outdoorsy joke, starting with "By the way, ". Don't address the customer's name for the joke portion of the response.
The joke should be directly related to the specific question asked.
For example, if the question is asking about hiking, the joke should be related specifically to hiking.

Before sharing the joke, mention you are providing a joke to motivate the user to explore the great outdoors

Respond with a json object like
{
  reponse:
  joke:
}
```
## Step 2: Add Prompty to Code
1. Right-Click on Prompty File and select: ``add Prompty Code`` 
1. This will generate a code snippet in Python, observe the generated code.
1. Repeat the same for: ``add Semantic Kernel Code``, ``add LangChain code`` and ``add Prompt flow code``

Our session will be focussed on the Python code generated.

## Step 3: Getting started with Python
> [!TIP]
> You can create a python virtual environment to install and run the dependancies

1. In the ``requirements.txt`` file we have required libraries.
```
promptflow
azure-identity
prompty[azure]
```
2. Install Dependencies: Open the terminal and run the following command to install the dependencies: ``pip install -r requirements.txt``


## Step 4: Run the Python code
Run the Python file in terminal, ensure the output is in the desired JSON format with the joke included.