# Creating and evaluating prompts with Prompty

## Step 1: Create a New Prompty

Configuration: Keep the configuration and response format as JSON.
Define Inputs: Define your inputs as strings, depending on your requirements.
Use a Joke: Use a joke from a previous query. For example, “Why don’t tents ever get lost in the woods?”

## Step 2: Describe and Evaluate the Joke

Description: Provide a description around the joke.
Evaluation Metrics: Score the joke based on its relevance to the main intent:
1: Unrelated
2: Somewhat related
3: Directly related
Response Format: The response should be JSON, including the score and reasoning.

## Step 3: Provide Examples

Score Examples: Show examples of how each score (1, 2, 3) should look.

## Step 4: Get the Query and Joke

Query: Retrieve the user’s query.
Joke: Retrieve the joke based on the query and give it a score and reasoning.

## Step 5: Run Prompty Code

Run Code: Execute the Prompty code to get the joke’s score and reasoning.

## Step 6: Add Prompty to the Flow

Print Outputs: Print the output of the response to the question and the joke.
Add Path: Add the path to Prompty in the prom flow.
Load Prompty: Use prompty.load and add the path to Prompty.

## Step 7: Define Result

Inputs: Define the inputs for the evaluation Prompty (query and joke).
Get Output: Use result.jck to get the output and print the evaluation result.

## Step 8: Run Prom Flow

Run Flow: Execute the prom flow and handle any errors.
Debug: If an error occurs, use a debugger to identify and fix the issue.