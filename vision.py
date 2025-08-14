
# Importar a biblioteca da pasta local (bot-vision-suite)
from bot_vision_suite.bot_vision import BotVision, BotVisionConfig
import time

bot = BotVision()

config = BotVisionConfig({
    "confidence_threshold": 85.0,
    "retry_attempts": 3,
    "overlay_duration": 100,
    "overlay_color": "green",
    "overlay_width": 1,
    "ocr_languages": ["eng", "por"],
    "log_level": "DEBUG",
    "show_overlay": True,
})

bot = BotVision(config=config)

time.sleep(2)  # Espera 2 segundos para garantir que o bot esteja pronto

# Usa click_relative_image para encontrar E clicar na imagem
success = bot.click_relative_image(
            anchor_image='D://suite2//Automation-Suite//images//anchor_1755114072.png',    # Imagem âncora (única na tela)
            target_image='D://suite2//Automation-Suite//images//target_1755114079.png',       # Imagem target (pode ter múltiplas)
            max_distance=200,                          # Distância máxima em pixels da âncora
            confidence=0.9,                            # Confiança de detecção (0.0-1.0)
            delay=0.5,                                 # Delay após o clique
            mouse_button="left",                       # Botão do mouse
            backtrack=False,                           # Backtrack se falhar
            max_attempts=3,                            # Tentativas máximas
            # target_region=(0, 0, 800, 600)             # Região específica para buscar target
            )

if success:
    print("✅ Clique realizado com sucesso!")
else:
    print("❌ Não foi possível clicar na imagem.")

