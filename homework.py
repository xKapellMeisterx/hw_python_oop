class InfoMessage:
    """Базовый класс тренировки."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self):
        """Информация о выполненной тренировке."""
        p = asdict(InfoMessage(self))
        return (
            f"Тип тренировки {self.training_type}, длительность {self.duration}, дистанция {self.distance},"
            f" {self.speed}, {self.calories}".format(**p))


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1: float = 0

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.coeff_calorie_1 = (18 * self.get_mean_speed() - 20) * self.weight / self.M_IN_KM * self.duration * 60
        return self.coeff_calorie_1


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_calorie_2: float = 0

    def __init__(self,
                 action: int,
                 duration: float,
                 weight :float,
                 height: float,
                 ) -> None:
        Training.__init__(self, action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.coeff_calorie_2 = (0.035 * self.weight + (self.get_mean_speed() ** 2 // self.height))
        return self.coeff_calorie_2


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    coeff_calorie_3: float = 0

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 lenght_pool: float,
                 count_pool: float,
                 ) -> None:
        Training.__init__(self, action, duration, weight)
        self.lenght_pool = lenght_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.lenght_pool * self.count_pool / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.coeff_calorie_3 = (self.get_mean_speed() + 1.1) * 2 * self.weight
        return self.coeff_calorie_3



def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)


