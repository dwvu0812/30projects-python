import qrcode


class MyQR:
    def __init__(self, size: int, padding: int) -> None:
        self.qr = qrcode.QRCode(
            box_size=size,
            border=padding,
        )

    def create_qr(self, fileName: str, fg: str, bg: str) -> str:
        userInput = input("Enter text: ")
        try:
            print("Creating QR code...")
            self.qr.add_data(userInput)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(fileName)
            print(f"QR code saved as {fileName}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    qr = MyQR(10, 5)
    qr.create_qr("qr.png", "black", "green")
