class Queue:

    def __init__(self, queue_id: int):

        self.__queue_id = queue_id
        self.__max_players = 8
        self.__players: set(int) = set()
        self.__frozen = False

    def add_player(self, user_id: int):

        self.__players.add(user_id)

    def remove_player(self, user_id: int):

        self.__players.remove(user_id)

    def freeze(self):

        self.__frozen = True

    def unfreeze(self):

        self.__frozen = False

    def is_frozen(self):

        return self.__frozen

    def set_max_players(self, max_players: int):

        self.__max_players = max_players

    def is_full(self):

        return len(self.__players) >= self.__max_players

    def get_players(self):

        return self.__players

    def get_max_players(self):
        
        return self.__max_players

    def clear(self):

        self.__players = set()