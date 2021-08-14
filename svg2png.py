from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
drawing = svg2rlg("Model 1.svg")
renderPM.drawToFile(drawing, "CNN Model Architecture.png", fmt="PNG")
