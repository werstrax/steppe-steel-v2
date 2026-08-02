# -*- coding: utf-8 -*-
"""
Генерация изображений через OpenAI Images API.
Ключ читается из файла вне репозитория и НИКОГДА не печатается.

Запуск:  python _gen_openai.py <имя_выхода.png> "промпт" [размер] [модель]
Размеры: 1536x1024 (гориз.), 1024x1536 (верт.), 1024x1024
"""
import base64, io, json, os, sys, urllib.request, urllib.error

KEY_PATH = r"C:\Users\Flockyman\openai-key.txt"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_gen")


def _key():
    with io.open(KEY_PATH, encoding="utf-8") as f:
        k = f.read().strip()
    if not k.startswith("sk-"):
        raise SystemExit("Ключ не найден или испорчен: " + KEY_PATH)
    return k


def generate(out_name, prompt, size="1536x1024", model="gpt-image-2", quality="high"):
    os.makedirs(OUT_DIR, exist_ok=True)
    payload = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "n": 1,
    }
    if quality:
        payload["quality"] = quality

    req = urllib.request.Request(
        "https://api.openai.com/v1/images/generations",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": "Bearer " + _key(),
                 "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        raise SystemExit("HTTP %s\n%s" % (e.code, body[:600]))

    item = data["data"][0]
    path = os.path.join(OUT_DIR, out_name)
    if item.get("b64_json"):
        with open(path, "wb") as f:
            f.write(base64.b64decode(item["b64_json"]))
    elif item.get("url"):
        with urllib.request.urlopen(item["url"], timeout=180) as r, open(path, "wb") as f:
            f.write(r.read())
    else:
        raise SystemExit("Ответ без изображения: " + json.dumps(data)[:300])

    print("OK ->", path, os.path.getsize(path) // 1024, "KB")
    return path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    generate(sys.argv[1], sys.argv[2],
             sys.argv[3] if len(sys.argv) > 3 else "1536x1024",
             sys.argv[4] if len(sys.argv) > 4 else "gpt-image-2")
