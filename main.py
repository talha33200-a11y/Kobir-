from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

class TelegramApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.input = TextInput(hint_text='এখানে লিখুন...')
        self.layout.add_widget(self.input)
        
        self.button = Button(text='পাঠান')
        self.button.bind(on_press=self.send_to_telegram)
        self.layout.add_widget(self.button)
        return self.layout

    def send_to_telegram(self, instance):
        text = self.input.text
        token = '8847510240:AAGLwyKgmC76FBS_KsAR8FCydRJM9M_dDBo'
        chat_id = '7712859116'
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        requests.post(url, data={'chat_id': chat_id, 'text': text})

if __name__ == '__main__':
    TelegramApp().run()