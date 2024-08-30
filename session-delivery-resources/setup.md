# TO-DO - setup

## Setting up Azure AI Studio

Follow the steps below to setup your Azure AI Studio environment:

1. Navigate to [Azure AI Studio](https://ai.azure.com) and login with your Azure account, once logged in, create a new project.

![](./demos/images/aistudio-landing-page.png)

2. Create a new project, you will also be prompted to create a new hub that will host your project.

![](./demos/images/aistudio-newproject.png)

3. Once you have successfully created your project, navigate to the deployments tab and deploy your Azure Open AI models i.e. ``GPT-4o`` and ``GPT-4``

![](./demos/images/aistudio-newmodel.png)

You are now ready to start the first demo on the introduction to Azure AI Studio and LLMs.

## Setting up your local Visual Studio Code

1. Install the [Prompty Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.prompty)

1. Log in to your Azure account using ``az login`` on the terminal. (You can also use ``az login --use-device-code``.)

3. Edit ``settings.json`` file to update your LLM details. You can edit this by navigating to ``settings > Extensions > Prompty > Edit in settings.json``

![Screeenshot of ](./demos/images/vscode-settings.png)

4. Update your credentials and settings.

![Screeenshot of ](./demos/images/vscode-settings-json.png)

> [TIP!]
> In case you encounter any challenges with permissions, you can follow the instructions for [Role-based access control for Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/role-based-access-control) to give access to your resources.
