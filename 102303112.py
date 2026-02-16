import sys
import os
from pytube import Search, YouTube
from pydub import AudioSegment

def create_mashup(singer, n, y, output):
    from pytube import Search, YouTube
    from pydub import AudioSegment
    import os

    os.makedirs("audio", exist_ok=True)

    search = Search(f"{singer} songs")
    videos = search.results[:n]

    merged = AudioSegment.empty()
    count = 0

    for vid in videos:
        try:
            yt = YouTube(vid.watch_url)
            stream = yt.streams.filter(only_audio=True).first()
            if stream is None:
                continue

            fname = f"audio/{count}.mp4"
            stream.download(filename=fname)

            audio = AudioSegment.from_file(fname)
            merged += audio[:y * 1000]
            count += 1
        except:
            continue

    if count == 0:
        raise Exception("No audio processed")

    merged.export(output, format="mp3")

def usage():
    print("Usage:")
    print("python <rollno>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
    sys.exit(1)

def main():
    # 1️⃣ Check number of parameters
    if len(sys.argv) != 5:
        print("❌ Error: Incorrect number of parameters.")
        usage()

    singer = sys.argv[1]

    # 2️⃣ Validate numeric inputs
    try:
        n = int(sys.argv[2])
        y = int(sys.argv[3])
    except ValueError:
        print("❌ Error: NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    if n <= 10:
        print("❌ Error: NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if y <= 20:
        print("❌ Error: AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    output = sys.argv[4]

    os.makedirs("audio", exist_ok=True)

    try:
        print("🔍 Searching YouTube...")
        search = Search(f"{singer} songs")
        videos = search.results[:n]

        if not videos:
            print("❌ Error: No videos found.")
            sys.exit(1)

        merged = AudioSegment.empty()
        count = 0

        for vid in videos:
            try:
                print("⬇ Downloading:", vid.watch_url)

                yt = YouTube(vid.watch_url)
                stream = yt.streams.filter(only_audio=True).first()

                if stream is None:
                    print("⚠ Skipped: No audio stream available.")
                    continue

                filename = f"audio/{count}.mp4"
                stream.download(filename=filename)

                audio = AudioSegment.from_file(filename)
                clip = audio[:y * 1000]

                merged += clip
                count += 1

            except Exception as e:
                print("⚠ Skipped video due to error:", e)

        if count == 0:
            print("❌ Error: No audio files processed.")
            sys.exit(1)

        print("🔗 Merging clips...")
        merged.export(output, format="mp3")

        print("✅ Mashup created successfully:", output)

    except Exception as e:
        print("❌ Unexpected Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
