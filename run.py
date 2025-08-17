from generate_voice import generate_voice

# 🔧 Replace this with your actual ElevenLabs API key
api_key = sk_fa161090daf340dfcdf637746480319dccd7378d17406c44

# 🗣️ Choose a voice ID from ElevenLabs (e.g., Rachel, Adam, etc.)
voice_id = "EXAVITQu4vr4xnSDxMaL"  # Example: Rachel

# 📰 Your news script
script_text = """
India @ 78 — From Chains to Champions.
In 1947, India broke free from colonial rule. Today, it leads in space, tech, and diplomacy.
This is not just independence. It’s transformation.
"""

generate_voice(script_text, voice_id, api_key)
