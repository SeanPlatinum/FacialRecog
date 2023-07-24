import cv2
import threading
from deepface import DeepFace
import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3 as tts
import random
cv2.__version__
class EmotionDetector:
    def __init__(self):
        self.videocapture = cv2.VideoCapture(0)
        self.snapshot_taken = False
        self.emotion = 'Processing...'
        self.counter = 0
        self.face_match = False
        self.ref_image = None

    def respond_to_emotion(self, emotion):
        engine = tts.init()
        responses = {
            'sad': [
                "I'm sorry to hear that you're feeling sad. Let me tell you a joke to cheer you up: Why don't scientists trust atoms? Because they make up everything!",
                "I see you're feeling sad. Here's a joke to lighten the mood: Why couldn't the bicycle stand up by itself? It was two tired!",
                "Sadness is temporary it may last a moment, a day, or even longer, but it will eventually fade away.",
                "Grief is the price we pay for love. Allow yourself to feel the sadness as a testament to the depth of your emotions",
                "It's okay to feel sad. Acknowledge your pain, and remember that healing takes time.",
                "In the midst of sadness, remember that brighter days will come. Hold on to hope and keep moving forward",
                "Sadness is like a storm cloud passing through. It may darken the sky for a while, but eventually, the sun will shine again."
            ],
            'happy': [
                "I'm glad to see you're happy! Here's a compliment for you: You have a great sense of humor!",
                "You're looking happy today! Here's a compliment: You always know how to brighten up a room!",
                "Your happiness is contagious! It brightens up the room and lifts everyone's spirits.",
                "Your radiant smile is a true reflection of the happiness you bring to those around you.",
                "I love being around you because your positivity and joy are absolutely infectious.",
                "Your happiness is like a ray of sunshine on a cloudy day. It's uplifting and refreshing.",
                "You have a natural gift for finding joy in the simplest things, and it's truly inspiring.",
                "Your laughter is music to my ears. It's a beautiful reminder of how wonderful life can be.",
                "Your happiness is a reflection of your inner strength and resilience. It's admirable and inspiring.",
                "You have a way of spreading happiness wherever you go. It's a remarkable quality that makes you truly special.",
                "Your genuine happiness is a breath of fresh air. It reminds me to appreciate the little moments in life.",
                "Your positive outlook on life is truly admirable. You have a remarkable ability to find joy even in challenging times."
            ],
            'fear': ["Courage is not the absence of fear, but the triumph over it.",
                "Don't let fear hold you back. Embrace it, learn from it, and let it fuel your determination to succeed.",
                "Fear is only temporary, but regret lasts forever. Take that leap of faith and see what amazing things await you.",
                "Remember, fear is just a feeling. It's not a fact. You have the strength within you to overcome any challenge.",
                "The only way to conquer fear is to face it head-on. Step out of your comfort zone and watch your fears diminish.",
                "Fear is not your enemy; it's a sign that you're pushing yourself to grow. Embrace it and let it propel you forward.",
                "The biggest risks often lead to the greatest rewards. Don't let fear rob you of the opportunities that lie ahead.",
                "You are capable of more than you think. Trust yourself, have faith, and let go of your fears. Amazing things can happen.",
                "Fear can paralyze you, or it can motivate you. Choose to let it motivate you to reach new heights.",
                "Every great accomplishment started with a small step taken in the face of fear. Take that step, and see where it leads you."],
            'disgust':["Disgust is just a feeling, and like all feelings, it will pass. Don't let it consume you.",
                        "Instead of being disgusted by others, try to understand their perspective and find common ground.",
                        "Disgust is often a reflection of our own insecurities. Focus on self-acceptance and compassion.",
                        "Every person has their own journey and experiences. Rather than being disgusted, practice empathy and tolerance.",
                        "Don't let disgust blind you to the potential beauty and goodness in others. Look beyond the surface.",
                        "Remember, everyone is entitled to their own choices and preferences. Embrace diversity and respect differences.",
                        "Disgust is a signal that something challenges our beliefs or values. Use it as an opportunity for growth and self-reflection.",
                        "When faced with disgust, choose to respond with grace and understanding. It speaks volumes about your character.",
                        "Let go of judgment and replace it with curiosity. Seek to understand what might be driving someone's actions before feeling disgusted.",
                        "Focus on cultivating gratitude and appreciation for the things that bring you joy, rather than dwelling on feelings of disgust."],
            'surprise':["Life is full of surprises. Embrace them with open arms and a curious heart",
                        "Surprises are the spice of life, adding a touch of magic and excitement to our everyday existence",
                        "The best moments are the unexpected ones that leave us in awe and wonder",
                        "Surprise yourself with what you are capable of. Push beyond your limits and discover your true potential",
                        "Surprise is the spark that ignites our imagination and fuels our creativity."],
            'angry':["Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured.",
                    "In the heat of anger, think twice before you speak, because your words can cause irreversible damage.",
                    "When anger rises, think of the consequences.","Peace begins when anger ends.",
                    "Reacting in anger or annoyance will not advance one's ability to persuade.",
                    "It's not about suppressing anger; it's about finding constructive ways to express it.",
                    "Choose forgiveness over anger, love over hate, and peace over chaos. You'll find inner serenity.",
                    "Anger doesn't solve anything; it builds nothing. Choose to let go and find peace within.",
                    "Breathe deeply, count to ten, and remember that anger doesn't resolve anything. Choose understanding and empathy instead.",
                    "In the face of anger, respond with kindness. It's a powerful tool to diffuse any situation."],
            'neutral': ["Believe you can, and you're halfway there.",
                "The future belongs to those who believe in the beauty of their dreams.",
                "Success is not final, failure is not fatal: It is the courage to continue that counts.",
                "The only limit to our realization of tomorrow will be our doubts of today.",
                "The harder you work for something, the greater you'll feel when you achieve it.",
                "The secret to getting ahead is getting started.",
                "You are never too old to set another goal or to dream a new dream.",
                "Don't watch the clock; do what it does. Keep going.",
                "The biggest adventure you can take is to live the life of your dreams.",
                "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."]

        }

        # Get a random response for the given emotion
        response = random.choice(responses.get(emotion, ["I'm not sure how to respond to that emotion."]))

        # Use the speech synthesis engine to say the response
        engine.say(response)
        engine.runAndWait()
    def convert_cv2tkinter(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return ImageTk.PhotoImage(image = Image.fromarray(frame))

    def picture(self):
        ret, frame = self.videocapture.read()
        if ret:
            self.ref_image = frame
            self.snapshot_taken = True

    def checkface(self, frame):
        try:
            results = DeepFace.analyze(frame, actions=['emotion'])
            print(results)
            if results:
                self.emotion = results[0]['dominant_emotion']
                self.respond_to_emotion(self.emotion)
            else:
                self.emotion = 'No face detected'
            verification = DeepFace.verify(frame, self.ref_image)
            self.face_match = verification['verified']
        except Exception as e:
            self.face_match = False
            self.emotion = str(e)

    def run(self):
        root = tk.Tk()
        root.config(bg='#171D1C')
        root.geometry("800x800")
        frame_tk = tk.Frame(master=root, bg='#171D1C')
        frame_tk.pack(pady=20, padx=60, fill="both", expand=True)
        label = tk.Label(master=frame_tk, text="Emotion Recognition\n By Sean Diaz", font=('',30),fg="green" ,bg='#171D1C')
        label.pack(pady=12, padx=12)
        button1 = tk.Button(master=frame_tk, text="START", command=self.picture,)
        button1.pack(pady=12, padx=12)
        video = tk.Label(frame_tk)
        video.pack(side="bottom")

        while True:
            ret, frame = self.videocapture.read()
            if ret:
                if self.counter % 30 == 0 and self.snapshot_taken:
                    try:
                        threading.Thread(target=self.checkface, args=(frame,)).start()
                    except ValueError:
                        pass
                self.counter += 1
                if self.face_match:
                    cv2.putText(frame, "MATCH! Emotion: " + self.emotion, (20, 450), cv2.FONT_ITALIC, .7, (0, 0, 255), 2)
                else:
                    cv2.putText(frame, "No face detected. Emotion: " + self.emotion, (20, 450), cv2.FONT_ITALIC, .7, (0, 255, 0), 2)

                tkinter_frame = self.convert_cv2tkinter(frame)
                video.imgtk = tkinter_frame
                video['image'] = video.imgtk
                root.update()

            if cv2.waitKey(1) == ord('q'):
                break

        self.videocapture.release()
        cv2.destroyAllWindows()

EmotionDetector().run()
