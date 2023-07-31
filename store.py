import requests

requests.put(f'http://127.0.0.1:5000/to{self.site}', data={"query": self.query})

