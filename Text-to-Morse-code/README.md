# 🆘 Text to Morse code

A **Python application** that lets you:

- 🔡 **Convert Text to Morse Code**
- 🔠 **Convert Morse Code to Text**
- 🔊 **Play Morse Code Sound**

---

## ⚙️ **Features**

- **Text to Morse**: Converts English text to Morse code.
- **Morse to Text**: Decodes Morse code to readable text.
- **Sound Playback**: Plays Morse as:
  - 🔴 Dot (.) → Short beep
  - ➖ Dash (-) → Long beep
  - ⬜ Space → Pause between letters
  - 🔁 Slash (/) → Pause between words

---

## 🛠️ **Tech Stack**

- **Python 3.x**
  [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
- `winsound` for sound (Windows only)
- `re` and `time` modules

## 📋 **Requirements**

- **Windows OS** (Uses `winsound`)
- **Python 3.x**

---

## ▶️ **How to Use**

1. **Run the script** and choose an option:
   - 1️⃣ Text to Morse
   - 2️⃣ Morse to Text
   - 3️⃣ Exit
2. **Enter the text** or **Morse code**.
3. **Hear the Morse code** if converting from text.

---

## 🔊 **Morse Code Sound Rules**

- **Dot (.)** → Short beep (100 ms)
- **Dash (-)** → Long beep (300 ms)
- **Space** → Short pause (0.3s)
- **Slash (/)** → Word pause (0.7s)

---

## 📁 **File Structure**

```
Text-to-Morse-code/
│
├── main.py  # Main script
└── README.md                # Documentation
```

---
