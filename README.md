# digital-dolphin
Text to binary to dolphin to audio converter, written in python of course.

## Installation
Clone the repository and install the requirements.
```bash
pip install -r requirements.txt
```

### MacOS
You will need to install `ffmpeg` to convert the audio to a `.wav` file. You can install it with homebrew. If you'd rather not install `ffmpeg` you can just install each requirement individually when you run the code.  The code will prompt you to install the requirements needed to run each step.

#### Install homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Install ffmpeg (only needed if you wish to produce dolphin audio)
```bash
brew install ffmpeg
```
If you get and error from homebrew about needing to install the command line tools, you can install them with the following command.
```bash
xcode-select --install
```

### Windows
I haven't tested this on Windows, but it should work. You will need to install `ffmpeg` and add it to your PATH. You can download it from [here](https://www.ffmpeg.org/download.html).

## Usage
Running the code will prompt you to enter a message, and then it will convert the message to binary, then to a dolphin, and then to audio. The audio will be saved as `output.wav` in the current directory.  You are prompted at each step to press enter to continue.
```bash
python digital_dolphin.py
```

The tool will also copy your message to your clipboard, so you can paste it into your text messages or emails.

## Roadmap
- [ ] Add a decoder to convert the audio back to text.
- [ ] Add a GUI, because why not?
- [ ] Add a web ui where I can display spammy google adwords ads to unsuspecting visitors they never actually click on and just end up degrading their browsing experience.

Please use responsibly.  Do not start any dolphin wars or otherwise incite any dolphin unrest with this tool.

May the clicks be with you.

