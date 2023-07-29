import webuiapi #https://github.com/mix1009/sdwebuiapi
import requests
from datetime import datetime
from PIL import Image
timestamp = datetime.now().strftime("%y%m%d_%H%M%S")

api = webuiapi.WebUIApi(host='de6b0d3fe5f8a90f0c.gradio.live', port=443, use_https=True)
print("api defined")

#options = api.get_options()
#print(options)


img_depth = Image.open("img_dpth/02.jpg")
print("depth image loaded")


unit1 = webuiapi.ControlNetUnit(
    input_image=img_depth, 
    module='depth', 
    model='control_v11f1p_sd15_depth [cfd03158]', 
    weight=1.0
)
#print(unit1.to_dict())
print("ControlNetUnit defined")

rslt1 = api.txt2img(
            prompt="a brutalist parking garage full of graffiti",
            width=512,
            height=512,
            #controlnet_units=[unit1],
            sampler_name="Euler a",
            cfg_scale=7,
           )
print(rslt1)
rslt1.image.save('{}.png'.format(timestamp))

# upscale
rslt2 = api.extra_single_image(image=rslt1.image,
                                 upscaler_1=webuiapi.Upscaler.ESRGAN_4x,
                                 upscaling_resize=2)
print(rslt2.image.size)
rslt2.image.save('{}_up.png'.format(timestamp))







"""
headers = {
    'accept': 'application/json',
}

params = {
    'attachment': 'false',
}

response = requests.get('https://de6b0d3fe5f8a90f0c.gradio.live/internal/sysinfo', params=params, headers=headers)
print(response.content)
"""