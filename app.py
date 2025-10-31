from flask import Flask, render_template_string
import os, datetime

app = Flask(__name__)

@app.route("/")
def home():
    build = os.environ.get("BUILD_SHA", "dev")[:7]
    build_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>UW–Stout • CNIT 371</title>
<style>
  :root {
    --stout-navy: #003865;  /* UW–Stout Navy */
    --stout-gold: #F1BE48;  /* UW–Stout Gold */
    --bg: #0a1c2a;
    --card: #0f2a45;
    --text: #ffffff;
    --muted: #c9d7e8;
    --shadow: 0 20px 40px rgba(0,0,0,.25);
  }
  body.light {
    --bg: #f6f9fc;
    --card: #ffffff;
    --text: #0e1726;
    --muted: #4b5b74;
    background: #f6f9fc;
  }
  body {
    margin: 0;
    font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
    color: var(--text);
    background: radial-gradient(1200px 600px at 10% -10%, #004a82 0%, #001d34 60%, #00121f 100%);
    min-height: 100vh; display: grid; place-items: center;
  }
  body.light { background: #f6f9fc; }
  .card {
    width: min(880px, 92vw);
    background: linear-gradient(180deg, var(--card), color-mix(in srgb, var(--card) 88%, #000 12%));
    border-radius: 22px; padding: 28px 28px 22px;
    box-shadow: var(--shadow);
    border: 1px solid color-mix(in srgb, var(--stout-navy) 30%, #fff 70%);
  }
  .badge {
    display:inline-block; padding:6px 12px; border-radius:999px;
    background: var(--stout-gold); color:#1a1a1a; font-weight:700; letter-spacing:.25px;
  }
  h1{ margin:.35rem 0 0.25rem; font-size: clamp(1.8rem, 3vw, 2.3rem); }
  p.lead{ margin:.25rem 0 1.1rem; color: var(--muted); font-size: 1.05rem; }
  .grid{ display:grid; gap:14px; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); margin-top:14px;}
  .panel{
    background: color-mix(in srgb, var(--card) 84%, #fff 16%);
    border:1px solid color-mix(in srgb, var(--stout-navy) 22%, #fff 78%);
    border-radius:16px; padding:14px 16px;
  }
  .btn {
    background: var(--stout-navy); color:#fff; border:none; padding:10px 14px;
    border-radius:12px; font-weight:600; cursor:pointer;
    box-shadow: 0 8px 20px rgba(0,56,101,.35);
  }
  .btn:hover{ filter: brightness(1.05); }
  .row{ display:flex; align-items:center; justify-content:space-between; gap:12px; flex-wrap:wrap;}
  .left h2{ margin:.2rem 0; font-size: clamp(1.4rem, 2.4vw, 1.6rem);}
  .tag{ color: var(--stout-gold); font-weight:700;}
  footer{ margin-top:14px; font-size:.92rem; color:var(--muted);}
  .mono{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }
</style>
</head>
<body>
  <div class="card">
    <div class="row">
      <div class="left">
        <span class="badge">UW–Stout • CNIT 371</span>
        <h1>🚀 Welcome to your Docker + GitHub Actions demo</h1>
        <p class="lead">A clean, UW–Stout–themed Flask app running in a container on EC2.</p>
      </div>
      <button id="theme" class="btn" aria-label="Toggle light/dark mode">🌙 Theme</button>
    </div>

    <div class="grid">
      <div class="panel">
        <h2>Why this matters</h2>
        <p>Every push to <span class="tag">main</span> triggers a build & deploy to EC2. Students see modern DevOps in action.</p>
      </div>
      <div class="panel">
        <h2>Tech stack</h2>
        <p>Flask • Docker • GitHub Actions • AWS EC2</p>
      </div>
      <div class="panel">
        <h2>Status</h2>
        <p>Build: <span class="mono">{{ build }}</span><br/>Built at: <span class="mono">{{ build_time }}</span></p>
      </div>
    </div>

    <footer>
      <strong style="color:var(--stout-gold)">UW–Stout</strong> — Polytechnic • Hands-on • Career-focused
    </footer>
  </div>

<script>
  // light/dark toggle with localStorage
  const key = "cnit371-theme";
  const saved = localStorage.getItem(key);
  if (saved === "light") document.body.classList.add("light");

  document.getElementById("theme").addEventListener("click", () => {
    document.body.classList.toggle("light");
    localStorage.setItem(key, document.body.classList.contains("light") ? "light" : "dark");
  });
</script>
</body>
</html>
    """, build=build or "dev", build_time=build_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
app = Flask(__name__)
@app.route('/')
def hello():

    app.run(host='0.0.0.0', port=5000)
