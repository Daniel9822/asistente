import os
from dotenv import load_dotenv
import requests

class SendMessage():
  def __init__(self):
    load_dotenv()
    self.api = os.getenv('API_BOT')

  def get(self, number, message):
    # response = requests.post(self.api, {
    #   number,
    #   message
    # })
    print(f"esto me llego", number, message)
    return True
    # if response.status_code == 200:
    #   return True
    # else:
    #   return False
      