import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image
from reportlab.pdfgen import canvas

def get_filenames(path) -> list:
    """Recursively get all the filenames present from all child directories.
    
    Parameters
    ----------
    path: str
        Directory containing all files, 
        (files can be in sub folders)

    Returns
    -------
    files: list
        fullpath of all the files inside this directory and subdirectories.
    """
    files = []
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            files.append(full_path)
        else:
            files += get_filenames(full_path)
    return files

def export_img2pdf(in_path, out_path, x=90, y=80):
    """Exports image to pdf
    
    Parameters
    ----------
    in_path: str
        Input image path (example: Images/1.jpg).

    out_path: str
        Output pdf path (example: Data/1.pdf).

    x: int  (Default=90)
        X coordinate on the canvas.

    y: int  (Default=80)
        Y coordinate on the canvas.
    """
    canva = canvas.Canvas(out_path, pagesize=letter)    
    img = Image(in_path, height=450, width=450)
    img.drawOn(canva, x, y)
    canva.save()

if __name__ == "__main__":
    x = 90  
    y = 180

    # directory containing images
    img_dir = 'Images' 
    files = get_filenames(img_dir)

    for f in files:
        out_fname = f.split(".")[0]+".pdf"
        export_img2pdf(f, out_fname, x, y)
        print(f"[+] {f} -> {out_fname}")