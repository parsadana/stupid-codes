import random

def predict_weather():
    factors = [
        "چون امروز گربه‌ها بیشتر از حد معمول میو کردن",
        "بر اساس زاویه قرارگیری لیوان چای روی میز",
        "به دلیل اینکه رنگ آبی امروز خسته‌تر به نظر می‌رسه",
        "چون سرعت اینترنت یه کم کند شده و ابرا گیر کردن"
    ]
    
    weathers = [
        "بارانی", 
        "آفتابی", 
        "برفی", 
        "همراه با احتمال بارش پیتزای پپرونی"
    ]
    
    reason = random.choice(factors)
    forecast = random.choice(weathers)
    
    print(f"پیش‌بینی امروز: هوا {forecast} خواهد بود، {reason}!")

predict_weather()
