import webuiapi #https://github.com/mix1009/sdwebuiapi
import requests




api = webuiapi.WebUIApi(host='06a9237bb7d0322410.gradio.live', use_https=True)

print("api made")
result1 = api.txt2img(prompt="cute squirrel",
                    negative_prompt="ugly, out of frame",
                    seed=1003,
                    styles=["anime"],
                    cfg_scale=7,
                    )

print(result1.info)


"""
headers = {
    'accept': 'application/json',
}

params = {
    'attachment': 'false',
}

response = requests.get('https://06a9237bb7d0322410.gradio.live/internal/sysinfo', params=params, headers=headers)
print(response)
"""