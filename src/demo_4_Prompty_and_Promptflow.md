# Prompty and PromptFlow

## Step 1: Edit the Prompty File
1. Open the Prompty File: Start by opening your existing Prompty file.
1. Add a Snippet: In the description, add a snippet to generate an outdoors joke related to the question.
1. Set Response Format: Edit the parameters to set the response format as a JSON object.

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
Right-Click on Prompty File: Right-click on the Prompty file.
Add to LangChain: Selangct the option to add it to LangChain.
Generate LangChain Code: Observe the generated LangChain code.
Add to Semantic Kernel: Similarly, add the Prompty file to the Semantic Kernel.
Generate Semantic Kernel Code: Observe the generated Semantic Kernel code.

## Step 3: Add Prompty to Proml Code
Add Prompty to Proml Code: Add the Prompty file to Proml code.
Install Necessary Libraries: Create a requirements.txt file and add the required libraries.
```
promptflow
azure-identity
```

Install Dependencies: Open the terminal and run the following command to install the dependencies.
``pip install -r requirements.txt``

## Step 4: Run the Prompty File
Run the Prompty File: Execute the Prompty file and expect similar results to your initial run.
Verify Output: Ensure the output is in the desired JSON format with the joke included.