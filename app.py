
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
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
            overflow: hidden;
            font-family: 'Trebuchet MS', sans-serif;
            background: linear-gradient(135deg, #ffd6e7, #ffb6d1, #fff0f5);
            color: #d63384;
        }

        .card {
            width: 90%;
            max-width: 450px;
            max-height: 90vh;
            overflow-y: auto;
            text-align: center;
            padding: 30px 24px;
            border: 3px solid white;
            border-radius: 30px;
            background: rgba(255, 255, 255, 0.85);
            box-shadow: 0 10px 40px #e7548050;
            position: relative;
            z-index: 2;
        }

        .big-heart {
            font-size: 75px;
            animation: beat 1s infinite;
        }

        h1 {
            font-size: 30px;
            margin: 12px 0;
        }

        h2 {
            color: #ff4081;
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
            transition: 0.3s;
        }

        button:hover {
            background: #e91e63;
            transform: scale(1.05);
        }

        #surprise {
            display: none;
            animation: appear 1s ease;
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
            50% { transform: scale(1.2); }
        }

        @keyframes floatUp {
            to {
                transform: translateY(-110vh) rotate(360deg);
                opacity: 0;
            }
        }

        @keyframes appear {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>

<body>
    <div class="card">
        <div class="big-heart">💗</div>

        <h1>Hi, MOMMYKO! 🥹</h1>

        <p>
            I made this little app just for you.
            I want you to know how special you are to me. 💕
        </p>

        <h2>I LOVEYOUSOMUCHMOMMYKO😘😘😘😘😘😘😘😘😘😘😘😘😘😘!! ❤️</h2>

        <p>
            You make me smile.<br>
            You make my days brighter.<br>
            And you make my heart happy. 🫶
        </p>

        <button onclick="openSurprise()">
            Open Your Surprise 💌
        </button>

        <div id="surprise">
            <h2>MWAAAA! 😘💋</h2>

            <p>
                ILOVEYOUMUCMOMMYKO! 💖<br><br>
                Thank you for being part of my life.<br>
                Even on difficult days, I want us to keep
                understanding, supporting, and choosing each other.<br><br>
                If I could choose all over again,<br>
                I would still choose YOU. 🥹💕
            </p>

            <h2>FOREVER YOURS 💗</h2>

            <button onclick="moreLove()">
                MORE LOVE!! 💞
            </button>

            <p id="extra"></p>
        </div>
    </div>

    <script>
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
            document.getElementById("surprise").style.display = "block";

            for (let i = 0; i < 40; i++) {
                setTimeout(createHeart, i * 70);
            }
        }

        function moreLove() {
            document.getElementById("extra").textContent =
                "I LOVE YOU I LOVE YOU I LOVE YOU SOOO MUCHHH!! " +
                "MWAAAA MWAAAA MWAAAA!! 😘❤️💗💕💖";
            
            for (let i = 0; i < 30; i++) {
                setTimeout(createHeart, i * 60);
            }
        }

        setInterval(createHeart, 600);
    </script>
</body>
</html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
