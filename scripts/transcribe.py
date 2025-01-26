import pathlib
import subprocess

def run_whisper_cli(input_dir, output_dir, whisper_path, model_path, threads=8):
    # Convert input and output to Path objects
    input_dir = pathlib.Path(input_dir)
    output_dir = pathlib.Path(output_dir)

    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    # Glob all .wav files in the input directory
    wav_files = input_dir.glob("*.wav")

    for wav_file in wav_files:
        # Define the output file path (e.g., "out.srt" for each WAV file)
        output_file = output_dir / (wav_file.stem + ".srt")

        # Skip if the output file already exists
        if output_file.exists():
            print(f"Skipping {wav_file.name}, output file already exists.")
            continue

        print(f"Processing {wav_file.name}...")
        try:
            # Build the Whisper CLI command
            command = [
                whisper_path,
                "-m", model_path,
                "-f", str(wav_file),
                "-t", str(threads),
                "-osrt",  # Output in SRT format
                "-of", str(output_file.with_suffix('')),  # Output file without the .srt extension
                "-et", "2.8",
                "-tp", "0.1",
                "-mc", "64",
            ]
            
            # Run the command
            subprocess.run(command, check=True)
            print(f"Successfully processed {wav_file.name} -> {output_file.name}.")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {wav_file.name}: {e}")

if __name__ == "__main__":
    # Define your paths
    input_directory = "/mnt/e/cushvlogs_wav"
    output_directory = "/mnt/e/cushvlogs_srt"
    whisper_cli_path = "/mnt/e/whisper.cpp/build/bin/whisper-cli"  # Path to the Whisper CLI binary
    model_file_path = "/mnt/e/whisper.cpp/models/ggml-large-v3-turbo-q5_0.bin"  # Path to the model file

    # Run the script
    run_whisper_cli(input_directory, output_directory, whisper_cli_path, model_file_path)
