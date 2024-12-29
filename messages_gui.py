import customtkinter

def sucess_message():
    success_window = customtkinter.CTkToplevel()
    success_window.title("Success")
    success_window.geometry("300x150")
    
    label = customtkinter.CTkLabel(success_window, text="Conversion Successful!")
    label.pack(pady=20)
    
    button_ok = customtkinter.CTkButton(success_window, text="OK", command=success_window.destroy)
    button_ok.pack(pady=20)

def no_file_selected_message():
    error_window = customtkinter.CTkToplevel()
    error_window.title("Error")
    error_window.geometry("300x150")
    
    label = customtkinter.CTkLabel(error_window, text="No file selected!")
    label.pack(pady=20)
    
    button_ok = customtkinter.CTkButton(error_window, text="OK", command=error_window.destroy)
    button_ok.pack(pady=20)

def no_directory_frames_found():
    error_window = customtkinter.CTkToplevel()
    error_window.title("Error")
    error_window.geometry("300x150")
    
    label = customtkinter.CTkLabel(error_window, text="Frames directory not found!")
    label.pack(pady=20)
    
    button_ok = customtkinter.CTkButton(error_window, text="OK", command=error_window.destroy)
    button_ok.pack(pady=20)

def no_directory_ascii_found():
    error_window = customtkinter.CTkToplevel()
    error_window.title("Error")
    error_window.geometry("300x150")
    
    label = customtkinter.CTkLabel(error_window, text="ASCII directory not found!")
    label.pack(pady=20)
    
    button_ok = customtkinter.CTkButton(error_window, text="OK", command=error_window.destroy)
    button_ok.pack(pady=20)