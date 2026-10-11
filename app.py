from flask import Flask, render_template_string, url_for
from pathlib import Path

app = Flask(__name__, static_folder="static")

# Photo filenames inside the static folder
PHOTO_1 = "image.png"
PHOTO_2 = "image copy.png"
PHOTO_3 = "image copy 2.png"


@app.route("/")
def home():
    photos = [PHOTO_1, PHOTO_2, PHOTO_3]

    # Check that the expected image files exist
    for photo in photos:
        image_path = Path(app.static_folder) / photo
        if not image_path.is_file():
            app.logger.warning("Photo not found: %s", image_path)

    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For MOMMYKO ❤️</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Trebuchet MS', sans-serif;
            background: linear-gradient(
                135deg, #ffd6e7, #ffb6d1, #fff0f5
            );
            color: #d63384;
            padding: 20px 12px;
            overflow-x: hidden;
        }

        .card {
            width: 100%;
            max-width: 450px;
            text-align: center;
            padding: 28px 22px;
            border: 3px solid white;
            border-radius: 30px;
            background: rgba(255, 255, 255, 0.94);
            box-shadow: 0 10px 40px #e7548050;
            position: relative;
            z-index: 2;
        }

        .big-heart {
            font-size: 65px;
            animation: beat 1s infinite;
        }

        h1 {
            font-size: clamp(24px, 6vw, 30px);
            margin: 12px 0;
        }

        h2 {
            color: #ff4081;
            font-size: 21px;
        }

        p {
            line-height: 1.8;
        }

        button {
            background: #ff4f87;
            color: white;
            border: none;
            border-radius: 30px;
            padding: 14px 22px;
            margin: 8px 4px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s, transform 0.3s;
        }

        button:hover {
            background: #e91e63;
            transform: scale(1.04);
        }

        button:focus-visible {
            outline: 3px solid #d63384;
            outline-offset: 3px;
        }

        #surprise {
            display: none;
            animation: appear 0.8s ease;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 12px;
            margin: 22px 0;
        }

        .photo-frame {
            width: 100%;
            height: 180px;
            overflow: hidden;
            border: 4px solid white;
            border-radius: 18px;
            background: #fff0f5;
            box-shadow: 0 4px 12px #e7548030;
        }

        .photo-frame img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .photo-frame:last-child:nth-child(odd) {
            grid-column: 1 / -1;
            width: 75%;
            height: 180px;
            justify-self: center;
        }

        .photo-frame img:not([src]) {
            display: none;
        }

        .photo-frame img[src=""] {
            display: none;
        }

        .photo-error {
            display: none;
            height: 100%;
            padding: 12px;
            color: #d63384;
            font-size: 14px;
            align-items: center;
            justify-content: center;
        }

        .floating-heart {
            position: fixed;
            bottom: -50px;
            pointer-events: none;
            z-index: 1;
            animation: floatUp 5s linear forwards;
        }

        @keyframes beat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.15); }
        }

        @keyframes floatUp {
            to {
                transform: translateY(-110vh) rotate(360deg);
                opacity: 0;
            }
        }

        @keyframes appear {
            from {
                opacity: 0;
                transform: translateY(15px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 380px) {
            .card {
                padding: 22px 14px;
            }

            .photo-frame {
                height: 145px;
            }

            .photo-frame:last-child:nth-child(odd) {
                height: 160px;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                scroll-behavior: auto !important;
            }
        }
    </style>
</head>

<body>
    <main class="card">
        <div class="big-heart">💗</div>

        <h1>Hi, MOMMYKO! 🥹</h1>

        <p>
            I made this little app just for you.
            I want you to know how special you are to me. 💕
        </p>

        <h2>I LOVE YOU SO MUCH MOMMYKO 😘❤️</h2>

        <h2>Our Little Memories 📸💗</h2>

        <p>My favorite moments are the ones with you! 🥹💕</p>

        <div class="gallery">
            {% for photo in photos %}
            <div class="photo-frame">
                <img
                    src="{{ url_for('static', filename=photo) }}"
                    alt="Our special memory"
                    loading="lazy"
                    onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';"
                >
                <div class="photo-error">
                    Photo not found: {{ photo }}
                </div>
            </div>
            {% endfor %}
        </div>

        <p>
            You make me smile.<br>
            You make my days brighter.<br>
            And you make my heart happy. 🫶
        </p>

        <button type="button" onclick="openSurprise()">
            Open Your Surprise 💌
        </button>

        <section id="surprise" hidden>
            <h2>MWAAAA! 😘💋</h2>

            <p>
                I LOVE YOU SO MUCH MOMMYKO! 💖<br><br>
                Thank you for being part of my life.<br>
                Even on difficult days, I want us to keep
                understanding, supporting, and choosing each other.<br><br>
                If I could choose all over again,<br>
                I would still choose YOU. 🥹💕
            </p>

            <h2>FOREVER YOURS 💗</h2>

            <button type="button" onclick="moreLove()">
                MORE LOVE!! 💞
            </button>

            <p id="extra" aria-live="polite"></p>
        </section>
    </main>

    <script>
        let heartInterval;

        function createHeart() {
            const heart = document.createElement("div");
            heart.className = "floating-heart";

            const hearts = ["❤️", "💗", "💕", "💖", "💘", "🩷"];
            heart.textContent =
                hearts[Math.floor(Math.random() * hearts.length)];

            heart.style.left = Math.random() * 100 + "vw";
            heart.style.fontSize = (20 + Math.random() * 25) + "px";
            heart.style.animationDuration = (3 + Math.random() * 4) + "s";

            document.body.appendChild(heart);

            setTimeout(() => heart.remove(), 7000);
        }

        function openSurprise() {
            const surprise = document.getElementById("surprise");
            surprise.hidden = false;
            surprise.style.display = "block";

            for (let i = 0; i < 30; i++) {
                setTimeout(createHeart, i * 70);
            }
        }

        function moreLove() {
            document.getElementById("extra").textContent =
                "I LOVE YOU I LOVE YOU I LOVE YOU SOOO MUCHHH!! " +
                "MWAAAA MWAAAA MWAAAA!! 😘❤️💗💕💖";

            for (let i = 0; i < 25; i++) {
                setTimeout(createHeart, i * 60);
            }
        }

        if (!window.matchMedia(
            "(prefers-reduced-motion: reduce)"
        ).matches) {
            heartInterval = setInterval(createHeart, 1200);
        }
    </script>
</body>
</html>
    """, photos=photos)


if __name__ == "__main__":
    app.run(debug=True)