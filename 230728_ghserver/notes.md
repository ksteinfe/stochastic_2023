

fixed grasshopper DLL HTTP Library issue 
using System.Net.Http;
using Newtonsoft.Json;

https://discourse.mcneel.com/t/upgrading-net-version-of-gh/127854/5


useful for testing requests
http://httpbin.org/




# Requests from WEBUIAPI

## IMG-TO-IMG

URL
https://de6b0d3fe5f8a90f0c.gradio.live:443/sdapi/v1

PAYLOAD

{
	"enable_hr": false,
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
	"restore_faces": false,
	"tiling": false,
	"do_not_save_samples": false,
	"do_not_save_grid": false,
	"negative_prompt": "",
	"eta": 1.0,
	"s_churn": 0,
	"s_tmax": 0,
	"s_tmin": 0,
	"s_noise": 1,
	"override_settings": {},
	"override_settings_restore_afterwards": true,
	"sampler_name": "Euler a",
	"sampler_index": "Euler a",
	"script_name": null,
	"script_args": [],
	"send_images": true,
	"save_images": false,
	"alwayson_scripts": {
		"ControlNet": {
			"args": [{
				"input_image": "IMAGE",
				"mask": null,
				"module": "depth",
				"model": "control_v11f1p_sd15_depth [cfd03158]",
				"weight": 1.0,
				"resize_mode": "Resize and Fill",
				"lowvram": false,
				"processor_res": 512,
				"threshold_a": 64,
				"threshold_b": 64,
				"guidance": 1.0,
				"guidance_start": 0.0,
				"guidance_end": 1.0,
				"control_mode": 0,
				"pixel_perfect": false
			}]
		}
	}
    
    
    
    
    



## NO IMG-TO-IMG

URL
https://de6b0d3fe5f8a90f0c.gradio.live:443/sdapi/v1

PAYLOAD

{
	""enable_hr"": false,
	""hr_scale"": 2,
	""hr_upscaler"": ""Latent"",
	""hr_second_pass_steps"": 0,
	""hr_resize_x"": 0,
	""hr_resize_y"": 0,
	""denoising_strength"": 0.7,
	""firstphase_width"": 0,
	""firstphase_height"": 0,
	""prompt"": ""a brutalist parking garage full of graffiti"",
	""styles"": [],
	""seed"": -1,
	""subseed"": -1,
	""subseed_strength"": 0.0,
	""seed_resize_from_h"": 0,
	""seed_resize_from_w"": 0,
	""batch_size"": 1,
	""n_iter"": 1,
	""steps"": 20,
	""cfg_scale"": 7,
	""width"": 512,
	""height"": 512,
	""restore_faces"": false,
	""tiling"": false,
	""do_not_save_samples"": false,
	""do_not_save_grid"": false,
	""negative_prompt"": """",
	""eta"": 1.0,
	""s_churn"": 0,
	""s_tmax"": 0,
	""s_tmin"": 0,
	""s_noise"": 1,
	""override_settings"": {},
	""override_settings_restore_afterwards"": true,
	""sampler_name"": ""Euler a"",
	""sampler_index"": ""Euler a"",
	""script_name"": null,
	""script_args"": [],
	""send_images"": true,
	""save_images"": false,
	""alwayson_scripts"": {}
}



# C-Sharp Version


  public Dictionary<string, object> TESTPROMPT(string prompt)
  {
    return new Dictionary<string, object>
      {
        { "enable_hr", false },
        { "hr_scale", 2 },
        { "hr_upscaler", "Latent" },
        { "hr_second_pass_steps", 0 },
        { "hr_resize_x", 0 },
        { "hr_resize_y", 0 },
        { "denoising_strength", 0.7 },
        { "firstphase_width", 0 },
        { "firstphase_height", 0 },
        { "prompt", prompt },
        { "styles", new List<object>() },
        { "seed", -1 },
        { "subseed", -1 },
        { "subseed_strength", 0.0 },
        { "seed_resize_from_h", 0 },
        { "seed_resize_from_w", 0 },
        { "batch_size", 1 },
        { "n_iter", 1 },
        { "steps", 20 },
        { "cfg_scale", 7 },
        { "width", 512 },
        { "height", 512 },
        { "restore_faces", false },
        { "tiling", false },
        { "do_not_save_samples", false },
        { "do_not_save_grid", false },
        { "negative_prompt", "" },
        { "eta", 1.0 },
        { "s_churn", 0 },
        { "s_tmax", 0 },
        { "s_tmin", 0 },
        { "s_noise", 1 },
        { "override_settings", new Dictionary<string, object>() },
        { "override_settings_restore_afterwards", true },
        { "sampler_name", "Euler a" },
        { "sampler_index", "Euler a" },
        { "script_name", null },
        { "script_args", new List<object>() },
        { "send_images", true },
        { "save_images", false },
        { "alwayson_scripts", new Dictionary<string, object>() }

        };
