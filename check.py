
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
        return self.action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration







class Swimming(Training):
    """Тренировка: плавание."""
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
        return self.lenght_pool * self.count_pool / M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        self.coeff_calorie_3 = (self.get_mean_speed() + 1.1) * 2 * self.weight
        return self.coeff_calorie_3

с = Swimming(720, 1, 80, 25, 40)

print(c)