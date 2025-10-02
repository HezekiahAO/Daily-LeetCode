from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def call():
    correct_answer = "Flask can be used to create a simple web server"
    message = ""
    if request.method == "POST":
        answer = request.form.get("answer", "")
        if answer.lower() == correct_answer.lower():
            message = "Correct! You can use Flask to create a simple web server."
        else:
            message = "Incorrect! Try again."
    return f"""
        <form method="post">
            <label>What can Flask be used for?</label><br>
            <input type="text" name="answer" required>
            <input type="submit" value="Submit">
        </form>
        <p>{message}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)