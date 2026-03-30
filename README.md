# ✋  AirCanvas – Hand Gesture Controlled Virtual Whiteboard

> Draw, write, and create on a virtual canvas using only your hand gestures — no mouse, no pen, no touch screen needed

## 📌 About the Project

Air Canvas is a computer vision application that lets users draw and interact with a digital canvas using hand gestures detected via webcam. Built with **Python**, **OpenCV**, and **MediaPipe**, it tracks hand landmarks in real-time and translates finger movements into drawing actions — no physical input device required.

---

## 🚀 Features

- ✏️ **Freehand Drawing** — Draw with your index finger in the air
- 🔷 **Shapes** — Rectangle, Circle, Triangle, Line, Oval
- 🎨 **10 Colors** — Pink, Blue, Green, Yellow, Orange, Purple, Teal, Olive, Indigo, Light Pink
- 🧹 **Eraser Tool** — Erase with one finger after activating eraser
- 🖐️ **Gesture Controls** — No buttons needed
- 📺 **Feedback Window** — See your canvas output separately
- ❌ **Exit** — Press `Q` to quit

---

## 🖐️ Gesture Guide

| Gesture | Action |
|---------|--------|
| ☝️ One finger (Index) | Draw / Operate selected tool |
| ✌️ Two fingers (V shape) | Select tool or color from navbar |
| 🖐️ Full hand | Set / finalize shape on canvas |
| ⌨️ Press `Q` | Exit the application |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.8+ | Core programming language |
| OpenCV 4.5+ | Real-time video capture & image processing |
| MediaPipe | Hand landmark detection (21 points) |
| NumPy | Array operations & canvas management |
| Anaconda | Virtual environment management |

---

## 📋 System Requirements

**Hardware:**
- Processor: Intel Core i3 or equivalent (Dual-core)
- RAM: 4 GB minimum
- Storage: 500 MB free space
- Webcam: HD (720p or better)
- Graphics: OpenGL 2.0 support

**Software:**
- OS: Windows 7 or later (64-bit recommended)
- Python 3.8 or later
- Anaconda (recommended)

---

## ⚙️ Installation & Setup

### 1. Clone or Download the project
```bash
git clone https://github.com/your-username/air-canvas.git
cd air-canvas
```

### 2. Create Conda Environment
```bash
conda create -n aircanvas python=3.8
conda activate aircanvas
```

### 3. Install Dependencies
```bash
pip install opencv-python mediapipe numpy
```

### 4. Run the Application
```bash
python main.py
```

---

## 📁 Project Structure

```
Air_Canvas/
│
├── cam.py          # Webcam test script
├── HandTrack.py    # Hand detection & landmark tracking class
├── main.py         # Main application — canvas, tools, drawing logic
└── README.md
```

---

## 🔄 How It Works

```
START WEBCAM
     ↓
MEDIAPIPE detects 21 hand landmarks
     ↓
OPENCV processes each video frame
     ↓
USER selects tool (2 fingers on navbar)
     ↓
USER draws / erases (1 finger)
     ↓
CANVAS updates in real-time
     ↓
OUTPUT shown in feedback window
     ↓
Press Q to exit
```

---

## 🗂️ Tools Available

| Tool | Description |
|------|-------------|
| Brush | Freehand drawing with index finger |
| Eraser | Erase parts of the drawing |
| Rectangle | Draw rectangle by dragging |
| Circle | Draw circle by dragging |
| Triangle | Draw triangle by dragging |
| Line | Draw straight line |
| Oval | Draw oval / ellipse |

---

## 📦 Dependencies

```
opencv-python>=4.5.0
mediapipe
numpy>=1.19.0
```

Install all at once:
```bash
pip install opencv-python mediapipe numpy
```

---

## 🧪 Testing

Testing was performed across 5 types:

- ✅ **Functional** — All tools and gestures work correctly
- ✅ **Performance** — Stable FPS during real-time tracking
- ✅ **Compatibility** — Tested on Windows, macOS, Linux
- ✅ **Usability** — Tested with educators, designers, general users
- ✅ **Stress** — Handles rapid gestures and complex backgrounds

---

## 🔮 Future Enhancements

- 🗣️ Voice command integration
- 🤝 Multi-user collaborative canvas
- 🥽 AR/VR environment support
- 📱 Mobile & tablet compatibility
- 🔁 Undo / Redo gestures
- 💾 Save canvas as image file
- 🧠 CNN-based improved gesture recognition

---

## 📚 References

1. S.V. Ashwin Kumar et al. (2021) — Virtual Whiteboard Using OpenCV
2. Akash Kumar Chaudhary et al. (2021) — Air Canvas using OpenCV & NumPy
3. Pranavi Srungavarapu et al. (2021) — Virtual Sketch Using OpenCV
4. Ramachandra V. et al. (2022) — Virtual Air Canvas Using OpenCV and MediaPipe

---

## 📄 License

This project was developed as a B.Tech final year project at **Tirumala Engineering College**, affiliated to JNTU Kakinada. For academic use only.

---

> *"Drawing in the air — where imagination meets technology."*
