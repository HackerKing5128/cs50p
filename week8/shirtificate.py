from fpdf import FPDF


pdf = FPDF()
pdf.add_page()

pdf.set_font("Times", "B", 45)
pdf.cell(0,60,text="CS50 Shirtificate",align="C")
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
name=input("Name: ")
pdf.image("shirtificate.png",x=0,y=70)
pdf.text(x=50,y=150,text= f"{name} took CS50")
pdf.output("Shirtificate.pdf")
