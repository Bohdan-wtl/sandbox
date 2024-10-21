import os
import time
from fpdf import FPDF
from faker import Faker
from pydub.generators import Sine
from moviepy.editor import ColorClip
from PIL import ImageDraw, Image, ImageFont


download_path = "downloaded_qr_codes/"
signup_password = "1234567890"


def navigate(BASE_URL_LANG_PARAM, page):
    page.goto(BASE_URL_LANG_PARAM)


# def random_email_faker():
#     fake = Faker()
#     fake_email = "wtl.automation" + fake.aba() + "@" + fake.domain_word() + ".com"
#     return fake_email


def random_website_faker():
    fake = Faker()
    fake_website = "www.test" + fake.domain_name()
    return fake_website


temporary_website = random_website_faker()


def generate_image():
    timestamp = int(time.time())
    image_filename = f"generated_image_{timestamp}.png"
    image_path = os.path.join("generated_files", image_filename)
    fake = Faker()
    image = Image.new('RGB', (800, 600), color=(000, 111, 255))
    draw = ImageDraw.Draw(image)
    #font = Image.load_default()
    font = ImageFont.load_default()
    text = f"{fake.texts(max_nb_chars=500)} {timestamp}"
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))
    image.save(image_path)
    return image_path


def generate_mp4():
    timestamp = int(time.time())
    mp4_filename = f"generated_file_{timestamp}.mp4"
    mp4_path = os.path.join("generated_files", mp4_filename)
    duration = 5
    fps = 24
    color = (0, 0, 255)
    resolution = (640, 480)
    clip = ColorClip(size=resolution, color=color, duration=duration)
    clip = clip.set_fps(fps)
    clip.write_videofile(mp4_path, codec="libx264", fps=fps)
    return mp4_path


def generate_pdf():
    timestamp = int(time.time())
    pdf_filename = f"generated_file_{timestamp}.pdf"
    pdf_path = os.path.join("generated_files", pdf_filename)
    fake = Faker()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(190, 10, txt=f"{fake.texts(max_nb_chars=5000)} {timestamp}", align='C')
    pdf.output(pdf_path)
    return pdf_path


def generate_mp3():
    timestamp = int(time.time())
    mp3_filename = f"generated_file_{timestamp}.mp3"
    mp3_path = os.path.join("generated_files", mp3_filename)
    sine_wave = Sine(340)
    audio = sine_wave.to_audio_segment(duration=5000)
    audio.export(mp3_path, format='mp3')
    return mp3_path


# def test_file_generation():
#     generate_pdf()
#     generate_image()
#     generate_mp4()
#     generate_mp3()
def emulate_drag_and_drop(page, selector, file_path):
    # Определение MIME-типа файла по его расширению
    mime_type_mapping = {
        '.pdf': 'application/pdf',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.mp3': 'audio/mpeg',
        '.mp4': 'video/mp4',
        '.avi': 'video/x-msvideo',
    }

    file_extension = file_path.suffix.lower()
    mime_type = mime_type_mapping.get(file_extension, 'application/octet-stream')
    with open(file_path, 'rb') as file:
        file_content = file.read()
    page.evaluate("""
      (data) => {
        const { fileContent, selector, mimeType, fileName } = data;
        const dropArea = document.querySelector(selector);
        const dataTransfer = new DataTransfer();
        const file = new File([new Uint8Array(fileContent)], fileName, { type: mimeType });

        dataTransfer.items.add(file);
        dropArea.dispatchEvent(new DragEvent('dragenter', { dataTransfer }));
        dropArea.dispatchEvent(new DragEvent('drop', { dataTransfer }));
      }
    """, {
        'fileContent': list(file_content),
        'selector': selector,
        'mimeType': mime_type,
        'fileName': file_path.name
    })


