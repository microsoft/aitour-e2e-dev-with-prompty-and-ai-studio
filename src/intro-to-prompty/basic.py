import json
import prompty
# to use the azure invoker make 
# sure to install prompty like this:
# pip install prompty[azure]
import prompty.azure
from prompty.tracer import trace, Tracer, console_tracer, PromptyTracer

# add console and json tracer:
# this only has to be done once
# at application startup
Tracer.add("console", console_tracer)
json_tracer = PromptyTracer()
Tracer.add("PromptyTracer", json_tracer.tracer)

@trace
def run(    
      firstName: any,
      context: any,
      question: any
) -> str:

  # execute the prompty file
  result = prompty.execute(
    "basic.prompty", 
    inputs={
      "firstName": firstName,
      "context": context,
      "question": question
    }
  )

  return result

if __name__ == "__main__":
   json_input = '''{
  "firstName": "Bethany",
  "context": "The Alpine Explorer Tent boasts a detachable divider for privacy,  numerous mesh windows and adjustable vents for ventilation, and  a waterproof design. It even has a built-in gear loft for storing  your outdoor essentials. In short, it's a blend of privacy, comfort,  and convenience, making it your second home in the heart of nature!\\n",
  "question": "What can you tell me about your tents?"
}'''
   args = json.loads(json_input)

   result = run(**args)
   print(result)
