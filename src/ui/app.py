import customtkinter as ctk
from tkinter import ttk, messagebox
import os
from PIL import Image

from src.core.qr_generator import QRGenerator
from src.data.countries import COUNTRY_CODES
from src.utils.validators import is_valid_email, is_valid_phone, sanitize_filename
from src.utils.helpers import open_url, LINKEDIN_URL

class QRCodeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.qr_generator = QRGenerator()
        self.geometry("600x850")
        self.title("Gerador de QR Code - Enterprise Edition")
        if os.path.exists("Icone.ico"):
            self.iconbitmap("Icone.ico")
        self._setup_ui()

    def _setup_ui(self):
        if os.path.exists("Interface.png"):
            try:
                header_image = ctk.CTkImage(
                    light_image=Image.open("Interface.png"),
                    dark_image=Image.open("Interface.png"),
                    size=(200, 200)
                )
                self.image_label = ctk.CTkLabel(self, image=header_image, text="")
                self.image_label.pack(pady=20)
            except Exception as e:
                pass

        self.label_nome = ctk.CTkLabel(self, text="Digite seu nome:")
        self.label_nome.pack(pady=10)
        self.entrada_nome = ctk.CTkEntry(self, width=250)
        self.entrada_nome.pack(pady=10)

        self.label_ddd = ctk.CTkLabel(self, text="Selecione o DDD do país:")
        self.label_ddd.pack(pady=10)
        self.combobox_ddd = ttk.Combobox(self, values=list(COUNTRY_CODES.keys()), state="readonly")
        self.combobox_ddd.pack(pady=10)
        self.combobox_ddd.current(0)

        self.label_numero = ctk.CTkLabel(self, text="Digite o número de telefone:")
        self.label_numero.pack(pady=10)
        self.entrada_numero = ctk.CTkEntry(self, width=250)
        self.entrada_numero.pack(pady=10)

        self.label_email = ctk.CTkLabel(self, text="Digite o e-mail:")
        self.label_email.pack(pady=10)
        self.entrada_email = ctk.CTkEntry(self, width=250)
        self.entrada_email.pack(pady=10)

        self.label_rede_social = ctk.CTkLabel(self, text="Digite a rede social (URL):")
        self.label_rede_social.pack(pady=10)
        self.entrada_rede_social = ctk.CTkEntry(self, width=250)
        self.entrada_rede_social.pack(pady=10)

        self.botao_gerar = ctk.CTkButton(self, text="Gerar QR Code", command=self._on_generate)
        self.botao_gerar.pack(pady=20)

        self.label_desenvolvido = ctk.CTkLabel(self, text="Desenvolvido por Isllan Toso")
        self.label_desenvolvido.pack(side="bottom", pady=10)

        self.botao_linkedin = ctk.CTkButton(
            self, 
            text="LinkedIn", 
            command=lambda: open_url(LINKEDIN_URL),
            width=100
        )
        self.botao_linkedin.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    def _on_generate(self):
        nome = self.entrada_nome.get().strip()
        ddd_key = self.combobox_ddd.get()
        ddd = COUNTRY_CODES.get(ddd_key, "").split(" ")[-1]
        numero = self.entrada_numero.get().strip()
        email = self.entrada_email.get().strip()
        rede_social = self.entrada_rede_social.get().strip()

        if not nome:
            messagebox.showwarning("Aviso", "Nome obrigatorio")
            return

        try:
            generated_any = False
            safe_name = sanitize_filename(nome)

            if numero:
                if is_valid_phone(numero):
                    telefone = f"{ddd} {numero}"
                    self.qr_generator.generate(telefone, f"{safe_name}_telefone_qrcode.png")
                    generated_any = True
                else:
                    messagebox.showwarning("Aviso", "Telefone invalido")

            if email:
                if is_valid_email(email):
                    self.qr_generator.generate(email, f"{safe_name}_email_qrcode.png")
                    generated_any = True
                else:
                    messagebox.showwarning("Aviso", "E-mail invalido")

            if rede_social:
                self.qr_generator.generate(rede_social, f"{safe_name}_rede_social_qrcode.png")
                generated_any = True

            if generated_any:
                messagebox.showinfo("Sucesso", "Gerado em Qr_code")
            else:
                messagebox.showwarning("Aviso", "Preencha um campo")

        except Exception as e:
            messagebox.showerror("Erro", str(e))
