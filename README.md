#  License Plate Detection Web App (YOLOv8 + Flask)

A lightweight Flask web application that uses a custom-trained YOLOv8 model (`best.pt`) to detect license plates in uploaded images. Users can upload photos of vehicles, and the system returns the same image with a bounding box highlighting the detected plate.

---

##  Features

-  License plate detection via YOLOv8
-  Simple web interface using Flask
-  Upload and save processed images
-  Easily extendable for OCR or multi-plate support

---

##  Tech Stack

- **Model:** YOLOv8 (`best.pt`)
- **Backend:** Python 3.10+ with Flask
- **Image Processing:** PIL, OpenCV
- **Frontend:** HTML (Jinja2 Templates)

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/didarbilgin/PlateDetection.git
cd PlateDetection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` should include:**

```txt
flask
ultralytics
Pillow
```

### 3. Add your trained YOLOv8 model

Place your `best.pt` file inside the `model/` directory:

```
model/
└── best.pt
```

---

## 🖼️ Usage

### Run the app

```bash
python app.py
```

Visit: `http://127.0.0.1:5000/` in your browser and upload an image to detect plates.

---

## 📂 Project Structure

```
PlateDetection/
├── app.py
├── model/
│   └── best.pt
├── static/
│   └── uploads/
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

---

## 🛡️ .gitignore Tips

Make sure you don't accidentally commit heavy model files or user-uploaded images:

```
*.pt
static/uploads/*
!static/uploads/.gitkeep
```


## 📄 License

MIT License
