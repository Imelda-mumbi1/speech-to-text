import speech_recognition as sr   # Import the speech recognition library

# Step 1: Create a recognizer instance
recognizer = sr.Recognizer()

# Step 2: Use the microphone as the input source
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)  # Helps reduce background noise
    print("🎤 Say something (say 'stop' to end)...")

    while True:
        try:
            # Listen for speech
            audio = recognizer.listen(source)

            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print("📝 You said: " + text)

            # Check if user said "stop"
            if text.lower() == "stop":
                print("👋 Stopping program...")
                break

        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError:
            print("⚠️ Could not request results, check your internet connection")
