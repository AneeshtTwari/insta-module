import qrcode

def generate_insta_qr(username_or_url=None):
    """
    Generates and saves a QR code for:
    - A username (e.g., 'virat.kohli')
    - A full Instagram URL
    - Or uses Aneesh's profile by default
    """
    if username_or_url is None:
        # Default: Aneesh's full Instagram link
        url = "https://www.instagram.com/aneeshhtiwarii?igsh=MXQ1aHQ5ejk2Z2o3Nw%3D%3D&utm_source=qr"
        filename = "aneeshhtiwarii_qr.png"
    elif username_or_url.startswith("http"):
        url = username_or_url
        filename = "custom_url_qr.png"
    else:
        url = f"https://www.instagram.com/{username_or_url}"
        filename = f"{username_or_url}_qr.png"

    qr = qrcode.make(url)
    qr.save(filename)
    print(f"✅ QR code saved as '{filename}' for: {url}")