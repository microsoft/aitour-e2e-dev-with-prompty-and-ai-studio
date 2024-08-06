# Getting Started with Prompty

I can liken Prompty to the AI Studio playground. Prompty is an asser class format for LLMs that provides observability, understandability and portability for developers.

## Step 1: Install the Prompty extension
1. Open Visual Studio Code (VS Code).
1. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window.
1. Search for “Prompty” and install the extension.

## Step 2: Create a new Prompty file
1. Once the extension is installed, go to your files in VS Code.
1. Right-click and select “New File”. A new file with a .prompty extension will be created.

## Step 3: Edit the Prompty file

The Prompty file consists of two main parts: Metadata in yaml and System Message in Markdown with templating.

### Update Metadata

1. Name: Change the name of your prompt file to ``OutdoorsyPrompt``
1. Description: Keep the description as it is.
1. Author Name: Update the author name to your name.
1. Model: Specify the model you are using. For example, chat for the Chat API.
1. Model Configuration:
    1. Use an AOP model.
    1. Update the endpoint link (if you don’t have an .env file, add the link directly).
    1. Specify the deployment, e.g., GPT-4.0.
    1. Parameters:
        1. Set maximum tokens to 3000.
        1. Add temperature and set it to 0.7.
1. Sample Data
    1. First Name: Update it to your name.
    1. Context: Provide more details about the context.
    1. User Question: Specify the question the user will ask.

## System Instructions
Add system instructions in Markdown format.Use the preview feature in VS Code to visualize how it looks.

## Step 4: Run the Prompty File
1. Run the file to get a response based on the question.
1. The response should include personalized details, such as your name.