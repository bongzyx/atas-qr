from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)


def escape_special_characters(value):
    special_characters = ["\\", ";", ",", '"', ":"]
    for char in special_characters:
        value = value.replace(char, "\\" + char)
    return value


def generate_wifi_syntax(
    auth_type,
    ssid,
    password="",
    hidden=False,
    eap_method="",
    anonymous_identity="",
    identity="",
    phase2_method="",
):
    wifi_syntax = "WIFI:"
    params = []

    # Authentication type
    if auth_type:
        params.append("T:" + auth_type)

    # Network SSID
    params.append("S:" + escape_special_characters(ssid))

    # Password
    if auth_type != "nopass":
        params.append("P:" + escape_special_characters(password))

    # Hidden SSID
    if hidden:
        params.append("H:true")

    # WPA2-EAP parameters
    if auth_type == "WPA2-EAP":
        if eap_method:
            params.append("E:" + eap_method)
        if anonymous_identity:
            params.append("A:" + escape_special_characters(anonymous_identity))
        if identity:
            params.append("I:" + escape_special_characters(identity))
        if phase2_method:
            params.append("PH2:" + phase2_method)

    wifi_syntax += ";".join(params) + ";;"
    return wifi_syntax


def generate_qr_code(data):
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()
    qr_image = qr.make_image(fill_color="black", back_color="white")
    byte_stream = io.BytesIO()
    qr_image.save(byte_stream, format="PNG")
    byte_stream.seek(0)

    # Convert the byte stream to a base64 string
    base64_image = base64.b64encode(byte_stream.read()).decode("utf-8")

    return base64_image


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        auth_type = request.form["auth_type"]
        ssid = request.form["ssid"]
        password = request.form["password"]
        hidden = "hidden" in request.form
        eap_method = request.form["eap_method"]
        anonymous_identity = request.form["anonymous_identity"]
        identity = request.form["identity"]
        phase2_method = request.form["phase2_method"]

        syntax = generate_wifi_syntax(
            auth_type,
            ssid,
            password,
            hidden,
            eap_method,
            anonymous_identity,
            identity,
            phase2_method,
        )
        qr_code = generate_qr_code(syntax)

        return render_template("index.html", syntax=syntax, qr_code=qr_code)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
