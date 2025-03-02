import qrcode

# Project link
project_link = "https://setayeshsaeidnia.github.io/Setayesh/"

# Generate QR Code
qr = qrcode.make(project_link)

# Save QR Code as an image file
qr.save("project_qr.png")

print("QR Code generated and saved as 'project_qr.png'")