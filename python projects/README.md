# OpenCV Computer Vision Playground

A curated collection of computer vision and image processing projects built using **Python** and **OpenCV**. This repository serves as a workspace for exploring real-time video processing, computer vision applications, and building interactive systems.

---

## 🚀 Projects List

Here are the projects currently inside this repository:

### 1. 📹 Video Streaming Application (`/video_streaming`)
A real-time web-based video streaming application. It captures live camera feeds using OpenCV and streams it to a web interface using Flask.
* **Tech Stack:** Python, OpenCV (`cv2`), Flask, HTML/CSS.
* **Key Features:**
  * Real-time webcam frame acquisition.
  * MJPEG stream rendering over HTTP.
  * Lightweight web UI.

---

## 🛠️ Getting Started

Follow these instructions to set up the workspace and run the projects locally.

### Prerequisites
Make sure you have Python 3.8+ installed on your system.

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/opencv-python-projects.git
   cd opencv-python-projects
   ```

2. **Navigate to a specific project (e.g., `video_streaming`):**
   ```bash
   cd video_streaming
   ```

3. **Set up a virtual environment:**
   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate it (Mac/Linux)
   source venv/bin/activate

   # Activate it (Windows)
   venv\Scripts\activate
   ```

4. **Install the required packages:**
   ```bash
   pip install opencv-python flask
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000` to view the stream.

---

## 🗺️ Future Project Ideas to Build

Here are some cool OpenCV projects you can add to this repository next:
- [ ] **Face & Eye Detection:** Real-time facial feature tracking using Haar Cascades or Mediapipe.
- [ ] **Object Detection & Tracking:** Real-time object identification using YOLO or SSD.
- [ ] **Hand Gesture Controller:** Control your system volume, mouse, or presentation slides using hand gestures.
- [ ] **Virtual Paint:** Draw on the screen in real-time by moving a colored object (e.g., a pen or cap) in front of the camera.
- [ ] **Document Scanner:** Capture document images, apply perspective warping, and convert them to clean scanned PDFs.
- [ ] **Invisible Cloak:** Color segmentation/masking project to create a Harry Potter style invisibility cloak effect.

---

## 📄 License
This repository is licensed under the [MIT License](LICENSE). Feel free to use the code for learning and development.
