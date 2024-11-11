import ffmpeg as ffmpeg_lib  # Renamed to avoid conflicts
import numpy as np

def load_audio(file, sr):
    try:
        # Clean up the file path
        file = file.strip().strip('"').strip("\n").strip()

        # Use ffmpeg-python to create the FFmpeg command for loading audio
        # Remove `cmd=["ffmpeg", "-nostdin"]` since `run()` can directly find FFmpeg in PATH
        out, _ = (
            ffmpeg_lib.input(file, threads=0)
            .output("pipe:", format="f32le", acodec="pcm_f32le", ac=1, ar=sr)
            .run(capture_stdout=True, capture_stderr=True)
        )

        # Convert the byte buffer to a numpy array of floats
        return np.frombuffer(out, dtype=np.float32).flatten()

    except Exception as e:
        raise RuntimeError(f"Failed to load audio: {e}")
