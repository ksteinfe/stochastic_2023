import requests, json, base64



url = 'https://a2bb54055900224c2d.gradio.live:443/sdapi/v1/txt2img'

headers = {'Content-type': 'application/json'}

data = {
	"enable_hr": False,
	"hr_scale": 2,
	"hr_upscaler": "Latent",
	"hr_second_pass_steps": 0,
	"hr_resize_x": 0,
	"hr_resize_y": 0,
	"denoising_strength": 0.7,
	"firstphase_width": 0,
	"firstphase_height": 0,
	"prompt": "a brutalist parking garage full of graffiti",
	"styles": [],
	"seed": -1,
	"subseed": -1,
	"subseed_strength": 0.0,
	"seed_resize_from_h": 0,
	"seed_resize_from_w": 0,
	"batch_size": 1,
	"n_iter": 1,
	"steps": 20,
	"cfg_scale": 7,
	"width": 512,
	"height": 512,
	"restore_faces": False,
	"tiling": False,
	"do_not_save_samples": False,
	"do_not_save_grid": False,
	"negative_prompt": "",
	"eta": 1.0,
	"s_churn": 0,
	"s_tmax": 0,
	"s_tmin": 0,
	"s_noise": 1,
	"override_settings": {},
	"override_settings_restore_afterwards": True,
	"sampler_name": "Euler a",
	"sampler_index": "Euler a",
	"script_name": None,
	"script_args": [],
	"send_images": True,
	"save_images": False,
	"alwayson_scripts": {}
}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers, timeout=15)
    print('Status Code:', response.status_code)
    print('Headers:', response.headers)

    if response.status_code == 200:
        # Assuming the response is json and has an 'image' field
        response_data = response.json()

        #for key, value in response_data.items(): print(key)
        #print(response_data.get('parameters'))
        #print(response_data.get('info'))

        image_base64 = response_data.get('images')[0] # get first image

        if image_base64:
            image_bytes = base64.b64decode(image_base64) # Decode the base64 image
            with open('output_image.jpg', 'wb') as out_file:
                out_file.write(image_bytes)
            print("Image saved to 'output_image.jpg'.")
        else:
            print('No image found in the response.')

except requests.exceptions.Timeout:
    print("The request timed out")


