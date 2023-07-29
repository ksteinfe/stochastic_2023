import requests, json, base64, copy
from PIL import Image
from io import BytesIO
from datetime import datetime

GRADIO_ID = "10226c57c39067dade"
BASEURL = "https://{}.gradio.live:443/sdapi".format(GRADIO_ID)



def main():
	timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
	#img = text_to_image("a city street")
	img = depth_to_image("a city street, post apocalyptic", "img_dpth/01.jpg")
	
	if img:
		img.save('{}.png'.format(timestamp))

def text_to_image(prompt):	
	pdata = copy.deepcopy(BASEDATA_TXT_2_IMG)
	pdata['prompt'] = prompt
	return _do_post_data(pdata, "/v1/txt2img")

def depth_to_image(prompt, pth_dimg):	
	pdata = copy.deepcopy(BASEDATA_TXT_2_IMG)
	pdata['prompt'] = prompt

	dimg = Image.open(pth_dimg)
	pdata = _append_depthimg(pdata, dimg)
	return _do_post_data(pdata, "/v1/txt2img")





def _do_post_data(pdata, urlsuffix):
	try:
		headers = {'Content-type': 'application/json'}
		url = BASEURL + urlsuffix
		response = requests.post(url, data=json.dumps(pdata), headers=headers, timeout=15)
		print('Status Code:', response.status_code)
		print('Headers:', response.headers)

		if response.status_code == 200:
			response_data = response.json()

			#for key, value in response_data.items(): print(key)
			#print(response_data.get('parameters'))
			#print(response_data.get('info'))

			images_base64 = response_data.get('images')
			if images_base64 and len(images_base64)>0:
				image_bytes = base64.b64decode(images_base64[0]) # Decode the first base64 image
				img = Image.open(BytesIO(image_bytes)) # Create a PIL Image from the bytes
				return img
			else:
				print('Key "images" not found in the response, or contained no data')
				print(images_base64)
				return False
		else:
			print("Bad response code: {}".format(response.status_code))
			return False

	except requests.exceptions.Timeout:
		print("The request timed out")
		return False



def _append_depthimg(pdata, img):
	
    #base64_str = base64.b64encode(img).decode('utf-8')
    #data = {'image': image_base64}   
    
    buf = BytesIO() # Create a BytesIO object
    img.save(buf, format='PNG') # Save the image to the BytesIO object
    byte_data = buf.getvalue() # Get the byte data from the BytesIO object
    base64_str = base64.b64encode(byte_data).decode('utf-8') # Convert the byte data to a base64 string
    
    cnscript_depth = {
		"ControlNet": {
			"args": [{
				"input_image": base64_str,
				"mask": None,
				"module": "depth",
				"model": "control_v11f1p_sd15_depth [cfd03158]",
				"weight": 1.0,
				"resize_mode": "Resize and Fill",
				"lowvram": False,
				"processor_res": 512,
				"threshold_a": 64,
				"threshold_b": 64,
				"guidance": 1.0,
				"guidance_start": 0.0,
				"guidance_end": 1.0,
				"control_mode": 0,
				"pixel_perfect": False
			}]
		}
	}

    pdata["alwayson_scripts"].update(cnscript_depth)
    return pdata


BASEDATA_TXT_2_IMG = {
	"enable_hr": False,
	"hr_scale": 2,
	"hr_upscaler": "Latent",
	"hr_second_pass_steps": 0,
	"hr_resize_x": 0,
	"hr_resize_y": 0,
	"denoising_strength": 0.7,
	"firstphase_width": 0,
	"firstphase_height": 0,
	"prompt": "",
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







if __name__ == "__main__":
    main()