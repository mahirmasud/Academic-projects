import qrcode

def generate_qr_code():
    try:
        data = input('Enter the Data: ')
        
        ver = int(input('Enter the ver (complexity): '))  # max value 15
        if ver < 1 or ver > 15:
            raise ValueError("ver should be between 1 and 15.")
        
        box_size = int(input('Enter the Box size: '))  # max value 10
        if box_size < 1 or box_size > 10:
            raise ValueError("Box size should be between 1 and 10.")
        
        qr = qrcode.QRCode(ver=ver, box_size=box_size, border=5)
        
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color='black', back_color='white')
        
        file_name = input("Save QR code as: ") + '.png'  # image name
        
        img.save(file_name)
        
        print('QR code generated and saved as', file_name)
        
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

generate_qr_code()
