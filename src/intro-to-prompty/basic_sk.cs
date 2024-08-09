
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.OpenAI;

var deployment = "gpt-4o";
var endpoint = "";
var key = "aoai_key";
var kernel = Kernel.CreateBuilder()
    .AddAzureOpenAIChatCompletion(deployment, endpoint, key)
    .Build();

    // update the input below to match your prompty
    KernelArguments kernelArguments = new()
    {
        { "question", "what's my question?" },
    };

var prompty = kernel.CreateFunctionFromPromptyFile("basic.prompty");
var result = await prompty.InvokeAsync<string>(kernel, kernelArguments);
Console.WriteLine(result);
