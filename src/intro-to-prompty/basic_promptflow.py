import json

from pathlib import Path
folder = Path(__file__).parent.absolute().as_posix()

from promptflow.core import tool, Prompty

@tool
def flow_entry(    
      firstName: any,
      context: any,
      question: any
) -> str:
  # path to prompty (requires absolute path for deployment)
  path_to_prompty = folder + "/basic.prompty"

  # load prompty as a flow
  flow = Prompty.load(path_to_prompty)
 
  # execute the flow as function
  result = flow(
    firstName = firstName,
    context = context,
    question = question
  )

  print(result)
  joke = result["joke"]

  path_to_prompty = folder + "/eval.prompty"

  eval_prompty = Prompty.load(path_to_prompty)
  eval_result = eval_prompty(query=question, joke=joke)

  print("~~~Evaluation~~~")
  print(eval_result)

if __name__ == "__main__":
   json_input = '''{
  "firstName": "Bethany",
  "context": "The Alpine Explorer Tent boasts a detachable divider for privacy,  numerous mesh windows and adjustable vents for ventilation, and  a waterproof design. It even has a built-in gear loft for storing  your outdoor essentials. In short, it's a blend of privacy, comfort,  and convenience, making it your second home in the heart of nature!\\n",
  "question": "What can you tell me about your tents?"
}'''
   args = json.loads(json_input)

   result = flow_entry(**args)
   print(result)
