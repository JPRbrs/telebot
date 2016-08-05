import telepot, time
import pywapi
import pdb

def get_weather():
# Returns a dict with two keys: out_feel and out_conditions
    return pywapi.get_weather_from_weather_com('BS3:4:UK')

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    if command == '/hello':
        bot.sendMessage(chat_id, "Hello, how are you?")
    elif command == '/weather':
        weather = get_weather()
        message = 'It is {} and feels {} out there' .format(\
            weather['current_conditions']['text'],
            weather['current_conditions']['feels_like'])
        bot.sendMessage(chat_id, message)
    elif command == '/tomorrow':
        weather = get_weather()
        pdb.set_trace()
        message = 'The chances or rain tomorrow are {}'.format(\
            weather['forecasts'][0]['day']['chance_precip'])
        if  int(weather['forecasts'][0]['day']['chance_precip']) < 15:
            message += '. Pretty good!'
        else:
            message += '. It might rain'
        bot.sendMessage(chat_id, message)

# Create a bot object with API key
bot = telepot.Bot('230469362:AAEUZX6ufOd8nNcwX1hmy86Pb0Edq3U-r_A')
bot.message_loop(handle)

while 1:
  time.sleep(10)
