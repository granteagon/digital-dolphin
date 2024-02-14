"""Text to binary to dolphin converter."""

# TODO: find a way to make a click sound instead of speaking a dot

b2d = {
    "0": "e",
    "1": ".",
}


def text_to_binary(text):
    """Convert text to binary."""
    binary = " ".join(format(ord(letter), "b") for letter in text)
    return binary


def binary_to_dolphin(binary):
    """Convert binary to dolphin."""
    dolphin = binary.replace("0", b2d["0"]).replace("1", b2d["1"])
    return dolphin


def decode_dolphin(dolphin):
    """Convert dolphin to binary."""
    d2b = {v: k for k, v in b2d.items()}
    binary = dolphin.replace("e", d2b["e"]).replace(".", d2b["."])
    return binary


def binary_to_text(binary):
    """Convert binary to text."""
    text = "".join(chr(int(letter, 2)) for letter in binary.split())
    return text


def copy_to_clipboard(text):
    """Copy text to clipboard."""
    import pyperclip

    pyperclip.copy(text)


def dolphin_text_to_audio_file(dolphin_text):
    """Convert dolphin text to an audio file."""
    from gtts import gTTS

    tts = gTTS(dolphin_text, lang="en")
    tts.save("dolphin.mp3")


def human_to_dolphin_audio(audio_file, speed=10, pitch=1.5):
    """Convert human audio to dolphin audio."""
    import pydub

    sound = pydub.AudioSegment.from_mp3(audio_file)
    # convert to a wav file
    sound.export("dolphin.wav", format="wav")

    import pyrubberband as pyrb
    import soundfile as sf

    y, sr = sf.read("dolphin.wav")
    # Play back at speed
    y_stretch = pyrb.time_stretch(y, sr, speed)
    # TODO: Make pitch shift work
    # Play back at pitch
    # y_shift = pyrb.pitch_shift(y, sr, pitch)
    sf.write("dolphin.wav", y_stretch, sr, subtype="PCM_24")
    sound = pydub.AudioSegment.from_wav("dolphin.wav")
    # convert back to mp3
    sound.export("dolphin.mp3", format="mp3")


def speak_dolphin(dolphin_text):
    """Speak dolphin text."""
    dolphin_text_to_audio_file(dolphin_text)
    human_to_dolphin_audio("dolphin.mp3")
    import os

    os.system("afplay dolphin.mp3")


def command_line_interface():
    """Command line interface."""
    import argparse

    parser = argparse.ArgumentParser(description="Text to binary to dolphin converter.")
    # all arguments are optional
    parser.add_argument("--encode", help="Text to convert to dolphin.", required=False)
    parser.add_argument(
        "--speak",
        help="Speak dolphin? (y/n): (pip install pydub pyrubberband soundfile gtts)",
        required=False,
    )
    parser.add_argument(
        "--copy",
        help="Copy to clipboard? (y/n): (pip install pyperclip)",
        required=False,
    )
    parser.add_argument("--decode", help="Decode dolphin to text.", required=False)
    args = parser.parse_args()
    if args.encode:
        binary = text_to_binary(args.encode)
        dolphin = binary_to_dolphin(binary)
        print(f"Dolphin: {dolphin}")
        print(binary_to_text(decode_dolphin(binary)))
        if args.copy:
            copy_to_clipboard(dolphin)
        if args.speak:
            speak_dolphin(dolphin)
    elif args.decode:
        binary = decode_dolphin(args.decode)
        text = binary_to_text(binary)
        print(f"Binary: {binary}")
        print(f"Text: {text}")
        if args.copy:
            copy_to_clipboard(text)
    # if no args were supplied, prompt the user
    elif not any(vars(args).values()):
        # ask them if they want to encode or decode
        print("Encode or decode? (e/d):")
        encode_or_decode = input()
        if encode_or_decode == "e":
            print("Text to encode:")
            text = input()
            binary = text_to_binary(text)
            dolphin = binary_to_dolphin(binary)
            print(f"Dolphin: {dolphin}")
            print("Copy to clipboard? (y/n):")
            copy = input()
            if copy == "y":
                copy_to_clipboard(dolphin)
            print("Speak dolphin? (y/n):")
            speak = input()
            if speak == "y":
                speak_dolphin(dolphin)
        elif encode_or_decode == "d":
            print("Dolphin to decode:")
            dolphin = input()
            binary = decode_dolphin(dolphin)
            text = binary_to_text(binary)
            print(f"Binary: {binary}")
            print(f"Text: {text}")


def print_ascii_dolphin():
    """Print the ASCII dolphin."""
    print(
        """
      _____ _____ _____ _____ _______       _        
     |  __ \_   _/ ____|_   _|__   __|/\   | |       
     | |  | || || |  __  | |    | |  /  \  | |       
     | |  | || || | |_ | | |    | | / /\ \ | |       
     | |__| || || |__| |_| |_   | |/ ____ \| |____   
     |_____/_____\_____|_____|__|_/_/  _ \_\______|_ 
     
         |  __ \ / __ \| |    |  __ \| |  | |_   _| \ | |
         | |  | | |  | | |    | |__) | |__| | | | |  \| |
         | |  | | |  | | |    |  ___/|  __  | | | | . ` |
         | |__| | |__| | |____| |    | |  | |_| |_| |\  |
         |_____/ \____/|______|_|    |_|  |_|_____|_| \_|
                                                 
                                                 
                                           00001110
                                       11110110 11110110
                                          00001110
                               _.-~  )  00100
                    _..--~~~~,'   ,-/  00  _
                 .-'. . . .'   ,-','  1 ,' )
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'
            /. . . . '~~             ,-'
           /. . . . .             ,-'
          ; . . . .  - .        ,'
         : . . . .       _     /
        . . . . .          `-.:
       . . . ./  - .          )
      .  . . |  _____..-~^-._/ ____.--~^--._
~---~~~~----~~~~             ~~
    """
    )


def run():
    """Run the program."""
    print_ascii_dolphin()
    command_line_interface()


if __name__ == "__main__":
    run()
