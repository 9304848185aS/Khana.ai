import webbrowser

from kivy.utils import platform


class VoiceControlController:

    def __init__(self):
        self.platform = platform

    def open_website(self, url):
        try:
            webbrowser.open(url)
            return "Website opened successfully."
        except Exception as e:
            return f"Error: {e}"

    def open_app(self, package_name):
        try:
            if self.platform == "android":
                from jnius import autoclass

                PythonActivity = autoclass(
                    'org.kivy.android.PythonActivity'
                )

                activity = PythonActivity.mActivity

                package_manager = activity.getPackageManager()

                intent = package_manager.getLaunchIntentForPackage(
                    package_name
                )

                if intent is not None:
                    activity.startActivity(intent)
                    return "App opened successfully."

                return "App not found."

            return "Android device required."

        except Exception as e:
            return f"Error: {e}"

    def open_youtube(self):
        return self.open_app("com.google.android.youtube")

    def open_chrome(self):
        return self.open_app("com.android.chrome")

    def open_whatsapp(self):
        return self.open_app("com.whatsapp")
