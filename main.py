from flask import Flask, render_template, request, redirect, url_for, abort
from datetime import datetime
import markdown
import json

app = Flask(__name__)

def json_serial(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

def save_data(data):
    with open("data.json", "w") as file:
        json.dump({"posts": data}, file, default=json_serial, indent=4)

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if isinstance(data, dict) and "posts" in data:
                return data["posts"]
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_audit_data(ip_address, action):
    with open("audit_log.txt", "a") as file:
        file.write(f"IP Address: {ip_address} - Action: {action} - Time: {datetime.now().isoformat()}\n")

def load_blocked_ips():
    try:
        with open("blocked_ips.json", "r") as file:
            blocked_ips = json.load(file)
            return blocked_ips if isinstance(blocked_ips, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_blocked_ips(blocked_ips):
    with open("blocked_ips.json", "w") as file:
        json.dump(blocked_ips, file, indent=4)

def get_client_ip():
    if request.headers.getlist("X-Forwarded-For"):
        # Pega a primeira parte da lista dividida por vírgulas
        ip_address = request.headers.getlist("X-Forwarded-For")[0].split(",")[0].strip()
    else:
        ip_address = request.environ.get('REMOTE_ADDR')
    return ip_address

blocked_ips = load_blocked_ips()

def check_blocked_ip():
    client_ip = get_client_ip()
    if client_ip in blocked_ips:
        return render_template("blocked.html")
    return None

@app.before_request
def handle_blocked_ip():
    blocked_template = check_blocked_ip()
    if blocked_template:
        response = app.make_response(blocked_template)
        response.status_code = 403  # Status 403 Forbidden
        return response

posts = load_data()

@app.route("/")
def index():
    ip_address = get_client_ip()
    timestamp = datetime.now().isoformat()
    save_audit_data(ip_address, "Accessed homepage")

    sorted_posts = sorted(posts, key=lambda x: datetime.fromisoformat(x['timestamp']), reverse=True)
    return render_template("index.html", posts=sorted_posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)

    if post:
        post['content'] = markdown.markdown(post['content'], extensions=['markdown.extensions.fenced_code'])
        ip_address = get_client_ip()
        save_audit_data(ip_address, f"Accessed post {post_id}")
        return render_template("post.html", post=post)

    return "Post não encontrado", 404

@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")

        ip_address = get_client_ip()
        save_audit_data(ip_address, "Created a new post")

        new_post = {
            "id": len(posts) + 1,
            "title": title,
            "content": content,
            "author": author,
            "timestamp": datetime.now().isoformat(),
            "comments": [],
            "ip_address": ip_address  # Adiciona a informação do endereço IP ao post
        }

        posts.append(new_post)
        save_data(posts)

        return redirect(url_for("index"))

    return render_template("create_post.html")

@app.route("/post/<int:post_id>/add_comment", methods=["POST"])
def add_comment(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)

    if post:
        comment_author = request.form.get("comment_author")
        comment_content = request.form.get("comment_content")

        ip_address = get_client_ip()
        save_audit_data(ip_address, f"Added a comment to post {post_id}")

        new_comment = {
            "author": comment_author,
            "content": comment_content,
            "ip_address": ip_address  # Adiciona a informação do endereço IP ao comentário
        }

        post["comments"].append(new_comment)
        save_data(posts)

    return redirect(url_for("post", post_id=post_id))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
