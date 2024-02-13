from random import choice

def get_response(user_input: str) -> str: 
   lowered: str = user_input.lower()
   
   if lowered == '':
       return 'hmmm?'
   elif 'hisui' in lowered:
       return 'Yes, Master'
   elif 'morning' in lowered:
       return 'good morning, Master'
   elif 'good night' in lowered:
       return 'sleep well, Master'
   else:
       return '.....'