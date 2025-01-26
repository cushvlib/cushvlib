import pathlib
import ffmpeg

def convert_mp3_to_wav(input_dir, output_dir):
    # Convert input and output to Path objects
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)

    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Glob all mp3 files in the input directory
    mp3_files = input_dir.glob("*.mp3")

    for mp3_file in mp3_files:
        # Define the output file path
        wav_file = output_dir / (mp3_file.stem + ".wav")

        # Skip conversion if the output file already exists
        if wav_file.exists():
            print(f"Skipping {mp3_file.name}, output file already exists.")
            continue

        print(f"Converting {mp3_file.name} to {wav_file.name}...")
        try:
            # Run the ffmpeg command to convert to WAV
            (
                ffmpeg
                .input(str(mp3_file))
                .output(str(wav_file), ar=16000, ac=1, c="pcm_s16le")
                .run(overwrite_output=True)
            )
            print(f"Successfully converted {mp3_file.name} to {wav_file.name}.")
        except ffmpeg.Error as e:
            print(f"Error converting {mp3_file.name}: {e.stderr.decode()}")

if __name__ == "__main__":
    # Define your input and output directories
    input_directory = "/mnt/e/cushvlogs"
    output_directory = "/mnt/e/cushvlogs_wav"

    convert_mp3_to_wav(input_directory, output_directory)
