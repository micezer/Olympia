from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generar_pdf_inscripcion(datos):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    styles = getSampleStyleSheet()
    elementos = []
    
    # Encabezado
    elementos.append(Paragraph("FICHA DE INSCRIPCIÓN", styles['Title']))
    elementos.append(Spacer(1, 24))
    
    # Datos personales
    elementos.append(Paragraph("<b>DATOS PERSONALES</b>", styles['Heading2']))
    elementos.append(Paragraph(f"<b>Nombre:</b> {datos['nombre_completo']}", styles['Normal']))
    elementos.append(Paragraph(f"<b>Fecha Nacimiento:</b> {datos['fecha_nacimiento']}", styles['Normal']))
    elementos.append(Paragraph(f"<b>DNI:</b> {datos['dni']}", styles['Normal']))
    
    # Datos deportivos
    elementos.append(Spacer(1, 12))
    elementos.append(Paragraph("<b>DATOS DEPORTIVOS</b>", styles['Heading2']))
    elementos.append(Paragraph(f"<b>Posición:</b> {datos['posicion']}", styles['Normal']))
    elementos.append(Paragraph(f"<b>Club Anterior:</b> {datos['club_anterior'] or 'Ninguno'}", styles['Normal']))
    
    doc.build(elementos)
    buffer.seek(0)
    return buffer