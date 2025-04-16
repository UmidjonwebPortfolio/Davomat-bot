import telebot
import time
from telebot import types

bot = telebot.TeleBot("7529857134:AAHCREPrVhia0XwqNdH41LLOIBispx6CAwY")
davomat=list()
davomat5=list()
davomat6=list()
davomat6b=list()
davomat7a=list()
davomat7b=list()
davomat8a=list()
davomat8b=list()
davomat9b=list()
davomat10a=list()
davomat10b=list()
davomat11a=list()
davomat11b=list()

@bot.message_handler(commands=['start'])
def start(message):
    asosiy = types.InlineKeyboardMarkup(row_width=2)
    asosiy.add(
        types.InlineKeyboardButton("👥 Sinflar", callback_data="sinflar_call"),
        types.InlineKeyboardButton("📚 Fanlar", callback_data="fanlar_call"),
        types.InlineKeyboardButton("🧾 Davomat", callback_data="davomat_call"),
        types.InlineKeyboardButton("📌 Qo'llanma", callback_data="qoll_call")
    )
    bot.send_message(message.chat.id, "Asosiy menyu:", reply_markup=asosiy)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    # 1 - Sinflar menyusi
    if call.data == "sinflar_call":
        sinf_lar = types.InlineKeyboardMarkup(row_width=2)
        sinf_lar.add(
            types.InlineKeyboardButton("♻️ 5-Sinf", callback_data="5_sinf"),
            types.InlineKeyboardButton("♻️ 6-Sinf", callback_data="6_sinf"),
            types.InlineKeyboardButton("♻️ 7-Sinf", callback_data="7_sinf"),
            types.InlineKeyboardButton("♻️ 8-Sinf", callback_data="8_sinf"),
            types.InlineKeyboardButton("♻️ 9-Sinf", callback_data="9_sinf"),
            types.InlineKeyboardButton("♻️ 10-Sinf", callback_data="10_sinf"),
            types.InlineKeyboardButton("♻️ 11-Sinf", callback_data="11_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="back_main")
        )
        bot.edit_message_text("💠 Kerakli sinfni tanlang!", chat_id, msg_id, reply_markup=sinf_lar)
    # Orqaga asosiy menyuga
    elif call.data == "back_main":
        asosiym = types.InlineKeyboardMarkup(row_width=2)
        asosiym.add(
            types.InlineKeyboardButton("👥 Sinflar", callback_data="sinflar_call"),
            types.InlineKeyboardButton("📚 Fanlar", callback_data="fanlar_call"),
            types.InlineKeyboardButton("🧾 Davomat", callback_data="davomat_call"),
            types.InlineKeyboardButton("📍 Qo'llanma", callback_data="qoll_call")
        )
        bot.edit_message_text("Asosiy menyu:", call.message.chat.id, call.message.message_id, reply_markup=asosiym)

    # Davomat bo'imi
    elif call.data=="davomat_call":
        davom_at=types.InlineKeyboardMarkup(row_width=1)
        davom_at.add(
            types.InlineKeyboardButton("📝 Davomat qilish", callback_data="davomat_q"),
            types.InlineKeyboardButton("🔍Davomatni ko'rish ", callback_data="davomat_k"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="back_main")
        )
        bot.edit_message_text("💠 Kerakli bo'limni tanlang !", chat_id, msg_id, reply_markup=davom_at)
    # Davomat ko'rish
    elif call.data=="davomat_k":
        qoll=types.InlineKeyboardMarkup()
        qoll.add(
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="back_main")
        )
        bot.edit_message_text(f"/start - B.tushirish va asosiy menyuni ko'rish\n\n2. Sinf bo'yicha davomat yig'ish\n\n• /davomat5a - 5-A sinf davomatini ko'rish\n• /davomat6a - 6-A sinf davomatini ko'rish\n• /davomat6b - 6-B sinf davomatini ko'rish\n• /davomat7a - 7-A sinf davomatini ko'rish\n• /davomat7b - 7-B sinf davomatini ko'rish\n• /davomat8a - 8-A sinf davomatini ko'rish\n• /davomat8b - 8-B sinf davomatini ko'rish\n• /davomat9a - 9-A sinf davomatini ko'rish\n• /davomat9b - 9-B sinf davomatini ko'rish\n• /davomat10a - 10-A sinf davomatini ko'rish\n• /davomat10b - 10-B sinf davomatini ko'rish\n• /davomat11a - 11-A sinf davomatini ko'rish\n• /davomat11b - 11-B sinf davomatini ko'rish", chat_id, msg_id, reply_markup=qoll)
    # Davomat qilish
    elif call.data=="davomat_q":
        sinf_lar = types.InlineKeyboardMarkup(row_width=2)
        sinf_lar.add(
            types.InlineKeyboardButton("♻️ 5-Sinf", callback_data="5_sinf"),
            types.InlineKeyboardButton("♻️ 6-Sinf", callback_data="6_sinf"),
            types.InlineKeyboardButton("♻️ 7-Sinf", callback_data="7_sinf"),
            types.InlineKeyboardButton("♻️ 8-Sinf", callback_data="8_sinf"),
            types.InlineKeyboardButton("♻️ 9-Sinf", callback_data="9_sinf"),
            types.InlineKeyboardButton("♻️ 10-Sinf", callback_data="10_sinf"),
            types.InlineKeyboardButton("♻️ 11-Sinf", callback_data="11_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="back_main")
        )
        bot.edit_message_text("Davomatni to'ldirish uchun kerakli sinfni tanlang!", chat_id, msg_id, reply_markup=sinf_lar)
    # Qo'llanma 
    elif call.data=="qoll_call":
        qoll=types.InlineKeyboardMarkup()
        qoll.add(
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="back_main")
        )
        bot.edit_message_text(f"‼️ Asosiy Buyruqlar\n\n1. Davomatni boshlash\n\n/start - B.tushirish va asosiy menyuni ko'rish\n\n2. Sinf bo'yicha davomat yig'ish\n\n• /davomat5a - 5-A sinf davomatini ko'rish\n• /davomat6a - 6-A sinf davomatini ko'rish\n• /davomat6b - 6-B sinf davomatini ko'rish\n• /davomat7a - 7-A sinf davomatini ko'rish\n• /davomat7b - 7-B sinf davomatini ko'rish\n• /davomat8a - 8-A sinf davomatini ko'rish\n• /davomat8b - 8-B sinf davomatini ko'rish\n• /davomat9a - 9-A sinf davomatini ko'rish\n• /davomat9b - 9-B sinf davomatini ko'rish\n• /davomat10a - 10-A sinf davomatini ko'rish\n• /davomat10b - 10-B sinf davomatini ko'rish\n• /davomat11a - 11-A sinf davomatini ko'rish\n• /davomat11b - 11-B sinf davomatini ko'rish\n\n\n‼️ Botdan foydalanish tartibi:\n\n1. /start buyrug'ini yuboring\n2. '🧾 Davomat' tugmasini bosing\n3. Kerakli sinfni tanlang (masalan, 6'A'-Sinf)\n4. Kelgan o'quvchilar ismini tanlab, belgilang\n5. Davomat tugagach, tegishli buyruq orqali ro'yxatni ko'ring (masalan, /davomat6a)\n\n\n‼️ Muhim eslatmalar:\n\n• Har bir o'quvchi nomini bosganingizda, bot O'quvchi kelgan ✅ deb javob qaytaradi\n• Davomat ro\'yxatini ko\'rish uchun yuqoridagi buyruqlardan birini ishlating\n• Agar xato qilsangiz, qaytadan /start bosib, jarayoni qayta boshlashingiz mumkin\n• Har bir sinf uchun alohida davomat ro\'yxati saqlanadi\n\n\n‼️ Agar qo'shimcha savollaringiz bo'lsa yoki botda muammo yuzaga kelsa, administratorlarga murojaat qiling.", chat_id, msg_id, reply_markup=qoll)
    # 1.1 - Sinflar bo‘limi
    # 1.1.5 
    elif call.data == "5_sinf":
        sinf5 = types.InlineKeyboardMarkup(row_width=2)
        sinf5.add(
            types.InlineKeyboardButton("5'A'-Sinf", callback_data="5_a_sinf"),
            types.InlineKeyboardButton("5'B'-Sinf", callback_data="5_b_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="sinflar_call")
        )
        bot.edit_message_text("💠 Kerakli sinfni tanlang.", chat_id, msg_id, reply_markup=sinf5)
    # 5 A
    elif call.data=="5_a_sinf":
        sinf_5a=types.InlineKeyboardMarkup(row_width=2)
        sinf_5a.add(
            types.InlineKeyboardButton("ABDILLAYEV HASAN", callback_data="5_a_01"),
            types.InlineKeyboardButton("ABDISAMIYEVA SARVINOZ", callback_data="5_a_02"),
            types.InlineKeyboardButton("ABDULLAYEV ELNUR", callback_data="5_a_03"),
            types.InlineKeyboardButton("ABDUNOROVA MUHAYYO", callback_data="5_a_04"),
            types.InlineKeyboardButton("BALTAYEV SHOHRO'Z", callback_data="5_a_05"),
            types.InlineKeyboardButton("BAXRAMOV HASAN", callback_data="5_a_06"),
            types.InlineKeyboardButton("DO'SQULOV BEHRO'Z", callback_data="5_a_07"),
            types.InlineKeyboardButton("ERKINOVA ZARINA", callback_data="5_a_08"),
            types.InlineKeyboardButton("ESHKULOVA RUXSHONA", callback_data="5_a_09"),
            types.InlineKeyboardButton("KUSHBAKOVA SHAHZODA", callback_data="5_a_10"),
            types.InlineKeyboardButton("MIYZAMOVA NASIBA", callback_data="5_a_11"),
            types.InlineKeyboardButton("MUSAYEVA ZILOLA", callback_data="5_a_12"),
            types.InlineKeyboardButton("NEKBAYEV LAZIZBEK", callback_data="5_a_13"),
            types.InlineKeyboardButton("NURMAMATOVA SHAXMIRA", callback_data="5_a_14"),
            types.InlineKeyboardButton("SAYFIDINOV SHOHRO'Z", callback_data="5_a_15"),
            types.InlineKeyboardButton("SHUKUROVA ZILOLA", callback_data="5_a_16"),
            types.InlineKeyboardButton("SIROJOV QODIR", callback_data="5_a_17"),
            types.InlineKeyboardButton("TINCHLIKOVA DINORA", callback_data="5_a_18"),
            types.InlineKeyboardButton("TOYCHIYEV DAVLATBEK", callback_data="5_a_19"),
            types.InlineKeyboardButton("UMIRZAQOVA ZILOLA", callback_data="5_a_20"),
            types.InlineKeyboardButton("XIKMATOV OLIMJON", callback_data="5_a_21"),
            types.InlineKeyboardButton("XOLDOROV ELNUR", callback_data="5_a_22"),
            types.InlineKeyboardButton("YULDOSHEV ORZUBEK", callback_data="5_a_23"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="5_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelgan o'quvchilarni tanlang!",chat_id, msg_id, reply_markup=sinf_5a)
    # 5-B
    elif call.data == "5_b_sinf":
        mavjutmas5 = types.InlineKeyboardMarkup(row_width=1)
        mavjutmas5.add(
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="5_sinf")
        )
        bot.edit_message_text("💠 Kechirasiz siz tanlagan sinf topilmadi!", chat_id, msg_id, reply_markup=mavjutmas5)

    #1.1.6
    elif call.data == "6_sinf":
        sinf6 = types.InlineKeyboardMarkup(row_width=2)
        sinf6.add(
            types.InlineKeyboardButton("6'A'-Sinf", callback_data="6_a_sinf"),
            types.InlineKeyboardButton("6'B'-Sinf", callback_data="6_b_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="sinflar_call")
        )
        bot.edit_message_text("💠 Kerakli sinfni tanlang.", chat_id, msg_id, reply_markup=sinf6)
    # 6-A
    elif call.data=="6_a_sinf":
        sinf_6a=types.InlineKeyboardMarkup(row_width=2)
        sinf_6a.add(
            types.InlineKeyboardButton("ABSOTAROVA SHIRIN", callback_data="6_a_02"),
            types.InlineKeyboardButton("AHROROV OLMOSBEK", callback_data="6_a_03"),
            types.InlineKeyboardButton("BAXTIVOROV ELBEK", callback_data="6_a_04"),
            types.InlineKeyboardButton("FAYZULLAYEV SHAXBOZ", callback_data="6_a_05"),
            types.InlineKeyboardButton("GAYIBNAZAROV AZIZBEK", callback_data="6_a_06"),
            types.InlineKeyboardButton("HUSANOVA ROZA", callback_data="6_a_07"),
            types.InlineKeyboardButton("ISMOILOV ELBEK", callback_data="6_a_08"),
            types.InlineKeyboardButton("MARDIBOYEVA SHOXSANAM", callback_data="6_a_09"),
            types.InlineKeyboardButton("MURODOV DAVLATBEK", callback_data="6_a_10"),
            types.InlineKeyboardButton("NE'MATULLAYEV AZIZBEK", callback_data="6_a_11"),
            types.InlineKeyboardButton("NURILLAYEV ASILBEK", callback_data="6_a_12"),
            types.InlineKeyboardButton("NURMAMATOV ASRORJON", callback_data="6_a_13"),
            types.InlineKeyboardButton("NURMUHAMMADOV UMIDJON", callback_data="6_a_14"),
            types.InlineKeyboardButton("QAYTAROVA ADIBA", callback_data="6_a_15"),
            types.InlineKeyboardButton("SADULLAYEV SHOXRUZBEK", callback_data="6_a_16"),
            types.InlineKeyboardButton("SHAMSITDINOV AZAMAT", callback_data="6_a_17"),
            types.InlineKeyboardButton("TAXAYEV IBROHIMBEK", callback_data="6_a_18"),
            types.InlineKeyboardButton("TO'XTAMURODOV ASLIDDIN", callback_data="6_a_19"),
            types.InlineKeyboardButton("XASANOV HUMOYUN", callback_data="6_a_20"),
            types.InlineKeyboardButton("XOLDOROVA ZUHRA", callback_data="6_a_21"),
            types.InlineKeyboardButton("XO'JAMQULOVA KAMOLA", callback_data="6_a_22"),
            types.InlineKeyboardButton("XUSHNAZAROV BEHRUZ", callback_data="6_a_23"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="6_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_6a)
    # 6-B
    elif call.data=="6_b_sinf":
        sinf_6b=types.InlineKeyboardMarkup(row_width=2)
        sinf_6b.add(
            types.InlineKeyboardButton("ABDAZOV NAVRO'ZALI", callback_data="6_b_01"),
            types.InlineKeyboardButton("ABDUMANONOVA MUXLISA", callback_data="6_b_02"),
            types.InlineKeyboardButton("BABABEKOV DIYORBEK", callback_data="6_b_03"),
            types.InlineKeyboardButton("BAXTIYOROV ELBEK", callback_data="6_b_04"),
            types.InlineKeyboardButton("BERDIQULOVA DINORA", callback_data="6_b_05"),
            types.InlineKeyboardButton("ESONBOYEV DAVRONBEK", callback_data="6_b_06"),
            types.InlineKeyboardButton("HASANOVA DURDONA", callback_data="6_b_07"),
            types.InlineKeyboardButton("HASANOVA SEVINCH", callback_data="6_b_08"),
            types.InlineKeyboardButton("IBRAGIMOV SHEHROZ", callback_data="6_b_09"),
            types.InlineKeyboardButton("MAXMUDOV ABDUG'OLIB", callback_data="6_b_10"),
            types.InlineKeyboardButton("MITANBOYEV ILG'ORBEK", callback_data="6_b_11"),
            types.InlineKeyboardButton("MUSTOFAYEV ELSHOD", callback_data="6_b_12"),
            types.InlineKeyboardButton("OOPULATOV G'ANISHER", callback_data="6_b_13"),
            types.InlineKeyboardButton("QQ'CHQOROV OZODBEK", callback_data="6_b_14"),
            types.InlineKeyboardButton("SAYDIRAXMATOV SHERXON", callback_data="6_b_15"),
            types.InlineKeyboardButton("SHODIYOROV FARHOD", callback_data="6_b_16"),
            types.InlineKeyboardButton("SHODMANOV JAVOHIR", callback_data="6_b_17"),
            types.InlineKeyboardButton("TURGUNOV KOMILJON", callback_data="6_b_18"),
            types.InlineKeyboardButton("XUDOYBERDIYEVA KOMILA", callback_data="6_b_19"),
            types.InlineKeyboardButton("YAXSHILIOOV DIYORBEK", callback_data="6_b_20"),
            types.InlineKeyboardButton("YOGUBOV UCHQUN", callback_data="6_b_21"),
            types.InlineKeyboardButton("YUSUPOV SARVARBEK", callback_data="6_b_22"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="6_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_6b)
    # 1.1.7
    elif call.data == "7_sinf":
        sinf7 = types.InlineKeyboardMarkup(row_width=2)
        sinf7.add(
            types.InlineKeyboardButton("7'A'-Sinf", callback_data="7_a_sinf"),
            types.InlineKeyboardButton("7'B'-Sinf", callback_data="7_b_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="sinflar_call")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf7)
    # 7-A
    elif call.data=="7_a_sinf":
        sinf_7a=types.InlineKeyboardMarkup(row_width=2)
        sinf_7a.add(
            types.InlineKeyboardButton("ABDIXASHIMOV ELBEK", callback_data="7_a_02"),
            types.InlineKeyboardButton("ABDULLAYEVA SHAROFAT", callback_data="7_a_03"),
            types.InlineKeyboardButton("AXROROV SARDOR", callback_data="7_a_04"),
            types.InlineKeyboardButton("BAHRAMOV AZAMAT", callback_data="7_a_05"),
            types.InlineKeyboardButton("BEKMURODOV SAMIR", callback_data="7_a_06"),
            types.InlineKeyboardButton("BOLIKULOV OTABEK", callback_data="7_a_07"),
            types.InlineKeyboardButton("ISOMIDDINOVA KIBRIYO", callback_data="7_a_08"),
            types.InlineKeyboardButton("JORAQULOV SHAXRIZOD", callback_data="7_a_09"),
            types.InlineKeyboardButton("NASRIDDINOVA CHAROS", callback_data="7_a_10"),
            types.InlineKeyboardButton("NORMUHAMMADOV SHOHJAXON", callback_data="7_a_11"),
            types.InlineKeyboardButton("NURALIYEVA E'ZOZA", callback_data="7_a_12"),
            types.InlineKeyboardButton("NURGOBILOV MUHAMMADJON", callback_data="7_a_13"),
            types.InlineKeyboardButton("QURBONQULOV SHEROZ", callback_data="7_a_14"),
            types.InlineKeyboardButton("ROZIQULOV RAMZBEK", callback_data="7_a_15"),
            types.InlineKeyboardButton("SAFAROVA CHAROS", callback_data="7_a_16"),
            types.InlineKeyboardButton("SATTAROV BEHRUZ", callback_data="7_a_17"),
            types.InlineKeyboardButton("SAYFULLAYEV XUMOYUN", callback_data="7_a_18"),
            types.InlineKeyboardButton("TIRKASHEVA MUXLISA", callback_data="7_a_19"),
            types.InlineKeyboardButton("TOLISHOVA DIHOZA", callback_data="7_a_20"),
            types.InlineKeyboardButton("TOSHPOLATOV ABUBAKIR", callback_data="7_a_21"),
            types.InlineKeyboardButton("XOLBOYEV ELDOR", callback_data="7_a_22"),
            types.InlineKeyboardButton("YOLDASHEV TEMURBEK", callback_data="7_a_23"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="7_sinf")
        )
        bot.edit_message_text("Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_7a)
    # 7-B
    elif call.data=="7_b_sinf":
        sinf_7b=types.InlineKeyboardMarkup(row_width=2)
        sinf_7b.add(
            types.InlineKeyboardButton("ABDUSAMATOVA E'ZOZA", callback_data="7_b_01"),
            types.InlineKeyboardButton("ABDUVOHOBOV BOBUR", callback_data="7_b_02"),
            types.InlineKeyboardButton("ASATULLAYEV ULUG'BEK", callback_data="7_b_03"),
            types.InlineKeyboardButton("BOTIROV BAXTBEK", callback_data="7_b_04"),
            types.InlineKeyboardButton("DONAQULOVA MARJONA", callback_data="7_b_05"),
            types.InlineKeyboardButton("HUBBIMOV AHMADJON", callback_data="7_b_06"),
            types.InlineKeyboardButton("MAMASOLIEV SARDOR", callback_data="7_b_07"),
            types.InlineKeyboardButton("MUHAMMADOVA FARANGIZ", callback_data="7_b_08"),
            types.InlineKeyboardButton("NURULLAYEVA SEVINCH", callback_data="7_b_09"),
            types.InlineKeyboardButton("PARDABOYEV ALIBEK", callback_data="7_b_10"),
            types.InlineKeyboardButton("QUIMUHAMMADOV SHAXBOZ", callback_data="7_b_11"),
            types.InlineKeyboardButton("RADJABOV SARDOR", callback_data="7_b_12"),
            types.InlineKeyboardButton("RASULOV ABDULAZIZ", callback_data="7_b_13"),
            types.InlineKeyboardButton("RAVSHANOV DAVRONBEK", callback_data="7_b_14"),
            types.InlineKeyboardButton("RUSTAMOVA DURDONA", callback_data="7_b_15"),
            types.InlineKeyboardButton("SAIDOV XUSHNUDXON", callback_data="7_b_16"),
            types.InlineKeyboardButton("SAYDIRAXMATOVA DILNURA", callback_data="7_b_17"),
            types.InlineKeyboardButton("SAYFULLAYEV LAZIZBEK", callback_data="7_b_18"),
            types.InlineKeyboardButton("SHUKUROV SARDORJON", callback_data="7_b_19"),
            types.InlineKeyboardButton("TOSHIMAMATOVA GULBAHOR", callback_data="7_b_20"),
            types.InlineKeyboardButton("TUXTAMURODOV OBIDJON", callback_data="7_b_21"),
            types.InlineKeyboardButton("UBAYDULLAYEV ISLOMJON", callback_data="7_b_22"),
            types.InlineKeyboardButton("YUNUSOVA SHABANAM", callback_data="7_b_23"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="7_sinf")
        )
        bot.edit_message_text("Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_7b)
    # 1.1.8
    elif call.data == "8_sinf":
        sinf8 = types.InlineKeyboardMarkup(row_width=2)
        sinf8.add(
            types.InlineKeyboardButton("8'A'-Sinf", callback_data="8_a_sinf"),
            types.InlineKeyboardButton("8'B'-Sinf", callback_data="8_b_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="sinflar_call")
        )
        bot.edit_message_text("🧑‍🎓 O'quvchilar hali kiritilmagan!", chat_id, msg_id, reply_markup=sinf8)
    # 8-A
    elif call.data=="8_a_sinf":
        sinf_8a=types.InlineKeyboardMarkup(row_width=2)
        sinf_8a.add(
            types.InlineKeyboardButton("ABDUMALIKOVA UMIDA", callback_data="8_a_02"),
            types.InlineKeyboardButton("ABDUNAZAROVA AZIZA", callback_data="8_a_03"),
            types.InlineKeyboardButton("ABDURAXIMOV RAMAZON", callback_data="8_a_04"),
            types.InlineKeyboardButton("ABDXAILIOVA UMIDA", callback_data="8_a_05"),
            types.InlineKeyboardButton("ALIBEKOV ASADBEK", callback_data="8_a_06"),
            types.InlineKeyboardButton("JOFRAMURODOVA MOHINUR", callback_data="8_a_07"),
            types.InlineKeyboardButton("JUMAQULOVA SEVINCH", callback_data="8_a_08"),
            types.InlineKeyboardButton("KAMONOV TOSHTEMUR", callback_data="8_a_09"),
            types.InlineKeyboardButton("KARIMOV RASULBEK", callback_data="8_a_10"),
            types.InlineKeyboardButton("MUHAMMADQULOVA SEVINCH", callback_data="8_a_11"),
            types.InlineKeyboardButton("NEMATULLAYEVA RAYXONA", callback_data="8_a_12"),
            types.InlineKeyboardButton("NORBOYEV BEHRO'Z", callback_data="8_a_13"),
            types.InlineKeyboardButton("NORTAYEVA NAFISA", callback_data="8_a_14"),
            types.InlineKeyboardButton("NURMAMATOVA FARNOZA", callback_data="8_a_15"),
            types.InlineKeyboardButton("NURMUHAMMADOV SHAXZODJON", callback_data="8_a_16"),
            types.InlineKeyboardButton("ORTIGBOYEV MATLAB", callback_data="8_a_17"),
            types.InlineKeyboardButton("SHAMSIDDINOVA POKIZA", callback_data="8_a_18"),
            types.InlineKeyboardButton("TOLLIBOYEVA MARXABO", callback_data="8_a_19"),
            types.InlineKeyboardButton("TOYIROVA MUSHTARIY", callback_data="8_a_20"),
            types.InlineKeyboardButton("UROLOV RAMAZON", callback_data="8_a_21"),
            types.InlineKeyboardButton("YAKUBOVA SAIDA", callback_data="8_a_22"),
            types.InlineKeyboardButton("YUSUPOV QUVONCHBEK", callback_data="8_a_23"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="8_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_8a)
    # 8-B
    elif call.data=="8_b_sinf":
        sinf_8b=types.InlineKeyboardMarkup(row_width=2)
        sinf_8b.add(
            types.InlineKeyboardButton("ACHILOV ABDULAZIZ", callback_data="8_b_03"),
            types.InlineKeyboardButton("Bahodirov Javohir", callback_data="8_b_05"),
            types.InlineKeyboardButton("Bektosheva Ruxshona", callback_data="8_b_06"),
            types.InlineKeyboardButton("Berkinov Sohibjon", callback_data="8_b_07"),
            types.InlineKeyboardButton("Joraqulov Hushnudbek", callback_data="8_b_08"),
            types.InlineKeyboardButton("Maxammadov Behro’z", callback_data="8_b_09"),
            types.InlineKeyboardButton("Miltigov Behruzjon", callback_data="8_b_10"),
            types.InlineKeyboardButton("NASIMOVA NIGINA", callback_data="8_b_11"),
            types.InlineKeyboardButton("Ne’matillayev Bahrom", callback_data="8_b_12"),
            types.InlineKeyboardButton("Ne’matullayev Aslbek", callback_data="8_b_13"),
            types.InlineKeyboardButton("Qaxxarov Jasur", callback_data="8_b_14"),
            types.InlineKeyboardButton("Qiichboyev Asilbek", callback_data="8_b_15"),
            types.InlineKeyboardButton("Rabbimova Manzura", callback_data="8_b_16"),
            types.InlineKeyboardButton("Rahmatova Shazzoda", callback_data="8_b_17"),
            types.InlineKeyboardButton("Razmatullaev Asilbek", callback_data="8_b_18"),
            types.InlineKeyboardButton("Razmonova Farangiz", callback_data="8_b_19"),
            types.InlineKeyboardButton("Toshnazarov Diyorbek", callback_data="8_b_20"),
            types.InlineKeyboardButton("Toshternirova Jasmina", callback_data="8_b_21"),
            types.InlineKeyboardButton("Xushbekova Dildora", callback_data="8_b_22"),
            types.InlineKeyboardButton("Yasshilikova Dilnoza", callback_data="8_b_23"),
            types.InlineKeyboardButton("YUSUFOVA JANONA", callback_data="8_b_24"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="8_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_8b)
    # 1.1.9
    elif call.data == "9_sinf":
        sinf9 = types.InlineKeyboardMarkup(row_width=2)
        sinf9.add(
            types.InlineKeyboardButton("9'A'-Sinf", callback_data="9_a_sinf"),
            types.InlineKeyboardButton("9'B'-Sinf", callback_data="9_b_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="sinflar_call")
        )
        bot.edit_message_text("💠 Kerakli sinfni tanlang.", chat_id, msg_id, reply_markup=sinf9)  
    # 9 A 
    elif call.data=="9_a_sinf":
        sinf_9a=types.InlineKeyboardMarkup(row_width=2)
        sinf_9a.add(
            types.InlineKeyboardButton("Abdalimov Sardor", callback_data="9_a_01"),
            types.InlineKeyboardButton("Abduraxmonov Zokir", callback_data="9_a_02"),
            types.InlineKeyboardButton("Axatov Humoyun", callback_data="9_a_03"),
            types.InlineKeyboardButton("Berdikulova Umida", callback_data="9_a_04"),
            types.InlineKeyboardButton("Boltayeva Yasmina", callback_data="9_a_05"),
            types.InlineKeyboardButton("Ergashev Shohrux", callback_data="9_a_06"),
            types.InlineKeyboardButton("G'aybullayev Umidjon", callback_data="9_a_07"),
            types.InlineKeyboardButton("Kenjayev Nodirjon", callback_data="9_a_08"),
            types.InlineKeyboardButton("Muhammadova Marjona", callback_data="9_a_09"),
            types.InlineKeyboardButton("Muratov Rasul", callback_data="9_a_10"),
            types.InlineKeyboardButton("Nosirova Parizoda", callback_data="9_a_11"),
            types.InlineKeyboardButton("Nurmuxammadova E'tibor", callback_data="9_a_12"),
            types.InlineKeyboardButton("O'ng'alova Dilnoza", callback_data="9_a_13"),
            types.InlineKeyboardButton("Safarboyev Elyor", callback_data="9_a_14"),
            types.InlineKeyboardButton("Saparova Shaxzoda", callback_data="9_a_15"),
            types.InlineKeyboardButton("Shodiyarov Behruz", callback_data="9_a_16"),
            types.InlineKeyboardButton("Shodmonov Boboyor", callback_data="9_a_17"),
            types.InlineKeyboardButton("Sultonov Islomjon", callback_data="9_a_18"),
            types.InlineKeyboardButton("To'xtamurodov Odilbek", callback_data="9_a_19"),
            types.InlineKeyboardButton("Xalilov Bexruz", callback_data="9_a_20"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="9_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_9a)
    # 9-B
    elif call.data=="9_b_sinf":
        sinf_9b=types.InlineKeyboardMarkup(row_width=2)
        sinf_9b.add(
            types.InlineKeyboardButton("Abdimominov Asilbek", callback_data="9_b_02"),
            types.InlineKeyboardButton("Abdimuratov Javlon", callback_data="9_b_03"),
            types.InlineKeyboardButton("Abdullayeva E'zoza", callback_data="9_b_04"),
            types.InlineKeyboardButton("Asatillayeva Dihoza", callback_data="9_b_05"),
            types.InlineKeyboardButton("Berdimurodov Temurbek", callback_data="9_b_06"),
            types.InlineKeyboardButton("Berdimurodova Jasmina", callback_data="9_b_07"),
            types.InlineKeyboardButton("Bobirov Elbek", callback_data="9_b_08"),
            types.InlineKeyboardButton("Boyxurozov Shahriyor", callback_data="9_b_09"),
            types.InlineKeyboardButton("Eshnamatova Sevinch", callback_data="9_b_10"),
            types.InlineKeyboardButton("Faxriddinova Dildora", callback_data="9_b_11"),
            types.InlineKeyboardButton("Husanova Farzona", callback_data="9_b_12"),
            types.InlineKeyboardButton("Mahammatov Muzaffar", callback_data="9_b_13"),
            types.InlineKeyboardButton("Nematullayeva Jasmina", callback_data="9_b_14"),
            types.InlineKeyboardButton("Normuxammatov Bobur", callback_data="9_b_15"),
            types.InlineKeyboardButton("Primova Farangiz", callback_data="9_b_16"),
            types.InlineKeyboardButton("Shakarov Azizbek", callback_data="9_b_17"),
            types.InlineKeyboardButton("Suvankulova Nafisa", callback_data="9_b_18"),
            types.InlineKeyboardButton("Toshmamatov Ortiqjon", callback_data="9_b_19"),
            types.InlineKeyboardButton("Xasanov Giyosiddin", callback_data="9_b_20"),
            types.InlineKeyboardButton("Xoldarov Sanjar", callback_data="9_b_21"),
            types.InlineKeyboardButton("Xolmorhinova Farangis", callback_data="9_b_22"),
            types.InlineKeyboardButton("Zakirova Farzona", callback_data="9_b_23"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="9_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_9b)
    # 1.1.10
    elif call.data == "10_sinf":
        sinf10 = types.InlineKeyboardMarkup(row_width=2)
        sinf10.add(
            types.InlineKeyboardButton("10'A'-Sinf", callback_data="10_a_sinf"),
            types.InlineKeyboardButton("10'B'-Sinf", callback_data="10_b_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="sinflar_call")
        )
        bot.edit_message_text("💠 Kerakli sinfni tanlang.", chat_id, msg_id, reply_markup=sinf10)  
    # 10-A
    elif call.data=="10_a_sinf":
        sinf_10a=types.InlineKeyboardMarkup(row_width=2)
        sinf_10a.add(
            types.InlineKeyboardButton("Abdijamilova Adiba", callback_data="10_a_02"),
            types.InlineKeyboardButton("Abdisattarov Umidjon", callback_data="10_a_03"),
            types.InlineKeyboardButton("Abduraxmonova Munisa", callback_data="10_a_04"),
            types.InlineKeyboardButton("Berdimurodova Setora", callback_data="10_a_05"),
            types.InlineKeyboardButton("Ergashova Sabina", callback_data="10_a_06"),
            types.InlineKeyboardButton("Jozilov Doston", callback_data="10_a_07"),
            types.InlineKeyboardButton("Karimov Suxrobjon", callback_data="10_a_08"),
            types.InlineKeyboardButton("Karjavova Sabina", callback_data="10_a_09"),
            types.InlineKeyboardButton("Miltiqboyeva Soxiba", callback_data="10_a_10"),
            types.InlineKeyboardButton("Miraqulova Dilnavo", callback_data="10_a_11"),
            types.InlineKeyboardButton("Pardaboyeva Gulsanam", callback_data="10_a_12"),
            types.InlineKeyboardButton("Quimuxammatova Durdona", callback_data="10_a_13"),
            types.InlineKeyboardButton("Razmonqulov Ozodbek", callback_data="10_a_14"),
            types.InlineKeyboardButton("Saydullayeva Marjona", callback_data="10_a_15"),
            types.InlineKeyboardButton("Toshmuhammedova Ruxsora", callback_data="10_a_16"),
            types.InlineKeyboardButton("Turaboyeva Gulsevar", callback_data="10_a_17"),
            types.InlineKeyboardButton("Xamrayev Xurshidjon", callback_data="10_a_18"),
            types.InlineKeyboardButton("Xolmorminova Guljahon", callback_data="10_a_19"),
            types.InlineKeyboardButton("Xushbekov Aziz", callback_data="10_a_20"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="10_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_10a)
    # 10-B
    elif call.data=="10_b_sinf":
        sinf_10b=types.InlineKeyboardMarkup(row_width=2)
        sinf_10b.add(
            types.InlineKeyboardButton("Abdullayeva Farangiz", callback_data="10_b_02"),
            types.InlineKeyboardButton("Berdigulova Marjona", callback_data="10_b_03"),
            types.InlineKeyboardButton("Karimov Alisher", callback_data="10_b_04"),
            types.InlineKeyboardButton("Komilov Behruzbek", callback_data="10_b_05"),
            types.InlineKeyboardButton("Normatova Rayxona", callback_data="10_b_06"),
            types.InlineKeyboardButton("Raxmonova Osuda", callback_data="10_b_07"),
            types.InlineKeyboardButton("Rizayev Jurabek", callback_data="10_b_08"),
            types.InlineKeyboardButton("Rustamjonov Javoxir", callback_data="10_b_09"),
            types.InlineKeyboardButton("Shodmonova Shalola", callback_data="10_b_10"),
            types.InlineKeyboardButton("Sulaymonov Javlon", callback_data="10_b_11"),
            types.InlineKeyboardButton("Xoldorov Dilshod", callback_data="10_b_12"),
            types.InlineKeyboardButton("Yogubov Jasur", callback_data="10_b_13"),
            types.InlineKeyboardButton("Yunusov Uktam", callback_data="10_b_14"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="10_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_10b)
    # 1.1.11
    elif call.data == "11_sinf":
        sinf11 = types.InlineKeyboardMarkup(row_width=2)
        sinf11.add(
            types.InlineKeyboardButton("11'A'-Sinf", callback_data="11_a_sinf"),
            types.InlineKeyboardButton("11'B'-Sinf", callback_data="11_b_sinf"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="sinflar_call")
        )
        bot.edit_message_text("💠 Kerakli sinfni tanlang.", chat_id, msg_id, reply_markup=sinf11)  
    # 11-A
    elif call.data=="11_a_sinf":
        sinf_11a=types.InlineKeyboardMarkup(row_width=2)
        sinf_11a.add(
            types.InlineKeyboardButton("Abdiboxidov Toshpo'lat", callback_data="11_a_02"),
            types.InlineKeyboardButton("Abdulkarimov Islom", callback_data="11_a_03"),
            types.InlineKeyboardButton("Abdullayeva Shahnoza", callback_data="11_a_04"),
            types.InlineKeyboardButton("Arziyeva Nurgul", callback_data="11_a_05"),
            types.InlineKeyboardButton("Gaybullayeva Marjona", callback_data="11_a_06"),
            types.InlineKeyboardButton("Hamrayeva Dildora", callback_data="11_a_07"),
            types.InlineKeyboardButton("Hasanova Sabrina", callback_data="11_a_08"),
            types.InlineKeyboardButton("Ibadullaev Azizbek", callback_data="11_a_09"),
            types.InlineKeyboardButton("Jumaqulov Umidjon", callback_data="11_a_10"),
            types.InlineKeyboardButton("Mingboyeva Dilafruz", callback_data="11_a_11"),
            types.InlineKeyboardButton("Nematillayeva Farida", callback_data="11_a_12"),
            types.InlineKeyboardButton("Nosirov Doniyor", callback_data="11_a_13"),
            types.InlineKeyboardButton("O'ralova Bahora", callback_data="11_a_14"),
            types.InlineKeyboardButton("Qaytarova Charos", callback_data="11_a_15"),
            types.InlineKeyboardButton("Rustamjonova Shaxlo", callback_data="11_a_16"),
            types.InlineKeyboardButton("Shonazarova Xumora", callback_data="11_a_17"),
            types.InlineKeyboardButton("Shukurova Sevinch", callback_data="11_a_18"),
            types.InlineKeyboardButton("Sulaymonova Sevinch", callback_data="11_a_19"),
            types.InlineKeyboardButton("Tofrayeva Shohsanam", callback_data="11_a_20"),
            types.InlineKeyboardButton("Xidirova Sevinch", callback_data="11_a_21"),
            types.InlineKeyboardButton("Yusupov Bexruz", callback_data="11_a_22"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="11_sinf")
        )
        bot.edit_message_text("🧑‍🎓 Kelmagan o'quvchilarni tanlang! ", chat_id, msg_id, reply_markup=sinf_11a)
    # 11-B
    elif call.data=="11_b_sinf":
        sinf_11b=types.InlineKeyboardMarkup(row_width=2)
        sinf_11b.add(
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="11_sinf")
        )
        bot.edit_message_text("💠 Kechirasiz siz tanlagan sinf topilmadi!", chat_id, msg_id, reply_markup=sinf_11b)
    # 2.5 - 5A-Sinf 
    elif call.data == "5_a_01":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("ABDILLAYEV HASAN")
    elif call.data == "5_a_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("ABDISAMIYEVA SARVINOZ")
    elif call.data == "5_a_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("ABDULLAYEV ELNUR")
    elif call.data == "5_a_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("ABDUNOROVA MUHAYYO")
    elif call.data == "5_a_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("BALTAYEV SHOHRO'Z")
    elif call.data == "5_a_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("BAXRAMOV HASAN")
    elif call.data == "5_a_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("DO'SQULOV BEHRO'Z")
    elif call.data == "5_a_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("ERKINOVA ZARINA")
    elif call.data == "5_a_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("ESHKULOVA RUXSHONA")
    elif call.data == "5_a_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("KUSHBAKOVA SHAHZODA")
    elif call.data == "5_a_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("MIYZAMOVA NASIBA")
    elif call.data == "5_a_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("MUSAYEVA ZILOLA")
    elif call.data == "5_a_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("NEKBAYEV LAZIZBEK")
    elif call.data == "5_a_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("NURMAMATOVA SHAXMIRA")
    elif call.data == "5_a_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("SAYFIDINOV SHOHRO'Z")
    elif call.data == "5_a_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("SHUKUROVA ZILOLA")
    elif call.data == "5_a_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("SIROJOV QODIR")
    elif call.data == "5_a_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("TINCHLIKOVA DINORA")
    elif call.data == "5_a_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("TOYCHIYEV DAVLATBEK")
    elif call.data == "5_a_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("UMIRZAQOVA ZILOLA")
    elif call.data == "5_a_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("XIKMATOV OLIMJON")
    elif call.data == "5_a_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("XOLDOROV ELNUR")
    elif call.data == "5_a_23":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat5.append("YULDOSHEV ORZUBEK")
    # 2.6 - 6A-Sinf
    elif call.data == "6_a_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("ABSOTAROVA SHIRIN")
    elif call.data == "6_a_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("AHROROV OLMOSBEK")
    elif call.data == "6_a_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("BAXTIVOROV ELBEK")
    elif call.data == "6_a_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("FAYZULLAYEV SHAXBOZ")
    elif call.data == "6_a_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("GAYIBNAZAROV AZIZBEK")
    elif call.data == "6_a_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("HUSANOVA ROZA")
    elif call.data == "6_a_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("ISMOILOV ELBEK")
    elif call.data == "6_a_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("MARDIBOYEVA SHOXSANAM")
    elif call.data == "6_a_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("MURODOV DAVLATBEK")
    elif call.data == "6_a_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("NE'MATULLAYEV AZIZBEK")
    elif call.data == "6_a_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("NURILLAYEV ASILBEK")
    elif call.data == "6_a_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("NURMAMATOV ASRORJON")
    elif call.data == "6_a_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("NURMUHAMMADOV UMIDJON")
    elif call.data == "6_a_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("QAYTAROVA ADIBA")
    elif call.data == "6_a_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("SADULLAYEV SHOXRUZBEK")
    elif call.data == "6_a_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("SHAMSITDINOV AZAMAT")
    elif call.data == "6_a_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("TAXAYEV IBROHIMBEK")
    elif call.data == "6_a_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("TO'XTAMURODOV ASLIDDIN")
    elif call.data == "6_a_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("XASANOV HUMOYUN")
    elif call.data == "6_a_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("XOLDOROVA ZUHRA")
    elif call.data == "6_a_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("XO'JAMQULOVA KAMOLA")
    elif call.data == "6_a_23":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6.append("XUSHNAZAROV BEHRUZ")
    # 2.6 - 6B
    elif call.data == "6_b_01":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("ABDAZOV NAVRO'ZALI")
    elif call.data == "6_b_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("ABDUMANONOVA MUXLISA")
    elif call.data == "6_b_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("BABABEKOV DIYORBEK")
    elif call.data == "6_b_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("BAXTIYOROV ELBEK")
    elif call.data == "6_b_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("BERDIQULOVA DINORA")
    elif call.data == "6_b_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("ESONBOYEV DAVRONBEK")
    elif call.data == "6_b_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("HASANOVA DURDONA")
    elif call.data == "6_b_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("HASANOVA SEVINCH")
    elif call.data == "6_b_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("IBRAGIMOV SHEHROZ")
    elif call.data == "6_b_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("MAXMUDOV ABDUG'OLIB")
    elif call.data == "6_b_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("MITANBOYEV ILG'ORBEK")
    elif call.data == "6_b_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("MUSTOFAYEV ELSHOD")
    elif call.data == "6_b_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("OOPULATOV G'ANISHER")
    elif call.data == "6_b_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("QQ'CHQOROV OZODBEK")
    elif call.data == "6_b_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("SAYDIRAXMATOV SHERXON")
    elif call.data == "6_b_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("SHODIYOROV FARHOD")
    elif call.data == "6_b_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("SHODMANOV JAVOHIR")
    elif call.data == "6_b_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("TURGUNOV KOMILJON")
    elif call.data == "6_b_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("XUDOYBERDIYEVA KOMILA")
    elif call.data == "6_b_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("YAXSHILIOOV DIYORBEK")
    elif call.data == "6_b_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("YOGUBOV UCHQUN")
    elif call.data == "6_b_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat6b.append("YUSUPOV SARVARBEK")
    # 2.7 7-A
    elif call.data == "7_a_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("ABDIXASHIMOV ELBEK")
    elif call.data == "7_a_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("ABDULLAYEVA SHAROFAT")
    elif call.data == "7_a_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("AXROROV SARDOR")
    elif call.data == "7_a_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("BAHRAMOV AZAMAT")
    elif call.data == "7_a_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("BEKMURODOV SAMIR")
    elif call.data == "7_a_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("BOLIKULOV OTABEK")
    elif call.data == "7_a_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("ISOMIDDINOVA KIBRIYO")
    elif call.data == "7_a_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("JORAQULOV SHAXRIZOD")
    elif call.data == "7_a_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("NASRIDDINOVA CHAROS")
    elif call.data == "7_a_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("NORMUHAMMADOV SHOHJAXON")
    elif call.data == "7_a_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("NURALIYEVA E'ZOZA")
    elif call.data == "7_a_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("NURGOBILOV MUHAMMADJON")
    elif call.data == "7_a_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("QURBONQULOV SHEROZ")
    elif call.data == "7_a_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("ROZIQULOV RAMZBEK")
    elif call.data == "7_a_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("SAFAROVA CHAROS")
    elif call.data == "7_a_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("SATTAROV BEHRUZ")
    elif call.data == "7_a_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("SAYFULLAYEV XUMOYUN")
    elif call.data == "7_a_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("TIRKASHEVA MUXLISA")
    elif call.data == "7_a_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("TOLISHOVA DIHOZA")
    elif call.data == "7_a_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("TOSHPOLATOV ABUBAKIR")
    elif call.data == "7_a_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("XOLBOYEV ELDOR")
    elif call.data == "7_a_23":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7a.append("YOLDASHEV TEMURBEK")
    # 7-B
    elif call.data == "7_b_01":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("ABDUSAMATOVA E'ZOZA")
    elif call.data == "7_b_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("ABDUVOHOBOV BOBUR")
    elif call.data == "7_b_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("ASATULLAYEV ULUG'BEK")
    elif call.data == "7_b_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("BOTIROV BAXTBEK")
    elif call.data == "7_b_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("DONAQULOVA MARJONA")
    elif call.data == "7_b_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("HUBBIMOV AHMADJON")
    elif call.data == "7_b_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("MAMASOLIEV SARDOR")
    elif call.data == "7_b_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("MUHAMMADOVA FARANGIZ")
    elif call.data == "7_b_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("NURULLAYEVA SEVINCH")
    elif call.data == "7_b_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("PARDABOYEV ALIBEK")
    elif call.data == "7_b_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("QUIMUHAMMADOV SHAXBOZ")
    elif call.data == "7_b_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("RADJABOV SARDOR")
    elif call.data == "7_b_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("RASULOV ABDULAZIZ")
    elif call.data == "7_b_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("RAVSHANOV DAVRONBEK")
    elif call.data == "7_b_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("RUSTAMOVA DURDONA")
    elif call.data == "7_b_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("SAIDOV XUSHNUDXON")
    elif call.data == "7_b_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("SAYDIRAXMATOVA DILNURA")
    elif call.data == "7_b_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("SAYFULLAYEV LAZIZBEK")
    elif call.data == "7_b_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("SHUKUROV SARDORJON")
    elif call.data == "7_b_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("TOSHIMAMATOVA GULBAHOR")
    elif call.data == "7_b_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("TUXTAMURODOV OBIDJON")
    elif call.data == "7_b_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("UBAYDULLAYEV ISLOMJON")
    elif call.data == "7_b_23":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat7b.append("YUNUSOVA SHABANAM")
    # 2.8 - 8-A
    elif call.data == "8_a_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("ABDUMALIKOVA UMIDA")
    elif call.data == "8_a_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("ABDUNAZAROVA AZIZA")
    elif call.data == "8_a_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("ABDURAXIMOV RAMAZON")
    elif call.data == "8_a_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("ABDXAILIOVA UMIDA")
    elif call.data == "8_a_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("ALIBEKOV ASADBEK")
    elif call.data == "8_a_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("JOFRAMURODOVA MOHINUR")
    elif call.data == "8_a_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("JUMAQULOVA SEVINCH")
    elif call.data == "8_a_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("KAMONOV TOSHTEMUR")
    elif call.data == "8_a_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("KARIMOV RASULBEK")
    elif call.data == "8_a_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("MUHAMMADQULOVA SEVINCH")
    elif call.data == "8_a_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("NEMATULLAYEVA RAYXONA")
    elif call.data == "8_a_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("NORBOYEV BEHRO'Z")
    elif call.data == "8_a_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("NORTAYEVA NAFISA")
    elif call.data == "8_a_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("NURMAMATOVA FARNOZA")
    elif call.data == "8_a_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("NURMUHAMMADOV SHAXZODJON")
    elif call.data == "8_a_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("ORTIGBOYEV MATLAB")
    elif call.data == "8_a_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("SHAMSIDDINOVA POKIZA")
    elif call.data == "8_a_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("TOLLIBOYEVA MARXABO")
    elif call.data == "8_a_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("TOYIROVA MUSHTARIY")
    elif call.data == "8_a_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("UROLOV RAMAZON")
    elif call.data == "8_a_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("YAKUBOVA SAIDA")
    elif call.data == "8_a_23":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8a.append("YUSUPOV QUVONCHBEK")
    # 8-B
    elif call.data == "8_b_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("ACHILOV ABDULAZIZ")
    elif call.data == "8_b_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Bahodirov Javohir")
    elif call.data == "8_b_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Bektosheva Ruxshona")
    elif call.data == "8_b_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Berkinov Sohibjon")
    elif call.data == "8_b_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Joraqulov Hushnudbek")
    elif call.data == "8_b_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Maxammadov Behro'z")
    elif call.data == "8_b_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Miltiqov Behruzjon")
    elif call.data == "8_b_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Nasimova Nigina")
    elif call.data == "8_b_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Ne'matillayev Bahrom")
    elif call.data == "8_b_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Ne'matullayev Aslbek")
    elif call.data == "8_b_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Qaxxarov Jasur")
    elif call.data == "8_b_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Qiichboyev Asilbek")
    elif call.data == "8_b_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Rabbimova Manzura")
    elif call.data == "8_b_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Rahmatova Shazzoda")
    elif call.data == "8_b_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Razmatullaev Asilbek")
    elif call.data == "8_b_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Razmonova Farangiz")
    elif call.data == "8_b_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Toshnazarov Diyorbek")
    elif call.data == "8_b_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Toshternirova Jasmina")
    elif call.data == "8_b_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Xushbekova Dildora")
    elif call.data == "8_b_23":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Yasshilikova Dilnoza")
    elif call.data == "8_b_24":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat8b.append("Yusufova Janona")
# 2.9 - 9A-Sinf 
    elif call.data == "9_a_01":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Abdalimov Sardor")
    elif call.data == "9_a_02":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Abduraxmonov Zokir")
    elif call.data == "9_a_03":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Axatov Humoyun")
    elif call.data == "9_a_04":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Berdiqulova Umida")
    elif call.data == "9_a_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("Boltayeva Yasmina")
    elif call.data == "9_a_06":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Ergashev Shohrux")
    elif call.data == "9_a_07":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("G'aybullayev Umidjon")
    elif call.data == "9_a_08":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Kenjayev Nodirjon")
    elif call.data == "9_a_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("Muhammadova Marjona")
    elif call.data == "9_a_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("Muratov Rasul")
    elif call.data == "9_a_11":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Nosirova Parizoda")
    elif call.data == "9_a_12":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Nurmuxammadova E'tibor")
    elif call.data == "9_a_13":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("O'ng'alova Dilnoza")
    elif call.data == "9_a_14":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Safarboyev Elyor")
    elif call.data == "9_a_15":
        bot.answer_callback_query(call.id,  "O'quvchi kelmagan ✅")
        davomat.append("Saparova Shaxrizoda")
    elif call.data == "9_a_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("Shodiyarov Behruz")
    elif call.data == "9_a_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("Shodmonov Boboyor")
    elif call.data == "9_a_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("Sultonov Islomjon")
    elif call.data == "9_a_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("To'xtamurodov Odilbek")
    elif call.data == "9_a_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat.append("Xalilov Bexruz")
    # 9-B
    elif call.data == "9_b_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Abdimominov Asilbek")
    elif call.data == "9_b_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Abdimuratov Javlon")
    elif call.data == "9_b_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Abdullayeva E'zoza")
    elif call.data == "9_b_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Asatillayeva Dihoza")
    elif call.data == "9_b_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Berdimurodov Temurbek")
    elif call.data == "9_b_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Berdimurodova Jasmina")
    elif call.data == "9_b_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Bobirov Elbek")
    elif call.data == "9_b_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Boyxurozov Shahriyor")
    elif call.data == "9_b_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Eshnamatova Sevinch")
    elif call.data == "9_b_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Faxriddinova Dildora")
    elif call.data == "9_b_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Husanova Farzona")
    elif call.data == "9_b_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Mahammatov Muzaffar")
    elif call.data == "9_b_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Nematullayeva Jasmina")
    elif call.data == "9_b_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Normuxammatov Bobur")
    elif call.data == "9_b_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Primova Farangiz")
    elif call.data == "9_b_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Shakarov Azizbek")
    elif call.data == "9_b_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Suvankulova Nafisa")
    elif call.data == "9_b_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Toshmamatov Ortiqjon")
    elif call.data == "9_b_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Xasanov Giyosiddin")
    elif call.data == "9_b_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Xoldarov Sanjar")
    elif call.data == "9_b_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Xolmorhinova Farangis")
    elif call.data == "9_b_23":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat9b.append("Zakirova Farzona")
    # 10-A
    elif call.data == "10_a_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Abdijamilova Adiba")

    elif call.data == "10_a_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Abdisattarov Umidjon")

    elif call.data == "10_a_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Abduraxmonova Munisa")

    elif call.data == "10_a_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Berdimurodova Setora")

    elif call.data == "10_a_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Ergashova Sabina")

    elif call.data == "10_a_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Jozilov Doston")

    elif call.data == "10_a_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Karimov Suxrobjon")

    elif call.data == "10_a_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Karjavova Sabina")

    elif call.data == "10_a_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Miltiqboyeva Soxiba")

    elif call.data == "10_a_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Miraqulova Dilnavo")

    elif call.data == "10_a_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Pardaboyeva Gulsanam")

    elif call.data == "10_a_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Quimuxammatova Durdona")

    elif call.data == "10_a_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Razmonqulov Ozodbek")

    elif call.data == "10_a_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Saydullayeva Marjona")

    elif call.data == "10_a_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Toshmuhammedova Ruxsora")

    elif call.data == "10_a_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Turaboyeva Gulsevar")

    elif call.data == "10_a_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Xamrayev Xurshidjon")

    elif call.data == "10_a_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Xolmorminova Guljahon")

    elif call.data == "10_a_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10a.append("Xushbekov Aziz")
    # 10-B
    elif call.data == "10_b_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Abdullayeva Farangiz")

    elif call.data == "10_b_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Berdigulova Marjona")

    elif call.data == "10_b_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Karimov Alisher")

    elif call.data == "10_b_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Komilov Behruzbek")

    elif call.data == "10_b_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Normatova Rayxona")

    elif call.data == "10_b_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Raxmonova Osuda")

    elif call.data == "10_b_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Rizayev Jurabek")

    elif call.data == "10_b_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Rustamjonov Javoxir")

    elif call.data == "10_b_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Shodmonova Shalola")

    elif call.data == "10_b_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Sulaymonov Javlon")

    elif call.data == "10_b_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Xoldorov Dilshod")

    elif call.data == "10_b_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Yogubov Jasur")

    elif call.data == "10_b_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat10b.append("Yunusov Uktam")
    # 11-A
    elif call.data == "11_a_02":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Abdiboxidov Toshpo'lat")

    elif call.data == "11_a_03":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Abdulkarimov Islom")

    elif call.data == "11_a_04":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Abdullayeva Shahnoza")

    elif call.data == "11_a_05":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Arziyeva Nurgul")
    elif call.data == "11_a_06":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Gaybullayeva Marjona")
    elif call.data == "11_a_07":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Hamrayeva Dildora")
    elif call.data == "11_a_08":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Hasanova Sabrina")
    elif call.data == "11_a_09":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Ibadullaev Azizbek")
    elif call.data == "11_a_10":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Jumaqulov Umidjon")
    elif call.data == "11_a_11":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Mingboyeva Dilafruz")
    elif call.data == "11_a_12":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Nematillayeva Farida")
    elif call.data == "11_a_13":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Nosirov Doniyor")
    elif call.data == "11_a_14":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("O'ralova Bahora")
    elif call.data == "11_a_15":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Qaytarova Charos")
    elif call.data == "11_a_16":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Rustamjonova Shaxlo")
    elif call.data == "11_a_17":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Shonazarova Xumora")
    elif call.data == "11_a_18":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Shukurova Sevinch")
    elif call.data == "11_a_19":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Sulaymonova Sevinch")
    elif call.data == "11_a_20":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Tofrayeva Shohsanam")
    elif call.data == "11_a_21":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Xidirova Sevinch")
    elif call.data == "11_a_22":
        bot.answer_callback_query(call.id, "O'quvchi kelmagan ✅")
        davomat11a.append("Yusupov Bexruz")
    # Fanlar menyusi
    elif call.data == "fanlar_call":
        fanlarr = types.InlineKeyboardMarkup(row_width=2)
        fanlarr.add(
            types.InlineKeyboardButton("📘 Matematika", callback_data="matem_call"),
            types.InlineKeyboardButton("📙 Fizika", callback_data="fizika_call"),
            types.InlineKeyboardButton("📕 Ingliz tili", callback_data="ingliz_call"),
            types.InlineKeyboardButton("📗 Informatika", callback_data="infor_call"),
            types.InlineKeyboardButton("🔙 Orqaga", callback_data="back_main")
        )
        bot.edit_message_text("⚙️ Sozlamalar bo‘limi:", chat_id, msg_id, reply_markup=fanlarr)


# Davomatni bilish buyruqlari 
@bot.message_handler(commands=['davomat9a'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"9'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat)}")

@bot.message_handler(commands=['davomat5'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"5'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat5)}")

@bot.message_handler(commands=['davomat6a'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"6'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat6)}")

@bot.message_handler(commands=['davomat6b'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"6'B'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat6b)}")

@bot.message_handler(commands=['davomat7a'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"7'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat7a)}")

@bot.message_handler(commands=['davomat7b'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"7'B'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat7b)}")

@bot.message_handler(commands=['davomat8a'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"8'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat8a)}")

@bot.message_handler(commands=['davomat8b'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"8'B'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat8b)}")

@bot.message_handler(commands=['davomat9b'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"9'B'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat9b)}")

@bot.message_handler(commands=['davomat10a'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"10'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat10a)}")

@bot.message_handler(commands=['davomat10b'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"10'B'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat10b)}")   

@bot.message_handler(commands=['davomat11a'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"11'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat11a)}")

@bot.message_handler(commands=['davomat11b'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, f"11'A'-sinfdan kelmagan o'quvchilar ro'yhati: {set(davomat11b)}")

bot.polling()