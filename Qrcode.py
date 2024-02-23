import qrcode
from PIL import Image, ImageTk
import tkinter as tk

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def display_qr_code(filename):
    root = tk.Tk()
    root.title("QR Code")
    
    # Open the image file
    img = Image.open(filename)
    
    # Convert image for Tkinter
    img_tk = ImageTk.PhotoImage(img) 
    
    # Create a label with the image
    label = tk.Label(root, image=img_tk)
    label.pack()
    
    # Function to destroy the root window after 15 seconds
    def destroy_window():
        root.destroy()

    # Schedule the destruction of the window after 15 seconds
    root.after(10000, destroy_window)
    
    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    # Generate a QR code with payment information
    payment_info = "Successful Payment"
    generate_qr_code(payment_info, "payment_qr_code.png")
    print("QR code generated successfully.")
