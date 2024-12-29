import customtkinter
import subprocess
import os
from messages_gui import sucess_message, no_file_selected_message
from generate_ascii_frames import convert_frames_to_ascii
from ascii_player import run_ascii_player
    
    
customtkinter.set_appearance_mode("dark")

selected_file_path = None

# Execução do ffmpeg para conversão do vídeo em frames
def convert_video_to_frames(file_path):
    output_dir = "frames"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    command = f"ffmpeg -i {file_path} -vf scale=100:50,format=gray {output_dir}/frame_%04d.png"
    subprocess.run(command, shell=True)
    sucess_message()

def upload_mp4():
    global selected_file_path
    selected_file_path = customtkinter.filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])

def confirm_conversion():
    if not selected_file_path:
        no_file_selected_message()
        return
    convert_video_to_frames(selected_file_path)

app = customtkinter.CTk()
app.title("ASCII Player")
app.geometry("600x500")
app.grid_columnconfigure(0, weight=1)

button_upload = customtkinter.CTkButton(app, text="Upload MP4", command=upload_mp4)
button_upload.grid(padx=20, pady=20)

button_confirm = customtkinter.CTkButton(app, text="Convert to Frames", command=confirm_conversion)
button_confirm.grid(padx=20, pady=20)

button_generate = customtkinter.CTkButton(app, text="Generate ASCII Frames", command=convert_frames_to_ascii)
button_generate.grid(padx=20, pady=20)

label = customtkinter.CTkLabel(app, text="FPS")
label.grid(padx=20, pady=(20, 0))

comboBox = customtkinter.CTkComboBox(app, values=["15", "30", "60"])
comboBox.grid(padx=20, pady=(0, 20))

checkbox = customtkinter.CTkCheckBox(app, text="Memory")
checkbox.grid(padx=20, pady=20)

button_run_ascii_player = customtkinter.CTkButton(app, text="Run ASCII Player", command=lambda: run_ascii_player(int(comboBox.get()), checkbox.get()))
button_run_ascii_player.grid(padx=20, pady=20)

app.mainloop()