import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
from PIL import Image, ImageTk

from downloader.linkValidator.linkValidator import validateLink


class YTDownloader:
    def __init__(self, title: str, width_height: str):

        self.__root = tk.Tk()
        self.__root.title(title)
        self.__root.geometry(width_height)

        self.canvas = tk.Canvas(self.__root, width=700, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.__root.after(10, self.__set_background, Path.home() / "Desktop" / "PracticeForInterviews"
                          / "youtube downloader - application code" / "background.png")

        self.__text_input = tk.Entry(self.__root, width=256)  # width = nr of characters allowed in the link
        self.placeTextLabelInput(150, 350, 400, 20)

        self.PutTextOnInterface("Put the link to your video/playlist in the box below", 100, 310)
        self.PutTextOnInterface("Select video(s) format", 230, 190)

        self.__downloadButton()

        self.__format_var = StringVar(self.__root)
        self.__formatMenu()

    def __set_background(self, img_path) -> None:
        '''
        the function that sets the background image of the interface
        :param img_path: path-uh to the background image that we want to set
        :return:
        '''
        try:
            image = Image.open(img_path)
            image = image.resize((700, 500), Image.LANCZOS)
            self.bg_image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load background image: {e}")

    def placeTextLabelInput(self, coord_x: int, coord_y: int, width: int, height: int) -> None:
        '''
        the function that puts the text label on the interface
        :param coord_x: x coordonate for text label
        :param coord_y: y coordonate
        :param width: width of the text label
        :param height: height of the text label
        :return:
        '''
        self.__text_input.place(x=coord_x, y=coord_y, width=width, height=height)

    def getTextFromLabelInput(self) -> str:
        '''
        the function that returns what you are typing in the text label, in our case, we want to
        get the link to the video/playlist from it
        :return:
        '''
        return self.__text_input.get()

    def PutTextOnInterface(self, text, coord_x, coord_y) -> None:
        '''
        the function that lets you write on the interface
        :param text: what will be shown on the interface
        :param coord_x: x coordonate of where the text is placed
        :param coord_y: y coordonate of where the text is placed
        :return:
        '''
        label_afisare = tk.Label(self.__root, text=text, font=("Arial", 16, "bold"))
        label_afisare.place(x=coord_x, y=coord_y)

    def __downloadLogic(self) -> None:
        '''
        the function that defines the logic of the download button
        :return: None
        '''
        try:
            save_path = Path.home() / "Desktop"
            youtube_link = self.getTextFromLabelInput()
            validator = validateLink()
            validator.validator(youtube_link)
            if youtube_link:
                format = self.__getSelectedFormat()
                # print(format)

                logs = None
                if format == ".mp4 - Video":
                    logs = self.__downloadVideo(youtube_link, save_path)
                elif format == ".mp3 - Audio" and self.__isLinkAPlaylist(youtube_link) is False:
                    logs = self.__downloadAudio(youtube_link, save_path)
                else:
                    logs = self.__downloadAudioPlaylist(youtube_link, save_path)
                # print(logs)
                messagebox.showinfo("Success", "Your file have been downloaded!!")
            else:
                messagebox.showwarning("Error", "Please enter a valid link!")

        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    @staticmethod
    def __downloadVideo(video_url, save_path) -> str:
        '''
        the function that performs the download of a youtube video
        :param video_url: link of the video
        :param save_path: save path is Desktop
        :return: returns the logs after the download
        '''
        save_path = save_path / "Video Downloads"
        command = [
            'C:\Python312\Scripts\youtube-dl.exe',  # path to my youtube-dl.exe file
            '-f', 'best',
            '--verbose',
            '--yes-playlist',
            '-o', str(save_path / "%(title)s.%(ext)s"),
            video_url
        ]
        return subprocess.run(command, capture_output=True, text=True).stderr

    @staticmethod
    def __downloadAudio(video_url, save_path) -> str:
        '''
        the function that performs the download of an audio
        :param video_url: url to the video that we want to save the audio of
        :param save_path: save path is Desktop
        :return: returns the logs after the download
        '''
        save_path = Path(save_path) / "Audio Downloads"
        save_path.mkdir(parents=True, exist_ok=True)
        command = [
            'C:\Python312\Scripts\youtube-dl.exe',  # path to my youtube-dl.exe file
            '-x',  # Extrage doar audio
            '--audio-format', 'mp3',
            '--yes-playlist',
            '--verbose',
            '-o', str(save_path / "%(title)s.%(ext)s"),
            video_url
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        for file in save_path.iterdir():
            if file.suffix != ".mp3":
                new_file = file.with_suffix(".mp3")
                file.rename(new_file)

        return result.stderr

    @staticmethod
    def __downloadAudioPlaylist(video_url, save_path) -> str:
        '''
        the function that performs the download of a playlist in audio mp3 format
        :param video_url: link to your playlist
        :param save_path: save path is Desktop
        :return: returns the logs after the download
        '''
        save_path = Path(save_path) / "Audio Downloads"
        save_path.mkdir(parents=True, exist_ok=True)

        command = [
            'C:\Python312\Scripts\youtube-dl.exe',  # path to my youtube-dl.exe file
            '-f', 'best',
            '--verbose',
            '--yes-playlist',
            '-o', str(save_path / "%(title)s.%(ext)s"),
            video_url
        ]

        result = subprocess.run(command, capture_output=True, text=True)

        for file in save_path.iterdir():
            if file.suffix != ".mp3":
                new_file = file.with_suffix(".mp3")
                file.rename(new_file)

        return result.stderr

    def __downloadButton(self) -> None:
        '''
        function that puts the download button on the interface
        :return:
        '''
        buton = tk.Button(self.__root, text="Download", command=self.__downloadLogic, width=10, height=3)
        buton.place(x=300, y=400)

    def __formatMenu(self) -> None:
        '''
        function that puts the format menu on the interface
        :return:
        '''
        self.__format_var.set(".mp4 - Video")  # default value
        # the option menu
        self.format_menu = OptionMenu(self.__root, self.__format_var, ".mp4 - Video", ".mp3 - Audio")
        self.format_menu.place(x=290, y=230)

    def __getSelectedFormat(self) -> str:
        '''

        :return: returns the format that is selected in the format menu
        '''
        return self.__format_var.get()

    @staticmethod
    def __isLinkAPlaylist(youtube_link) -> bool:
        '''
        checks if a link is a playlist
        :param youtube_link: playlist link
        :return: true if it is, else false
        '''
        return youtube_link.startswith("https://www.youtube.com/playlist?list=")

    def runProgram(self) -> None:
        '''
        the function that starts the program
        :return:
        '''
        self.__root.mainloop()
