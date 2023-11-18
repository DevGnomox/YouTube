import sys
import os
from moviepy import *
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QPixmap, QIcon
from tela import Ui_Dialog
from PyQt6.QtWidgets import *
import logging
from pytube import YouTube, Playlist
from pydub import AudioSegment
import logging
import datetime
from pytube.exceptions import VideoUnavailable
from pydub import AudioSegment
import threading
from pytube.exceptions import RegexMatchError, VideoUnavailable
from qdarkstyle import load_stylesheet_pyqt6
from PyQt6.QtCore import QSettings
import platform



project_dir = os.path.dirname(os.path.abspath(__file__))

ffprobe_path = os.path.join(project_dir, "ffprobe")
ffplay_path = os.path.join(project_dir, "ffplay")
ffmpeg_path = os.path.join(project_dir, "ffmpeg")

os.environ['PATH'] = ffprobe_path + os.pathsep + ffplay_path + os.pathsep + ffmpeg_path + os.pathsep + os.environ['PATH']

save_path = os.path.expanduser("~/Desktop")


file_path = "Termos_de_Uso.txt"
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.readlines()  # Lê o arquivo e divide o conteúdo em uma lista de linhas
except FileNotFoundError:
    file_content = ["Arquivo não encontrado."]

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class GUI_cont(QMainWindow, Ui_Dialog):

    update_list_signal = QtCore.pyqtSignal(str)
    update_list_signal2 = QtCore.pyqtSignal(str)
    update_progress_signal = QtCore.pyqtSignal(int)
    update_progress_signal2 = QtCore.pyqtSignal(int)
    

    def __init__(self, parent = None) -> None:
        _translate = QtCore.QCoreApplication.translate
        super().__init__(parent)
        super().setupUi(self)

        
        


        self.settings = QSettings("MyApp", "MyProgram")
        self.radioButton_tema.toggled.connect(self.toggle_theme)
        self.radioButton_tema2.toggled.connect(self.toggle_theme)
        self.radioButton_tema.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.radioButton_tema2.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.buttonBox_4.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.radioButton_tema2.setChecked(True)
        

        self.update_list_signal.connect(self.update_list_widget)
        self.update_list_signal2.connect(self.update_list_widget2)
        self.update_progress_signal.connect(self.update_progress)
        self.update_progress_signal2.connect(self.update_progress2)

        #icone_png="icone.png"
        #icone = os.path.dirname(os.path.abspath(__file__))
        #caminho_icone = os.path.join(icone, icone_png)

        #self.setWindowIcon(QIcon(caminho_icone))

        for line in file_content:
            self.listWidget_3.addItem(line.strip())
        if not file_content:
            self.listWidget_3.addItem("Arquivo vazio.")

        self.update_progress_signal.emit(0)
        self.update_progress_signal2.emit(0)

        
        self.log.debug("Iniciando sistema")
        self.update_list_signal.emit(current_time + " - Iniciando sistema")
        self.update_list_signal.emit(current_time + " - Sistema Pronto")
        self.update_list_signal2.emit(current_time + " - Iniciando sistema")
        self.update_list_signal2.emit(current_time + " - Sistema Pronto")

        self.label_yt.setPixmap(QPixmap("yt.png"))
        self.label_yt.setScaledContents(True)
        self.label_yt2.setPixmap(QPixmap("music.png"))
        self.label_yt2.setScaledContents(True)
        self.pushButton_2.clicked.connect(self.choose_directory)
        self.pushButton.clicked.connect(self.choose_directory)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.download_music)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.close)
        self.buttonBox_2.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.close)
        self.buttonBox_3.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.close)
        self.buttonBox_4.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.close)
        self.buttonBox_3.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.switch)
        self.buttonBox_4.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.switch)
        self.buttonBox_2.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self.video_baixar)

    def update_list_widget(self, message):
        self.log.debug("iniciando update_list_widget")
        self.listWidget.addItem(message)
        self.listWidget.scrollToBottom()
    
    def update_list_widget2(self, message2):
        self.log.debug("iniciando update_list_widget2")
        self.listWidget_2.addItem(message2)
        self.listWidget_2.scrollToBottom()

    def update_progress(self, value):
        self.log.debug("iniciando update_progress")
        self.progressBar.setValue(value)

    def update_progress2(self, value2):
        self.log.debug("iniciando update_progress2")
        self.progressBar_2.setValue(value2)


    def apply_style(self, dark_mode):
        self.log.debug("iniciando apply_style")
        if dark_mode:
            self.setStyleSheet(load_stylesheet_pyqt6())
        else:
            self.setStyleSheet("")  # Reverta para o estilo padrão

    def load_settings(self):
        self.log.debug("iniciando load_settings")
        dark_mode = self.settings.value("dark_mode", type=bool)
        if dark_mode is None:
            dark_mode = False  # Use o tema claro como padrão
        self.apply_style(dark_mode)
        self.radioButton_tema.setChecked(dark_mode)
        self.radioButton_tema2.setChecked(not dark_mode)

    def save_settings(self):
        self.log.debug("iniciando save_settings")
        self.log.debug("Tema salvo")
        self.update_list_signal.emit(current_time + " - Tema salvo")
        self.update_list_signal2.emit(current_time + " - Tema salvo")
        self.settings.setValue("dark_mode", self.radioButton_tema.isChecked())

    def toggle_theme(self, checked):
        self.log.debug("O tema foi alterado")
        if checked:
            if self.radioButton_tema.isChecked():
                self.apply_style(dark_mode=True)
                self.log.debug("Tema escuro")
                self.update_list_signal.emit(current_time + " - Tema alterado")
                self.update_list_signal.emit(current_time + " - Tema escuro selecionado")
                self.update_list_signal2.emit(current_time + " - Tema alterado")
                self.update_list_signal2.emit(current_time + " - Tema escuro selecionado")
            else:
                self.apply_style(dark_mode=False)
                self.log.debug("Tema claro")
                self.update_list_signal.emit(current_time + " - Tema alterado")
                self.update_list_signal.emit(current_time + " - Tema Claro selecionado")
                self.update_list_signal2.emit(current_time + " - Tema alterado")
                self.update_list_signal2.emit(current_time + " - Tema Claro selecionado")
            self.save_settings()



    def switch(self):
        self.tabWidget.setCurrentIndex(0)

    def choose_directory(self):
        global save_path
        save_path = QtWidgets.QFileDialog.getExistingDirectory()
        self.label_7.setText(save_path)
        self.label_5.setText(save_path)
        self.log.debug("Diretorio de salvamento selecionado")
        self.update_list_signal.emit(current_time + " - Diretorio de salvamento selecionado")
        self.update_list_signal2.emit(current_time + " - Diretorio de salvamento selecionado")

    def download_music(self):
        self.update_progress_signal.emit(0)
        global save_path
        self.update_progress_signal.emit(10)
        url = self.lineEdit.text()
        self.log.debug("Iniciando dowload_music")
        self.update_list_signal.emit(current_time + " - Iniciando")

        if self.checkBox.isChecked():
            self.update_progress_signal.emit(15)
            self.log.debug("Termos de uso aceito")
            self.update_list_signal.emit(current_time + " - Termos de uso aceito")
            if not self.is_valid_youtube_url(url):
                
                self.log.debug("URL invalida")
                self.show_error_message("URL inválido do YouTube")
                self.update_list_signal.emit(current_time + " - URL do YouTube invalido")
                return
            elif not save_path:  
                save_path = os.path.expanduser("~/Desktop")
                self.log.debug("Diretorio padrão selecionado (Desktop)")
                self.update_list_signal.emit(current_time + " - Diretorio padrão seleionado (Desktop)")
            elif 'playlist' in url:
                self.update_progress_signal.emit(20)
                self.log.debug("URL Playlist utilizado")
                self.update_list_signal.emit(current_time + " - Iniciando Download")
                self.update_list_signal.emit(current_time + " - URL YouTube Playlist")
                self.update_list_signal.emit(current_time + " - Será baixado todas as musicas da Playlist")
                playlist = Playlist(url)
                for video_url in playlist.video_urls:
                    self.update_progress_signal.emit(25)
                    self.log.debug("Iniciando URL Playlist")
                    self.update_list_signal.emit(current_time + " - Download...")
                    quality = self.comboBox_music.currentText()
                    quality = quality.split(" (")[0] 
                    self.log.debug(f"Qaulidade selecionada: {quality}")
                    self.update_list_signal.emit(current_time + f" - Qualidade selecionada: {quality} ")
                    self.log.debug("Iniciando Threading")
                    self.update_list_signal.emit(current_time + " - Processo executando em segundo plano")
                    self.update_progress_signal.emit(35)
                    download_thread = threading.Thread(target=self.download_video, args=(video_url, save_path, quality))
                    download_thread.start()
                    self.log.debug("Threading iniciado")

            else:
                self.update_progress_signal.emit(36)
                self.log.debug("URL padrão utilizado")
                self.update_list_signal.emit(current_time + " - Iniciando Download")
                self.update_list_signal.emit(current_time + " - URL Padrão")
                quality = self.comboBox_music.currentText()
                quality = quality.split(" (")[0] 
                self.log.debug(f"Qualidade selecionada: {quality}")
                self.update_list_signal.emit(current_time + f" - Qualidade selecionada: {quality}")
                self.log.debug("Iniciando Threading")
                self.update_list_signal.emit(current_time + " - Processo executando em segundo plano")
                self.update_progress_signal.emit(40)
                download_thread = threading.Thread(target=self.download_video, args=(url, save_path, quality))
                download_thread.start()
                self.log.debug("Threading iniciada ")
        else:
            self.log.debug("Termos de uso não aceitos")
            self.show_error_message("Os termos de uso devem ser aceitos")
            self.update_list_signal.emit(current_time + " - Os termos de uso devem ser aceitos")
        
    def is_valid_youtube_url(self, url):
        self.log.debug("Iniciando is_valid_youtube_url")
        self.log.debug(f"URL informada - {url}")
        if not url:
            self.log.debug("Não foi informado um link")
            self.update_list_signal.emit(current_time + " - Falta o link no campo indicado")
            self.update_list_signal2.emit(current_time + " - Falta o link no campo indicado")
            return False  # URL vazio é considerado inválido

        if 'playlist' in url:
            try:
                playlist = Playlist(url)
                return len(playlist.video_urls) > 0
            except VideoUnavailable:
                self.log.debug("Link informado esta quebrado, não existe ou esta bloqueado")
                self.update_list_signal.emit(current_time + " - Playlist não disponível ou foi removida")
                self.update_list_signal2.emit(current_time + " - Playlist não disponível ou foi removida")
                return False
        else:
            try:
                video = YouTube(url)
                return video.streams.filter(only_audio=True).first() is not None
            except (RegexMatchError, VideoUnavailable):
                self.log.debug("Link invalido ou não disponivel")
                self.update_list_signal.emit(current_time + " - URL do YouTube inválida ou vídeo não disponível")
                self.update_list_signal2.emit(current_time + " - URL do YouTube inválida ou vídeo não disponível")
                return False


    def show_error_message(self, message):
        self.log.debug("Iniciando show_error_message")
        self.log.debug("Mensagem de aviso gerada")
        self.log.debug(f"Mensagem - {message}")
        self.update_list_signal.emit(current_time + f" - Mensagem de aviso gerada - {message}")
        self.update_list_signal2.emit(current_time + f" - Mensagem de aviso gerada - {message}")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Erro")
        msg.exec()

    def download_video(self, url, save_path, quality="Qualidade Padrão"):
        self.update_progress_signal.emit(48)

        self.log.debug("Iniciando download_video")
        self.log.debug("URL valida")
        self.update_list_signal.emit(current_time + " - Iniciando processo")
        self.update_list_signal.emit(current_time + " - URL valida")

        yt = YouTube(url)
        stream = self.select_audio_stream(yt, quality)

        if stream:
            video_file = stream.download(output_path=save_path)

            if save_path and isinstance(save_path, str):
                self.log.debug("convertendo arquivo")
                self.update_list_signal.emit(current_time + " - Convertendo arquivo")

                file_name = yt.title + ".mp3"
                file_name = ''.join(char for char in file_name if char.isalnum() or char in (' ', '.', '-'))
                self.log.debug("caracteres não permitidos removidos")
                self.update_list_signal.emit(current_time + " - Caracteres não permitidos removidos do titulo")

                audio_file = os.path.join(save_path, file_name)
                audio = AudioSegment.from_file(video_file)
                self.update_progress_signal.emit(79)
                if quality == "Qualidade Padrão":
                    audio.export(audio_file, format="mp3", bitrate="128k")
                elif quality == "Qualidade Media":
                    self.update_list_signal.emit(" aqui fdp")
                    audio.export(audio_file, format="mp3", bitrate="192k")
                elif quality == "Alta Qualidade":
                    audio.export(audio_file, format="mp3", bitrate="256k")
                elif quality == "Qualidade Máxima":
                    audio.export(audio_file, format="mp3", bitrate="320k")

            if os.path.exists(video_file):
                self.update_progress_signal.emit(93)
                os.remove(video_file)
                self.update_list_signal.emit(current_time + " - Arquivos temporarios removidos")
                self.log.debug("Arquivos temporarios removidos")

        self.update_progress_signal.emit(100)
        self.update_list_signal.emit(current_time + " - Conversão concluida")
        self.update_list_signal.emit(current_time + " - Musica baixada")
        self.update_list_signal.emit(current_time + " - -------------------------")
        self.update_list_signal.emit(current_time + f" - Musica - {yt.title}")
        self.update_list_signal.emit(current_time + " - -------------------------")
        self.update_list_signal.emit(current_time + " - Fim do Processo")
        self.log.debug(f"Musica baixada - {yt.title}")

        title = "Download Concluído"
        message = "O download foi concluído com sucesso."

        self.notificacao(title, message)
        

        


    def download_terms_of_service(self):
      
        terms_of_service_path = "Termos de uso.pdf"

        save_path2, _ = QFileDialog.getSaveFileName(self, "Salvar Termos de Serviço", terms_of_service_path, "Arquivos PDF (*.pdf)")

        if save_path2:
            try:
                with open(terms_of_service_path, "rb") as file:
                    content = file.read()
                    if content:
                        with open(save_path2, "wb") as output_file:
                            output_file.write(content)
                        self.update_list_signal.emit(current_time + " - Termos de Serviço (PDF) baixado com sucesso")
                        self.update_list_signal2.emit(current_time + " - Termos de Serviço (PDF) baixado com sucesso")
                        self.log.debug("Termos de serviço baixados")
                    else:
                        self.update_list_signal.emit(current_time + " - Erro ao baixar os Termos de Serviço (PDF)")
                        self.update_list_signal2.emit(current_time + " - Erro ao baixar os Termos de Serviço (PDF)")
                        self.log.debug("Erro ao baixar termos de serviço")
            except Exception as e:
                self.update_list_signal.emit(current_time + " - Erro ao baixar os Termos de Serviço (PDF): " + str(e))
                self.update_list_signal2.emit(current_time + " - Erro ao baixar os Termos de Serviço (PDF): " + str(e))
                self.log.debug("Erro ao baixar os termos de serviço (PDF): " + str(e))

    save_path = os.path.expanduser("~/Desktop")


    def select_audio_stream(self, yt, quality):
        audio_streams = yt.streams.filter(only_audio=True)

        # Mapeie as qualidades para as taxas de bits correspondentes
        quality_to_bitrate = {
            "Qualidade Padrão": "128kbps",
            "Qualidade Media": "192kbps",
            "Alta Qualidade": "256kbps",
            "Qualidade Máxima": "320kbps"
        }

        if quality in quality_to_bitrate:
            desired_bitrate = quality_to_bitrate[quality]
            
            for stream in audio_streams:
                if stream.abr == desired_bitrate:
                    return stream
        else:
            self.update_list_signal.emit(current_time + " - Qualidade não encontrada")
            self.log.debug("Qualidade não encontrada")

        for stream in audio_streams:
            if stream.abr == "128kbps":
                return stream

        self.update_list_signal.emit(current_time + " - Qualidade Padrão Selecionada")
        self.log.debug("Qualidade padrão selecionada")
        return None
    
#########################################################################################
##############     MUSICA YOUTUBE FIM   #################################################


#########################################################################################
##############     VIDEO YOUTUBE     ####################################################


    def video_baixar(self):
        self.update_progress_signal2.emit(10)
        global save_path
        url2 = self.lineEdit_2.text()
        self.log.debug("Iniciando video_baixar")
        self.update_list_signal2.emit(current_time + " - Iniciando")

        if self.checkBox_2.isChecked():
            self.update_progress_signal2.emit(20)
            self.log.debug("Termos de uso aceito")
            self.update_list_signal2.emit(current_time + " - Termos de uso aceito")
            if not self.is_valid_youtube_url(url2):
                
                self.log.debug("URL invalida")
                self.show_error_message("URL inválido do YouTube")
                self.update_list_signal2.emit(current_time + " - URL do YouTube invalido")
                return
            elif not save_path:  
                save_path = os.path.expanduser("~/Desktop")
                self.log.debug("Diretorio padrão selecionado (Desktop)")
                self.update_list_signal2.emit(current_time + " - Diretorio padrão seleionado (Desktop)")
            elif 'playlist' in url2:
                self.update_progress_signal2.emit(36)
                self.log.debug("URL Playlist utilizado")
                self.update_list_signal2.emit(current_time + " - Iniciando Download")
                self.update_list_signal2.emit(current_time + " - URL YouTube Playlist")
                self.update_list_signal2.emit(current_time + " - Será baixado todos os videos da Playlist")
                playlist = Playlist(url2)
                for video_url in playlist.video_urls:
                    self.log.debug("Iniciando URL Playlist")
                    self.update_list_signal2.emit(current_time + " - Download...")
                    self.log.debug("Iniciando Threading")
                    self.update_list_signal2.emit(current_time + " - Processo executando em segundo plano")

                    self.update_progress_signal2.emit(63)
                    download_thread = threading.Thread(target=self.download_single_video, args=(video_url, save_path))
                    download_thread.start()
                    self.log.debug("Threading iniciado")

            else:
                self.update_progress_signal2.emit(56)
                self.log.debug("URL padrão utilizado")
                self.update_list_signal2.emit(current_time + " - Iniciando Download")
                self.update_list_signal2.emit(current_time + " - URL Padrão")
                self.log.debug("Iniciando Threading")
                self.update_list_signal2.emit(current_time + " - Processo executando em segundo plano")
                
                self.update_progress_signal2.emit(69)
                download_thread = threading.Thread(target=self.download_single_video, args=(url2, save_path))
                download_thread.start()
                self.log.debug("Threading iniciada ")
        else:
            self.log.debug("Termos de uso não aceitos")
            self.show_error_message("Os termos de uso devem ser aceitos")
            self.update_list_signal2.emit(current_time + " - Os termos de uso devem ser aceitos")



    def download_single_video(self, url, save_path):
        self.update_progress_signal2.emit(73)
        self.log.debug("Iniciando download_single_video")
        self.update_list_signal2.emit(current_time + " - Iniciando processo")
        self.update_list_signal2.emit(current_time + " - URL válida")

        yt = YouTube(url)
        file_name = ''.join(char for char in yt.title if char.isalnum() or char in (' ', '.', '-'))

        video_file = yt.streams.get_highest_resolution().download(output_path=save_path)

        self.update_progress_signal2.emit(89)
        if os.path.exists(video_file):
            video_file_cleaned = os.path.join(save_path, file_name + '.mp4')
            os.rename(video_file, video_file_cleaned)
            
            self.update_progress_signal2.emit(100)
            self.update_list_signal2.emit(current_time + " - Vídeo baixado")
            self.update_list_signal2.emit(current_time + " - -------------------------")
            self.update_list_signal2.emit(current_time + f" - Vídeo - {file_name}")
            self.update_list_signal2.emit(current_time + " - -------------------------")
            self.update_list_signal2.emit(current_time + " - Fim do Processo")
            self.log.debug(f"Vídeo baixado - {file_name}")

            title = "Download Concluído"
            message = "O download foi concluído com sucesso."

            self.notificacao(title, message)





#########################################################################################
##############     VIDEO YOUTUBE FIM    #################################################




    def notificacao(self, title, message):
        current_system = platform.system()

        imagem_nome = "icone.png"

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_da_imagem = os.path.join(diretorio_atual, imagem_nome)


        if current_system == "Windows":
            from winotify import Notification, audio

            if self.checkBox_4.isChecked():
                notification = Notification(
                                            app_id="Gnomox",
                                            title=title,
                                            msg=message,
                                            icon=caminho_da_imagem,
                                            )
                
                notification.set_audio(audio.LoopingAlarm, loop=False)
                notification.show()
                self.log.debug("Notificação gerada Windows")
                self.update_list_signal2.emit(current_time + " - Notificação gerada Windows")
                self.update_list_signal.emit(current_time + " - Notificação gerada Windows")
            else:
                self.log.debug("Notificacao desativada")
                self.update_list_signal2.emit(current_time + " - Notificação desativada")
                self.update_list_signal.emit(current_time + " - Notificação desativada")

        elif current_system == "Darwin":  # Para macOS
            from pync import Notifier
            if self.checkBox_4.isChecked():
                Notifier.notify(message, 
                                title=title,
                                sound='Ping',
                                group='Gnomox',
                                execute=f"Open {save_path}",
                                actions=["Abrir Diretório"],
                                app_icon=caminho_da_imagem
                                )
                self.log.debug("Notificação gerada macOS")
                self.update_list_signal2.emit(current_time + " - Notificação gerada macOS")
                self.update_list_signal.emit(current_time + " - Notificação gerada macOS")
            else:
                self.log.debug("Notificacao desativada")
                self.update_list_signal2.emit(current_time + " - Notificação desativada")
                self.update_list_signal.emit(current_time + " - Notificação desativada")
        else:
            if self.checkBox_4.isChecked():
                self.log.debug("Não foi possivel gerar a notificação")
                self.update_list_signal2.emit(current_time + " - Não foi possivel gerar a notificação")
                self.update_list_signal.emit(current_time + " - Não foi possivel gerar a notificação")
            else:
                self.log.debug("Notificacao desativada")
                self.update_list_signal2.emit(current_time + " - Notificação desativada")
                self.update_list_signal.emit(current_time + " - Notificação desativada")











if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='./logsistema.log',
        filemode='w' )
    qt = QApplication(sys.argv)
    qt.setWindowIcon(QIcon(os.path.abspath("icone.png")))
    qt.setApplicationName("Gnomox")
    view = GUI_cont()
    view.show()
    qt.exec()