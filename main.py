from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform


class KanaAI(App):

    def build(self):
        self.title = "Kana AI"

        Window.clearcolor = (0.08, 0.09, 0.13, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="[b]KANA AI[/b]",
            markup=True,
            font_size=32,
            size_hint=(1, 0.2)
        )

        self.status = Label(
            text="Hello! I am Kana AI.",
            font_size=18,
            size_hint=(1, 0.2)
        )

        self.command = TextInput(
            hint_text="Type your command here...",
            multiline=False,
            size_hint=(1, 0.15),
            font_size=18
        )

        send_button = Button(
            text="Send Command",
            size_hint=(1, 0.15),
            font_size=18
        )

        send_button.bind(on_press=self.process_command)

        layout.add_widget(title)
        layout.add_widget(self.status)
        layout.add_widget(self.command)
        layout.add_widget(send_button)

        return layout

    def process_command(self, instance):
        text = self.command.text.strip().lower()

        if not text:
            self.status.text = "Please enter a command."
            return

        if "hello" in text or "hi" in text:
            self.status.text = "Hello! How can I help you?"

        elif "kana" in text:
            self.status.text = "Yes, I am Kana AI."

        elif "help" in text:
            self.status.text = "Tell me what you want me to do."

        else:
            self.status.text = "Command received: " + text

        self.command.text = ""


if __name__ == "__main__":
    KanaAI().run()
