import arcade
import random
import os

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Simon Says - With Sound"

COLORS = [
    (arcade.color.RED, arcade.color.DARK_RED),
    (arcade.color.BLUE, arcade.color.DARK_BLUE),
    (arcade.color.GREEN, arcade.color.DARK_GREEN),
    (arcade.color.YELLOW, arcade.color.GOLDENROD)
]


class SimonSays(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.BLACK

        self.sequence = []
        self.player_index = 0
        self.is_flashing = False
        self.flash_index = 0
        self.active_color = -1
        self.timer = 0
        self.click_timer = 0

        self.message = "Press SPACE to Start"
        self.game_over = False

        # --- SOUND LOADING ---
        self.sounds = []
        sound_files = ["red.wav", "blue.wav", "green.wav", "yellow.wav"]

        for file in sound_files:
            if os.path.exists(file):
                self.sounds.append(arcade.load_sound(file))
            else:
                self.sounds.append(None)
                print(f"Warning: {file} not found. Beeps will not play.")

    def play_color_sound(self, index):
        """Helper to play sound if the file exists."""
        if index != -1 and self.sounds[index]:
            arcade.play_sound(self.sounds[index])

    def start_new_round(self):
        self.sequence.append(random.randint(0, 3))
        self.player_index = 0
        self.is_flashing = True
        self.flash_index = 0
        self.timer = 0
        self.active_color = -1
        self.message = "Watch..."

    def on_draw(self):
        self.clear()
        positions = [(150, 450), (450, 450), (150, 150), (450, 150)]

        for i in range(4):
            color = COLORS[i][0] if self.active_color == i else COLORS[i][1]
            arcade.draw_rect_filled(
                arcade.XYWH(positions[i][0], positions[i][1], 280, 280),
                color
            )

        arcade.draw_text(self.message, SCREEN_WIDTH / 2, 300, arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text(f"Score: {len(self.sequence)}", 20, 560, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        if self.is_flashing:
            self.timer += delta_time
            if self.timer > 0.5:
                self.timer = 0
                if self.active_color == -1:
                    if self.flash_index < len(self.sequence):
                        self.active_color = self.sequence[self.flash_index]
                        self.play_color_sound(self.active_color)  # PLAY SOUND ON FLASH
                    else:
                        self.is_flashing = False
                        self.message = "Your turn!"
                        self.flash_index = 0
                else:
                    self.active_color = -1
                    self.flash_index += 1

        if self.click_timer > 0:
            self.click_timer -= delta_time
            if self.click_timer <= 0:
                self.active_color = -1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.game_over or len(self.sequence) == 0:
                self.sequence = []
                self.game_over = False
                self.start_new_round()

    def on_mouse_press(self, x, y, button, modifiers):
        if self.is_flashing or self.game_over or not self.sequence:
            return

        clicked = -1
        if x < 300 and y > 300:
            clicked = 0
        elif x > 300 and y > 300:
            clicked = 1
        elif x < 300 and y < 300:
            clicked = 2
        elif x > 300 and y < 300:
            clicked = 3

        if clicked != -1:
            self.active_color = clicked
            self.click_timer = 0.25
            self.play_color_sound(clicked)  # PLAY SOUND ON CLICK

            if clicked == self.sequence[self.player_index]:
                self.player_index += 1
                if self.player_index >= len(self.sequence):
                    self.message = "Correct!"
                    self.is_flashing = True
                    self.timer = -0.5
                    self.flash_index = 0
                    self.sequence.append(random.randint(0, 3))
                    self.player_index = 0
            else:
                self.message = "WRONG! Space to Restart"
                self.game_over = True


def main():
    game = SimonSays()
    arcade.run()


if __name__ == "__main__":
    main()