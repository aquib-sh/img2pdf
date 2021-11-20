import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.pdfgen import canvas

x = 90
y = 180

# put the paths for input directories
paths = ['Images/2021-11-17 14-27', 
     'Images/extractImages_a662ebda43da247612eec97a51b71b58/90 Tidewater Manor',
     'Images/extractImages_a662ebda43da247612eec97a51b71b58/Summer Hall IG in front of house'
     ]

for path in paths:
    files = os.listdir(path)
    for f in files:
        out_fname = f.split(".")[0]+".pdf"

        in_fpath = os.path.join(path, f)
        out_fpath = os.path.join('data', out_fname)

        canva = canvas.Canvas(out_fpath, pagesize=letter)    

        img = Image(in_fpath, height=450, width=450)

        img.drawOn(canva, x, y)
        canva.save()
        print(f"[+] {in_fpath} -> {out_fpath}")
