from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=32)
        self.cell(0, 0, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    create_shirt(input("Name: ").strip())

def create_shirt(name):
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", 12.34375, 56, 185.3125)
    pdf.set_font("helvetica", style="B", size=22)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 200, f"{name} took CS50", 0, align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

