# Требования:
#   1.  Класс Player (Игрок)
#   •  Свойства:
#   •  name (имя игрока)
#   •  rating (рейтинг игрока)
#   •  Методы:
#   •  get_info() – возвращает строку с именем и рейтингом.
#   2.  Класс Match (Матч)
#   •  Свойства:
#   •  player1 (первый игрок)
#   •  player2 (второй игрок)
#   •  winner (победитель, изначально None)
#   •  Методы:
#   •  play(winner) – принимает победителя (player1 или player2) и обновляет его рейтинг.
#   3.  Класс Tournament (Турнир)
#   •  Свойства:
#   •  name (название турнира)
#   •  players (список игроков)
#   •  matches (список матчей)
#   •  Методы:
#   •  add_player(player) – добавляет игрока в турнир.
#   •  schedule_match(player1, player2) – создаёт матч между двумя игроками.
#   •  record_result(match, winner) – записывает результат матча.
#   •  show_standings() – показывает список игроков и их рейтинги.

class Player:
    def __init__(self, name: str, rating: int):
        self.name = name
        self.rating = rating

    def get_info(self):
        return f"Player {self.name}. Rating: {self.rating}"


class Match:
    def __init__(self, player1: Player, player2: Player):
        self.first_player = player1
        self.second_player = player2
        self.winner = None

    def play(self, player: Player):
        if player not in [self.first_player, self.second_player]:
            print(f"The winner is not match participant.")
            return
        player.rating += 10


class Tournament:
    def __init__(self, name: str):
        self.name = name
        self.players = []
        self.matches = []

    def add_player(self, player: Player):
        if len(self.players)>2:
            print("There can only be 2 players.")
            return
        self.players.append(player)


    def schedule_match(self, player1:Player, player2:Player):
        for player in self.players:
            if player not in [player1,player2]:
                print(f"{player.get_info()} - Unknown player")
                return
        return Match(player1, player2)

    def record_result(self, match:Match, winner:Player):
        self.matches.append(match.play(winner))

    def show_standings(self):
        if len(self.players)!=2:
            print("There must be 2 players")
            return
        print(f"Rating:")
        for player in self.players:
            print(player.get_info())


tournament = Tournament("Quake")
tournament.show_standings()
player1 = Player("Anton", 2150)
player2 = Player("Dima",1972)
tournament.add_player(player1)
tournament.show_standings()
tournament.add_player(player2)
tournament.show_standings()
match1 = tournament.schedule_match(player1, player2)
tournament.record_result(match1,player1)
tournament.show_standings()
