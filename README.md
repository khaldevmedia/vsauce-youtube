# Unused Letter Finder in YouTube Videos

This Python script responds to a challenge by **Michael Stevens** from [Vsauce](https://www.youtube.com/user/Vsauce) to identify any unused letters in his YouTube Short: [Watch the Video](https://www.youtube.com/shorts/hIMIsbLodzM).

## Features

- **Download Captions:** Extracts auto-generated English captions from a YouTube video.
- **Analyze Text:** Checks which letters of the English alphabet are not used in the captions.
- **Save Captions:** Stores the downloaded captions in a text file.
- **Supports YouTube Shorts and Standard YouTube Videos:** Handles various YouTube URL formats, including Shorts and regular videos, ensuring compatibility across different types of YouTube content.


## Installation

### Prerequisites

- **Python 3.6+**

### Install Required Library

```bash
pip install youtube_transcript_api
```

## Usage

1. **Set the YouTube Video URL**

   Open the script (`main.py`) and update the `VIDEO_URL` variable with the desired YouTube Short URL.

   ```python
   VIDEO_URL = "https://www.youtube.com/shorts/hIMIsbLodzM"  # Vsauce Short
   ```

2. **Run the Script**

   Execute the script using Python:

   ```bash
   python main.py
   ```

3. **View Results**

   - If all letters are used:
     ```
     All letters of the English alphabet were used in the video captions.
     ```
   - If some letters are not used:
     ```
     The following letters were NOT used in the video captions:
     q, x, z
     ```
   - If the transcript is too short:
     ```
     Transcript is very short. Letter usage may be limited.
     The following letters were NOT used in the video captions:
     q, x, z
     ```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- **[Michael Stevens (Vsauce)](https://www.youtube.com/user/Vsauce):** For inspiring this challenge.
- **[youtube_transcript_api](https://github.com/jdepoix/youtube-transcript-api):** For providing an easy way to access YouTube transcripts.

---

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** Create a `LICENSE` file in your project repository and include the MIT License text as shown below.

---

## MIT License

```markdown
MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
