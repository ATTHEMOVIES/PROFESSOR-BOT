import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


RUN_STRINGS = (
    "ஐயோ.. திமிர்... அப்படியே.... எந்த மாற்றமும் இல்லை..... தவறில்லை....!!!",
    "அல்லாஹ்... ஒவ்வொரு குழந்தையும்... பேரார்வம்...",
    "எனக்கு படிக்கத் தெரியாது சார். படிக்கத் தெரியாது. புரியுது சொர்க்கம், நரகம் இல்லை, 'ஒற்றை வாழ்க்கை', எங்கு, எப்படி செய்வது என்று எல்லோரும் தீர்மானிக்கிறார்கள் ",
    " என்ன ஒரு குண்டு வெடிப்பு! அப்படி ஒரு பயங்கரமான வெளிப்பாடு !! இன்று... கீழே போகாதே.. ",
    " என்னால் அதை செய்ய முடியும் , நான் அதை செய்ய முடியும் ",
    " பிஸ்கட்டில் கிரீம் இருப்பதாக நினைத்து புலி இருக்கக்கூடாது. க்ரீம் பிஸ்கட்.",
    "அரசே... நீங்கள் என்னை நன்றாக இருக்க அனுமதிக்கவில்லை.  உங்க அப்பா கஞ்சியும் கோழியும் பண்றாரா?, கள்ளும் நனைந்த மழையும் வீணா....",
    "இவ்வளவு நேரம் எங்கிருந்தாய்....!","எனக்கு இங்கிலீஷ் தெரியாது.... ",
    " ட்விங்கிள் ஸ்டார்ஸ் போல் கனவுகள் அனைத்தும்... "," என் சுற்றளவு முத்தப்பா அவருக்கு வழி தாருங்கள் ",
    "உன் அக்கா அலியாவுக்கு கட்டிய வரதட்சணையை கொடுப்பாயா ",
    " மிகவும் சோர்வாக இருக்கிறாய் ",
    " கண்ணீருடன் காத்திருக்கிறாய். உன் கண்கள் ",
    " செல்லகண்டு என்னு போட தடி.யா.", 
)


@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
