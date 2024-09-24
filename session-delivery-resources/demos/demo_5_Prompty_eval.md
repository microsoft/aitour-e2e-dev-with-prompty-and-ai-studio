# Creating and evaluating prompts with Prompty

In this demo, we create a new Prompty to evaluate whether the joke is directly related to the question asked by the user.

## Step 1: EvalPrompty

1. Head over to the ``eval.prompty`` file.
1. In this file update the configuration endpoint and retain response format as JSON.
1. Next define your inputs, both of which are type ``string``. 
1. The sample input would be the user query and joke based on the query, as shown below:

```
sample:
  query: What can you tell me about your tents?
  joke: By the way, why don't tents ever get lost in the woods? Because they always stick to their roots! 🌲😄
```

## Step 2: Describe and Evaluate the Joke
In our system instructions provide a description around the joke and evaluation metrics. The evaluation metrics will score the joke based on its relevance to the main intent in three main categories with examples based on each category: 
    
- Unrelated
- Somewhat related
- Directly related

Lastly, the response should be JSON, including the score and reasoning. Execute the Prompty code to get the joke’s score and reasoning.

## Step 3: Add EvalPrompty to Python

1. First, print the output of the response to the question and the joke. Then get the joke from the output as follows:

```python
  print(result)
  joke = result.joke
```

2. Next add Prompty path to the flow using ``prompty.execute``

``` python
  # execute the prompty file
  eval = prompty.execute(
    "eval.prompty", 
    inputs={
      "joke": joke,
      "query": question
    }
  )

  return eval
```
3. Next, run the code. 
4. You will encounter an error which can be fixed using the debugger. Add a breakpoint to line 28, where there is an error. Run the code again. If everything works perfectly, you can fix the code at line 28 as follows: ```python
  # Extract the joke from the result
  joke = result["joke"]
  print("Joke: ", joke)
```

## Step 4: Run Python

The last step is to run the flow, it should return the joke, score and reasoning behind the score.