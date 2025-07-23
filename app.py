import os
from flask import Flask, render_template, request
from PIL import Image, ImageDraw
from ultralytics import YOLO

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# === YOLO Modelini Yükle ===
model = YOLO("model/best.pt")  # YOLOv8 için eğittiğin modelin yolu

def predict_yolo(image_path):
    results = model(image_path)
    boxes = results[0].boxes  # İlk görselin kutuları

    # Eğer hiç kutu yoksa None döndür
    if len(boxes) == 0:
        return None

    # İlk bulunan kutunun koordinatlarını al
    box = boxes[0].xyxy[0].cpu().numpy()  # x1, y1, x2, y2
    return [int(coord) for coord in box]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Kutuyu tahmin et
            box = predict_yolo(filepath)

            # Görseli aç ve kutuyu çiz
            img = Image.open(filepath).convert('RGB')
            if box:
                draw = ImageDraw.Draw(img)
                draw.rectangle(box, outline="red", width=4)

            # Sonucu kaydet
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], "result_" + file.filename)
            img.save(result_path)

            return render_template('index.html', result_img=result_path)

    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
