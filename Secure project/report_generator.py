from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ReportGenerator:
    def __init__(self, filename):
        self.filename = filename

    def generate_report(self, content):
        c = canvas.Canvas(self.filename, pagesize=letter)
        width, height = letter
        c.drawString(100, height - 100, content)
        c.save()
