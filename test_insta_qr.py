import insta_module

# 1. Generate QR for your own Insta (default)
insta_module.generate_insta_qr()

# 2. Generate QR using a username
insta_module.generate_insta_qr("virat.kohli")

# 3. Generate QR using a full URL
insta_module.generate_insta_qr("https://www.instagram.com/cristiano")