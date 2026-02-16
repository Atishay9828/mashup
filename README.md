Mashup Generation & Web Service Pipeline

## 1. Methodology
```
┌──────────────────────┐
│ User Input Capture   │
│ (CLI / Web Form)     │
└─────────┬────────────┘
          ↓
┌────────────────────────────┐
│ Input Validation           │
│ (Parameter & Email Check)  │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┐
│ YouTube Search &           │
│ Audio Download (PyTube)    │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┐
│ Audio Extraction           │
│ & Pre-processing           │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┐
│ Audio Trimming             │
│ (First Y Seconds)          │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┐
│ Audio Merging              │
│ (Mashup Creation)          │
└─────────┬──────────────────┘
          ↓
┌────────────────────────────┐
│ ZIP Packaging              │
│ & Email Delivery           │
└────────────────────────────┘
```

The methodology follows a modular automation pipeline where user input is validated, audio is programmatically downloaded, processed, trimmed, merged into a mashup, compressed into a ZIP archive, and delivered via email. The core mashup logic is implemented once (Program 1) and reused in a web service layer (Program 2), demonstrating clean separation of concerns.

## 2. Description

- **Task Type:** Multimedia Processing & Web Service Automation
- **Problem Nature:** Manual mashup creation is time-consuming and requires downloading, trimming, merging, and file packaging
- **Objective:** Automate mashup generation from YouTube content; provide both CLI-based and web-based interfaces; deliver output via email in ZIP format
- **Core Components:**
    - Command-line parameter parsing
    - Web form interface (Streamlit)
    - YouTube search and download (PyTube / yt-dlp)
    - Audio processing (pydub)
    - File compression (zipfile)
    - Email automation (smtplib)
    - Environment variable-based credential security
- **Architecture Type:** Layered Architecture (Core Engine + Service Layer)

## 3. Input / Output

**Input:**
- Singer name
- Number of videos (>10)
- Duration of each video in seconds (>20)
- Valid email ID

**Example Input (CLI):**
```bash
python 102303112.py "Sharry Maan" 20 30 output.mp3
```

**Example Input (Web Service):**
- Singer: Sharry Maan
- Number of videos: 20
- Duration: 30 sec
- Email: user@example.com

**Intermediate Representation:**
- Downloaded audio streams
- Trimmed audio segments (Y seconds each)
- Combined AudioSegment object

**Output:**
- Generated mashup file (`output.mp3`)
- Zipped result (`result.zip`)
- Email delivery of ZIP file

## 4. Execution Environment

- **Language:** Python
- **CLI Framework:** `sys` module
- **Web Framework:** Streamlit
- **YouTube Library:** PyTube (or `yt-dlp` as alternative)
- **Audio Processing:** `pydub` (requires `ffmpeg`)
- **Compression:** `zipfile`
- **Email Service:** `smtplib` (SMTP over SSL)
- **Security:** Environment variable for email password
- **Platform:** Local Machine / Google Colab

## 5. Results Summary

**Key Outcomes:**
- Fully automated mashup generation
- Dual-interface system (CLI + Web Service)
- Secure email-based delivery mechanism
- Input validation prevents runtime failures
- Exception handling ensures fault tolerance

## 6. Key Observations

- Input validation is critical for robust CLI tools
- Environment variables improve security over hardcoded credentials
- Audio trimming precision depends on millisecond-level slicing
- Modular design allows reuse of core logic across interfaces
- Web layer and processing engine separation simplifies scalability

## 7. Conclusion

This project demonstrates a complete automation pipeline for multimedia mashup generation and delivery.

**Core Takeaways:**
- Reusable core logic reduces redundancy
- Separation of engine and service layers improves maintainability
- Secure credential handling is essential in web services
- Automation significantly reduces manual multimedia processing effort

**Applications:**
- Automated playlist mashups
- Music sampling tools
- Audio preview generators
- Educational demonstrations of multimedia pipelines
- Cloud-based media automation services
