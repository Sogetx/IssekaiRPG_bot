from Events.Event import Event


class Church(Event):
    def __init__(self):
        super().__init__()
        self.description = "Вы заходите в небольшое святилище, оно аккуратное, чистое хотя никого в нем нету. Постояв у алтаря вам становиться легче а раны затягиваються"
