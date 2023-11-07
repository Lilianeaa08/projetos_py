import cv2
from pyzbar.pyzbar import decode
import streamlit as st

def read_qrcode_from_webcam():
    camera = cv2.VideoCapture(0)

    st.write("Aguardando leitura do QR Code...")
    stframe = st.empty()

    while True:
        _, frame = camera.read()

        # Convert the frame to grayscale for QR code detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Get QR code data
        qr_codes = decode(gray_frame)

        # If QR codes are found, process the data
        if qr_codes:
            for qr_code in qr_codes:
                qr_code_data = qr_code.data.decode('utf-8')
                st.write("QR Code data:", qr_code_data)
                save_to_file(qr_code_data)
        
        # Display the video capture with a window named 'QR Code Reader'
        stframe.image(frame, channels='BGR', use_column_width=True)

        # Check for key press 'q' to exit the loop and close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    camera.release()
    cv2.destroyAllWindows()

def save_to_file(qr_code_data):
    with open("qr_code_result.txt", "w") as file:
        file.write(qr_code_data)

def main():
    st.title("Leitura de QR Code")
    st.write("Criado por: Liliane Araujo")
    st.write("---")
    read_qrcode_from_webcam()


if __name__ == "__main__":
    main()
