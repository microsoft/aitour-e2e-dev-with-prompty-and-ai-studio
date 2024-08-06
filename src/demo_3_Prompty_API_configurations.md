# Configuring your Azure OpenAI Service API

## Step 1: Edit Deployment Settings
Access Deployment: Click on the GPT-4 deployment on the bottom right side of the screen.
Edit Settings: Navigate to settings and switch to JSON view.
Add Credentials: Input the necessary credentials, including endpoint, deployment details, and API key.

## Step 2: Use Environment File (.env)
1. Create .env File: Create a new .env file in your project directory.
1. Add Parameters: Include the following parameters in the .env file:

```
OPENAI_API_VERSION = 
OPENAI_CHAT_DEPLOYMENT_NAME = 
OPENAI_ENDPOINT = 
OPENAI_API_KEY =
```

## Step 3: Update Prompt Key

Point to Environment Variables: Update your prompt key configuration to use environment variables. Use the following syntax to reference environment variables: ``$ENVIRONMENT_VARIABLE_NAME``

## Step 4: Run Configuration
1. Execute Configuration: Run your configuration to see if it is successful.
1. Verify Output: Ensure that the output is as expected.