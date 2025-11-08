import aiohttp
import asyncio
import io

# URL backend FastAPI
API_URL = "http://127.0.0.1:8000/predict/"


async def predict_image(image_file):
    """
    Gửi ảnh đến backend FastAPI và nhận kết quả dự đoán.
    """
    try:
        # Đọc file ảnh từ Streamlit
        image_bytes = image_file.getvalue()
        filename = image_file.name

        # Dùng aiohttp để gửi file qua POST
        async with aiohttp.ClientSession() as session:
            form = aiohttp.FormData()
            form.add_field("file", image_bytes,
                           filename=filename,
                           content_type="image/jpeg")

            async with session.post(API_URL, data=form) as resp:
                if resp.status != 200:
                    text = await resp.text()
                    raise Exception(f"Backend error {resp.status}: {text}")

                result = await resp.json()
                return result

    except Exception as e:
        raise Exception(f"❌ Failed to connect to backend: {e}")
