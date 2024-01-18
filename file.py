from tkinter import *
from tkinter import ttk, filedialog
import fitz  # PyMuPDF
from docx import Document  # python-docx

# Création d'une instance de la fenêtre Tkinter
win = Tk()

# Configuration de la géométrie de la fenêtre Tkinter
win.geometry("700x350")

# Définition de la fonction open_file pour afficher le contenu du fichier dans la fenêtre
def open_file():
    file_types = [('Text Files', '*.txt'), ('Python Files', '*.py'), ('PDF Files', '*.pdf'), ('Word Files', '*.docx')]
    file = filedialog.askopenfile(mode='r', filetypes=file_types)

    if file:
        if file.name.endswith('.pdf'):
            pdf_document = fitz.open(file.name)
            content = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                content += page.get_text()
        elif file.name.endswith('.docx'):
            doc = Document(file.name)
            content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        else:
            content = file.read()

        file.close()

        content_window = Toplevel(win)
        content_window.title("Contenu du fichier")

        text_widget = Text(content_window, wrap="word", font=('Arial', 12))
        text_widget.insert("1.0", content)
        text_widget.pack(expand=True, fill="both")

# Ajout d'un widget Label
label = Label(win, text="Cliquez sur le bouton pour parcourir les fichiers", font=('Georgia 13'))
label.pack(pady=10)

# Création d'un bouton qui, lorsqu'il est cliqué, appelle la fonction open_file
ttk.Button(win, text="Parcourir", command=open_file).pack(pady=20)

# Démarrage de la boucle d'événements Tkinter
win.mainloop()
