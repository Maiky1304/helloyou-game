import time

from storyline import story
from enum import Enum


class PartType(Enum):
    QUESTION = 1
    STORY = 2


class Game:
    def __init__(self):
        self.story = story['story']
        self.current = "1"
        self.subpart = None

    def start(self):
        self.display_part()

    def display_part(self, notification=None):
        self.clear_screen()
        pd = self.part_data()
        self.send(f" | {pd['title']}")
        if notification is not None:
            print(f"    {notification}")
        part_type = PartType[pd['type']]
        if part_type == PartType.QUESTION and pd['options'] is not None:
            self.send(" ")
            for i in range(0, len(pd['options'])):
                self.send(f"  {str(i + 1)}. {pd['options'][i]['text']}")
            self.send(" ")
            self.handle_input(input(' > '))
        else:
            time.sleep(4)
            self.next_part(pd)



    def handle_input(self, input_el):
        if input_el is None or input_el == '':
            self.display_part(notification="Je hebt niks ingevoerd.")
            return

        pd = self.part_data()
        chosen = pd['options'][int(input_el)-1]

        if chosen is None:
            self.display_part(notification="Dit was geen optie.")
            return
        self.next_part(chosen)

    def next_part(self, target):
        if 'close_app' in target and target['close_app']:
            exit(0)
            return

        if self.subpart is not None:
            self.subpart = None
        next_part = target['target']
        if next_part == "-":
            self.display_part(notification="Part was setup incorrectly")
            return
        if next_part.startswith('S'):
            self.subpart = next_part
            self.display_part()
            return
        self.current = next_part
        self.display_part()


    def part_data(self):
        if self.subpart is not None:
            return self.story[self.current]['substories'][self.subpart[1:2]]
        return self.story[self.current]

    @staticmethod
    def clear_screen():
        print(1000*"\n")

    @staticmethod
    def send(text):
        print(text)

    def stop(self):
        self.send('Bedankt voor het spelen!')


if __name__ == "__main__":
    game = Game()
    try:
        game.start()
    except KeyboardInterrupt:
        game.stop()
