import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                            QLabel, QVBoxLayout, QWidget, QHBoxLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon

class RockPaperScissors(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.setMinimumSize(600, 400)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 18px;
                color: #333;
            }
        """)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Title
        title = QLabel("Rock Paper Scissors")
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Score display
        self.score_label = QLabel("Score: 0 - 0")
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.score_label)

        # Result display
        self.result_label = QLabel("Choose your move!")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        # Player and computer choice display
        choices_layout = QHBoxLayout()
        self.player_choice = QLabel("Your choice: -")
        self.computer_choice = QLabel("Computer's choice: -")
        choices_layout.addWidget(self.player_choice)
        choices_layout.addWidget(self.computer_choice)
        layout.addLayout(choices_layout)

        # Buttons layout
        buttons_layout = QHBoxLayout()
        
        # Rock button
        self.rock_btn = QPushButton("Rock")
        self.rock_btn.setFixedSize(100, 50)
        self.rock_btn.clicked.connect(lambda: self.play("rock"))
        buttons_layout.addWidget(self.rock_btn)

        # Paper button
        self.paper_btn = QPushButton("Paper")
        self.paper_btn.setFixedSize(100, 50)
        self.paper_btn.clicked.connect(lambda: self.play("paper"))
        buttons_layout.addWidget(self.paper_btn)

        # Scissors button
        self.scissors_btn = QPushButton("Scissors")
        self.scissors_btn.setFixedSize(100, 50)
        self.scissors_btn.clicked.connect(lambda: self.play("scissors"))
        buttons_layout.addWidget(self.scissors_btn)

        layout.addLayout(buttons_layout)

        # Initialize game variables
        self.player_score = 0
        self.computer_score = 0

    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        self.player_choice.setText(f"Your choice: {player_choice.capitalize()}")
        self.computer_choice.setText(f"Computer's choice: {computer_choice.capitalize()}")

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.result_label.setText(result)
        self.score_label.setText(f"Score: {self.player_score} - {self.computer_score}")

def main():
    app = QApplication(sys.argv)
    game = RockPaperScissors()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 