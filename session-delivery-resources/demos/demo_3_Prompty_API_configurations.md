# Configuring your Azure OpenAI Service API

Prompty allows you to configure your API either using environmental variables or through ``settings.json``

## Option 1: Edit Deployment Settings (recommended)
 1. Access Deployment: Click on the ```default`` text on the bottom right side of the screen.

![screenshot of the default text on Visual Studio Code](images/prompty-default.png)

2. Navigate to settings and switch to JSON view.
3. Input the necessary credentials, including endpoint and deployment details. Add ``api_key`` but leave it blank

4. On your terminal, log in to your Azure account using ``az login --use-device-code`` to authenticate your connection.

## Option 3: Use Environment File (.env) - not recommended
1. Create a new ``.env`` file in your project directory.
2. Add Parameters: Include the following parameters in the .env file:

```
OPENAI_API_VERSION = 
OPENAI_CHAT_DEPLOYMENT_NAME = 
OPENAI_ENDPOINT = 
OPENAI_API_KEY =
```
3. Update your Prompty model configuration to use environment variables. Use the following syntax to reference environment variables: ``${env:ENVIRONMENT_VARIABLE_NAME}``

## Step 4: Run Configuration
1. Run your Prompty file to see if it is successful.
2. Ensure that the output is as expected.