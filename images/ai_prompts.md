# AI image prompts for CyberReconX

These prompts are ready-to-copy for use with local Stable Diffusion (Automatic1111/InvokeAI) or cloud image services. Each prompt has an English version and a concise Bangla hint.

## Cyberpunk Scene (Hero Image)

- Prompt (English):
  "cyberpunk cityscape at night, neon signs, rain-soaked streets, a lone operator with a laptop on a rooftop overlooking servers, cinematic lighting, high detail, 4k, vibrant colors, volumetric fog, cinematic composition"

- Bangla hint: "সাইবারপাংক রাতের শহর, নিয়ন সাইন, ছাদে ল্যাপটপ নিয়ে অপারেটর, নাটকীয় আলো"

## Architecture Overview (System Diagram, Stylized)

- Prompt (English):
  "stylized technical architecture diagram, modern flat isometric view, nodes labeled: scanner, nmap, whois, whatweb, local network, results dashboard, clean lines, soft shadows, infographic style, high clarity"

- Bangla hint: "সিস্টেম আর্কিটেকচার, আইসোমেট্রিক ডায়াগ্রাম, স্ক্যানার-নোড-ড্যাশবোর্ড দেখাবে"

## Motion Graphic / Animated Concept (idea for short clip frames)

- Prompt (English):
  "animated motion-graphic style frame: data packets flowing across neon grid, glowing lines connecting nodes, subtle parallax, loopable 3-second clip, high contrast"

- Bangla hint: "মোশন-গ্রাফিক: ডেটা ফ্লো, নোড সংযোগ, লুপেবল শর্ট ক্লিপ"

## Tips for best results

- Use a high sampling step count (20-40) and a good sampler (DPM++/Euler a).
- For Automatic1111 web UI, use the prompt above in the Txt2Img panel; for architecture, try using negative prompt to keep text legible.
- If you want labeled nodes, consider generating the base art then add labels in an image editor for clarity.

## Example curl to Automatic1111 API

```bash
curl -s -X POST "http://127.0.0.1:7860/sdapi/v1/txt2img" -H "Content-Type: application/json" -d '{"prompt":"<PUT_PROMPT_HERE>","steps":28,"width":1024,"height":576}' --output out.png
```

Replace `<PUT_PROMPT_HERE>` with one of the prompts above (properly escaped).
