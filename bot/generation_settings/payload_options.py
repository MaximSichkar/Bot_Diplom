import requests
from PIL import Image
import io
import base64
from bot import dp, bot
from aiogram.types import Message


async def generation_option(message: Message):
    payload = {
        "prompt": message.text,
        "negative_prompt": "(worst quality:1.4),(low quality:1.4), easynegative, badhandv4, neg_grapefruit, "
                           "extra fingers, extra arms, extra legs, extra limbs, malformed limbs, missing arms, "
                           "missing legs, missing fingers, fused fingers, too many fingers, long neck, mutated hands, "
                           "mutation, deformed, bad anatomy, bad proportions, cloned face, disfigured, username, "
                           "jpeg artifacts, out of frame, blurry, watermark, signature",

        "seed": -1,
        "sampler_name": "DPM++ 2M Karras",
        "batch_size": 1,
        "steps": 20,
        "cfg_scale": 10,
        "width": 480,
        "height": 800,
        "restore_faces": False,
        "tiling": False,
        "denoising_strength": 0.4,
        "enable_hr": True,
        "hr_scale": 2,
        "hr_upscaler": "4x-UltraSharp",
        "hr_second_pass_steps": 10,
        "hr_checkpoint_name": 'calicomix_v75',
        "hr_sampler_name": "DPM++ 2M Karras",
    }

    options_payload = {
        "sd_model_checkpoint": 'calicomix_v75'
    }
    options_response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/options', json=options_payload)

    print(options_response.status_code)

    response = requests.post(url=f'http://127.0.0.1:7860/sdapi/v1/txt2img', json=payload)

    print(response.status_code)

    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
        file_path = r'C:/Users/clash/PycharmProjects/botik/bot/pictures/picture.png'
        image.save(file_path)

        with open(file_path, 'rb') as photo:
            await bot.send_document(chat_id=message.chat.id, document=photo)
