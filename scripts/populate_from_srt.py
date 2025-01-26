import os
import pysrt  # Install this with `pip install pysrt`
from library.models import Episode, Sentence

def populate_database_from_srt(srt_directory):
    # Iterate over all .srt files in the given directory
    for srt_file in os.listdir(srt_directory):
        if srt_file.endswith(".srt"):
            srt_path = os.path.join(srt_directory, srt_file)
            episode_title = os.path.splitext(srt_file)[0]

            # Create or get the Episode object
            episode, created = Episode.objects.get_or_create(
                title=episode_title,
                defaults={"description": f"Transcription for {episode_title}."}
            )

            # Parse the .srt file
            subs = pysrt.open(srt_path)

            for sub in subs:
                start_seconds = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000
                end_seconds = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000

                # Create a Sentence object for each subtitle entry
                Sentence.objects.create(
                    episode=episode,
                    text=sub.text,
                    start_time=start_seconds,
                    end_time=end_seconds,
                )

            print(f"Processed {srt_file}")

# Call the function with the directory path
srt_directory = "/mnt/e/cushvlogs_srt"
populate_database_from_srt(srt_directory)
