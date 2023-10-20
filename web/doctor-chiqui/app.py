from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from fpdf import FPDF
import os
import base64

app = Flask(__name__)

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Receta Médica', 0, 1, 'C')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        dni = request.form['dni']
        birthdate = request.form['birthdate']
        medications = request.form.getlist('medications')

        # Crear PDF
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 12)
        pdf.ln(10)
        pdf.cell(0, 10, f'Nombre: {name}', 0, 1)
        pdf.cell(0, 10, f'DNI: {dni}', 0, 1)
        pdf.cell(0, 10, f'Fecha de Nacimiento: {birthdate}', 0, 1)
        pdf.ln(10)
        pdf.cell(0, 10, 'Medicamentos:', 0, 1)
        for med in medications:
            pdf.cell(0, 10, f'- {med}', 0, 1)

        # Guardar PDF en directorio correspondiente
        # Guardar PDF en directorio correspondiente
        dir_count = len([name for name in os.listdir('pdfs') if os.path.isdir(os.path.join('pdfs', name))])
        dir_name = base64.b64encode(str(dir_count + 1).encode()).decode()
        if not os.path.exists(f'pdfs/{dir_name}'):
            os.makedirs(f'pdfs/{dir_name}')
        pdf.output(f'pdfs/{dir_name}/receta.pdf')

        return redirect(url_for('download_pdf', dir_name=dir_name))

    return render_template('index.html')

@app.route('/<dir_name>/receta.pdf')
def download_pdf(dir_name):
    return send_from_directory(f'pdfs/{dir_name}', 'receta.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
